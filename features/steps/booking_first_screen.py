from behave import *
from features.helpers.utils import assert_elements_found, \
    set_bundle_to_locator, click_result, date_picker
from features.helpers.locators import *
use_step_matcher("re")


@given("the screen is open")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver
    assert context.bundle

    element = set_bundle_to_locator(PROFILE, context.bundle)
    click_result(context, element)

    element = TABBAR
    result = assert_elements_found(context, element, text='ПОКУПКА')
    result.click()


@then("user chooses date of flight")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    element = set_bundle_to_locator(DATE_TO, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(NEXT_MONTH, context.bundle)
    click_result(context, element)

    element = DATE_CHOICE
    date_picker(context, element)

    element = set_bundle_to_locator(DATE_BACK_EMPTY, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(NEXT_MONTH, context.bundle)
    click_result(context, element)

    element = DATE_CHOICE
    date_picker(context, element)


@then("user chooses cities")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    element = set_bundle_to_locator(FROM, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(CITY, context.bundle)
    click_result(context, element, text='Москва')

    element = set_bundle_to_locator(TO, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(CITY, context.bundle)
    click_result(context, element, text='Сургут')


@then("user chooses passengers")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("user clicks Next")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass