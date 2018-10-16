import os
from os.path import isfile, join, abspath, dirname, getmtime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.helpers.configs import *

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
    recent_file = get_recent_file(HOME_LOCATION)
    full_path = '{}{}'.format(HOME_LOCATION, recent_file)
    desired_caps = CAPS
    desired_caps["app"] = PATH(full_path)
    return desired_caps


def do_swipe_jesture(context):
    size = context.driver.get_window_size()
    startx, starty = int(size['width']) - 40, int(size['height']) * 0.5
    endx, endy = int(size['width']) * 0.2, int(size['height']) * 0.5
    context.driver.swipe(startx, starty, endx, endy, 300)


def assert_element_found(context, element, text=None):
    WebDriverWait(context.driver, 120).until(
        EC.presence_of_element_located(element)
    )
    try:
        if text:
            assert context.driver.find_element(*element).is_displayed() is True
            assert context.driver.find_element(*element).text == text
            return context.driver.find_element(*element)
        else:
            assert context.driver.find_element(*element).is_displayed() is True
            return context.driver.find_element(*element)
    except AssertionError as error:
        error.args += ('Element with text "%s" is not displayed' % text,)
        raise
