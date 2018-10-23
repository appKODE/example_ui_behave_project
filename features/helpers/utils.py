import os
from os.path import isfile, join, abspath, dirname, getmtime
from random import choice
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.helpers.configs import *
from features.helpers.locators import DATE_CANCEL, DATE_OK

# Returns abs path relative to this file and not cwd
PATH = lambda p: abspath(
    join(dirname(__file__), p)
)


def get_recent_file(mypath):
    files_tuple = [(f, int(getmtime(join(mypath, f)))) for f in os.listdir(mypath) if isfile(join(mypath, f))]
    sort_by_update = sorted(files_tuple, key=lambda file: file[1])
    return sort_by_update[-1][0]


def get_bundle(filename):
    if 'dev' in filename:
        return INTERNAL
    elif 'alpha' in filename:
        return ALPHA
    else:
        return RELEASE


def get_capabilities():
    recent_file = get_recent_file(DOCKER_LOCATION)
    full_path = '{}{}'.format(REMOTE_LOCATION, recent_file)
    desired_caps = CAPS
    desired_caps["app"] = PATH(full_path)
    return desired_caps


def do_swipe_jesture(context):
    size = context.driver.get_window_size()
    startx, starty = int(size['width']) * 0.7, int(size['height']) * 0.5
    endx, endy = int(size['width']) * 0.1, int(size['height']) * 0.5
    context.driver.swipe(startx, starty, endx, endy, 300)


def assert_element_found(context, element, text=None):
    WebDriverWait(context.driver, 120).until(
        EC.presence_of_element_located(element)
    )
    try:
        if text:
            assert context.driver.find_element(*element).is_displayed() is True
            assert text in context.driver.find_element(*element).text
            return context.driver.find_element(*element)
        else:
            assert context.driver.find_element(*element).is_displayed() is True
            return context.driver.find_element(*element)
    except AssertionError as error:
        error.args += ('Element with text "%s" is not displayed' % text,)
        raise


def assert_elements_found(context, element, text=None):
    WebDriverWait(context.driver, 120).until(
        EC.presence_of_element_located(element)
    )
    try:
        if text:
            result = [item for item in context.driver.find_elements(*element) if text in item.text]
            assert result
            assert result[0].is_displayed() is True
            return result[0]
        else:
            assert context.driver.find_elements(*element)[0].is_displayed() is True
            return context.driver.find_elements(*element)[0]
    except AssertionError as error:
        error.args += ('Element with text "%s" is not displayed' % text,)
        raise


def set_bundle_to_locator(locator, bundle):
    return (locator[0], locator[1] % bundle)


def date_picker(context, element):
    WebDriverWait(context.driver, 120).until(
        EC.presence_of_element_located(element)
    )
    try:
        result = [item for item in context.driver.find_elements(*element) if item.is_enabled()]
        none = set_bundle_to_locator(DATE_CANCEL, context.bundle)
        if result:
            new_element = choice(result)
            new_element.click()
            new_element = set_bundle_to_locator(DATE_OK, context.bundle)
            assert_element_found(context, new_element).click()
        else:
            context.driver.find_element(*none).click()
    except AssertionError as error:
        error.args += ('Date is not displayed',)
        raise


def do_scroll_jesture(context, direction):
    """
    :param context: behave.runner.Context
    :param direction: 'up' or 'down'
    :return: None
    """
    if direction == 'down':
        size = context.driver.get_window_size()
        startx, starty = int(size['width']) * 0.5, int(size['height']) * 0.9
        endx, endy = int(size['width']) * 0.5, int(size['height']) * 0.2
        context.driver.swipe(startx, starty, endx, endy, 300)
    elif direction == 'up':
        size = context.driver.get_window_size()
        startx, starty = int(size['width']) * 0.5, int(size['height']) * 0.2
        endx, endy = int(size['width']) * 0.5, int(size['height']) * 0.9
        context.driver.swipe(startx, starty, endx, endy, 300)
