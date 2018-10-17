from behave import *
from features.helpers.utils import assert_elements_found, \
    set_bundle_to_locator, click_result, date_picker
from features.helpers.locators import *
use_step_matcher("re")


@given("the screen is open")
def step_impl(context):

    assert context.driver
    assert context.bundle


@then("user closes profile sign")
def step_impl(context):

    element = set_bundle_to_locator(PROFILE, context.bundle)
    click_result(context, element)


@then("user chooses booking tab")
def step_impl(context):

    element = TABBAR
    result = assert_elements_found(context, element, text='ПОКУПКА')
    result.click()


@then("user chooses date of flight to")
def step_impl(context):

    element = set_bundle_to_locator(DATE_TO, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(NEXT_MONTH, context.bundle)
    click_result(context, element)

    element = DATE_CHOICE
    date_picker(context, element)


@then("user chooses date of flight back")
def step_impl(context):

    element = set_bundle_to_locator(DATE_BACK_EMPTY, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(NEXT_MONTH, context.bundle)
    click_result(context, element)

    element = DATE_CHOICE
    date_picker(context, element)


@then("user chooses city from")
def step_impl(context):

    element = set_bundle_to_locator(FROM, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(CITY, context.bundle)
    result = assert_elements_found(context, element, text="Москва")
    result.click()


@then("user chooses city to")
def step_impl(context):

    element = set_bundle_to_locator(TO, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(CITY, context.bundle)
    result = assert_elements_found(context, element, text="Сургут")
    result.click()


@then("user chooses passengers")
def step_impl(context):

    element = set_bundle_to_locator(PLUS_ADULT, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(MINUS_ADULT, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(PLUS_CHILD, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(MINUS_CHILD, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(PLUS_INFANT, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(PLUS_INFANT, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(MINUS_INFANT, context.bundle)
    click_result(context, element)


@then("user clicks Next")
def step_impl(context):

    element = set_bundle_to_locator(SEARCH_BUTTON, context.bundle)
    click_result(context, element)
