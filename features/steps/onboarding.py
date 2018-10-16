from behave import *
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
        element = set_bundle_to_locator(ONBOARD_TITLE, context.bundle)
        assert_element_found(context, element, text=text)


@then("user sees finish button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    element = set_bundle_to_locator(BEGIN_BUTTON, context.bundle)
    result = assert_element_found(context, element)
    result.click()
