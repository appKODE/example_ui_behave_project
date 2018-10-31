from behave import *
from features.helpers.utils import assert_elements_found, \
    set_bundle_to_locator, date_picker, assert_element_found
from features.helpers.locators import *
use_step_matcher("re")


@given("the screen is open")
def step_impl(context):

    assert context.driver
    assert context.bundle


@then("user closes profile sign")
def step_impl(context):

    element = set_bundle_to_locator(PROFILE, context.bundle)
    assert_element_found(context, element).click()


@then("user chooses booking tab")
def step_impl(context):
    if context.driver.capabilities.get('desired').get('platformVersion') == '7.0':
        text = 'ПОКУПКА'
    else:
        text = 'Покупка'

    element = TABBAR
    assert_elements_found(context, element, text=text).click()


@then("user chooses date of flight to")
def step_impl(context):

    element = set_bundle_to_locator(DATE_TO, context.bundle)
    assert_element_found(context, element).click()

    element = set_bundle_to_locator(NEXT_MONTH, context.bundle)
    assert_element_found(context, element).click()

    element = DATE_CHOICE
    date_picker(context, element)


@then("user chooses date of flight back")
def step_impl(context):

    element = set_bundle_to_locator(DATE_BACK_EMPTY, context.bundle)
    assert_element_found(context, element).click()

    element = set_bundle_to_locator(NEXT_MONTH, context.bundle)
    assert_element_found(context, element).click()

    element = DATE_CHOICE
    date_picker(context, element)


@then("user chooses city from")
def step_impl(context):

    element = set_bundle_to_locator(FROM, context.bundle)
    assert_element_found(context, element).click()

    element = set_bundle_to_locator(CITY, context.bundle)
    assert_elements_found(context, element, text="Москва").click()


@then("user chooses city to")
def step_impl(context):

    element = set_bundle_to_locator(TO, context.bundle)
    assert_element_found(context, element).click()

    element = set_bundle_to_locator(CITY, context.bundle)
    assert_elements_found(context, element, text="Сургут").click()


@then("user chooses passengers")
def step_impl(context):

    element = set_bundle_to_locator(PLUS_ADULT, context.bundle)
    assert_element_found(context, element).click()

    element = set_bundle_to_locator(MINUS_ADULT, context.bundle)
    assert_element_found(context, element).click()

    element = set_bundle_to_locator(PLUS_CHILD, context.bundle)
    assert_element_found(context, element).click()

    element = set_bundle_to_locator(MINUS_CHILD, context.bundle)
    assert_element_found(context, element).click()

    element = set_bundle_to_locator(PLUS_INFANT, context.bundle)
    assert_element_found(context, element).click()

    element = set_bundle_to_locator(PLUS_INFANT, context.bundle)
    assert_element_found(context, element).click()

    element = set_bundle_to_locator(MINUS_INFANT, context.bundle)
    assert_element_found(context, element).click()


@then("user clicks Next")
def step_impl(context):

    element = set_bundle_to_locator(SEARCH_BUTTON, context.bundle)
    assert_element_found(context, element).click()
