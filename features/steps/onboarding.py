from behave import *
from time import sleep
from features.helpers.utils import assert_element_found, do_swipe_jesture, set_bundle_to_locator
from features.helpers.locators import *
use_step_matcher("re")


@given("activity started normally")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver
    element = set_bundle_to_locator(ONBOARD_TITLE, context.bundle)
    assert_element_found(context, element, text='Покупайте бутерброды быстрее, чем за 2 минуты')


@then("user swipes on-boarding")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    texts = [
        'Регистрируйтесь на концерт Элджея меньше, чем за 69 секунд',
        'Печатайте постеры с Тимати с помощью терминалов в аэропорту',
        'Следите за весом, грейте ноги'
    ]
    for text in texts:
        do_swipe_jesture(context)
        sleep(2)
        element = set_bundle_to_locator(ONBOARD_TITLE, context.bundle)
        assert_element_found(context, element, text=text)


@then("user sees finish button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    element = set_bundle_to_locator(BEGIN_BUTTON, context.bundle)
    assert_element_found(context, element).click()
