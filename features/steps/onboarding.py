from behave import *
from selenium.webdriver.common.by import By
from features.utils import assert_element_found, do_swipe_jesture
from features.locators import *
use_step_matcher("re")


@given("activity started normally")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver
    element = (By.ID, ONBOARD_TITLE % context.bundle)
    assert_element_found(context, element, text='Покупайте авиабилеты быстрее, чем за 2 минуты')


@then("user swipes on-boarding")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    texts = [
        'Регистрируйтесь на рейс меньше, чем за 49 секунд',
        'Печатайте посадочные билеты с помощью терминалов в аэропорту',
        'Следите за бонусным балансом'
    ]
    for text in texts:
        do_swipe_jesture(context)
        element = (By.ID, ONBOARD_TITLE % context.bundle)
        assert_element_found(context, element, text=text)


@then("user sees finish button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    element = (By.ID, BEGIN_BUTTON % context.bundle)
    result = assert_element_found(context, element)
    result.click()
