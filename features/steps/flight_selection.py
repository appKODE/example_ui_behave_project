from behave import *
from selenium.webdriver.support import expected_conditions as EC
from features.helpers.utils import assert_elements_found, \
    set_bundle_to_locator, click_result, do_scroll_jesture, \
    assert_element_found
from features.helpers.locators import *
use_step_matcher("re")


@given("the screen is on")
def step_impl(context):

    assert context.driver
    assert context.bundle


@then("assure header is on the screen")
def step_impl(context):

    element = set_bundle_to_locator(HEADER, context.bundle)
    assert_element_found(context, element)


@then("assure date carousel is on the screen")
def step_impl(context):

    element = set_bundle_to_locator(DATE_CAROUSEL, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(DAY_NAME, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(DAY_NUMBER, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(DATE_CAROUSEL_MIN_PRICE, context.bundle)
    assert_element_found(context, element)


@then("choose filter by price, by date")
def step_impl(context):

    element = set_bundle_to_locator(BY_FLIGHT_PRICE, context.bundle)
    click_result(context, element)

    element = set_bundle_to_locator(BY_FLIGHT_TIME, context.bundle)
    click_result(context, element)


@then("find direct flight")
def step_impl(context):

    element = set_bundle_to_locator(DIRECT_FLIGHT_CARD, context.bundle)
    assert_element_found(context, element)


@then("assure direct flight elements are present")
def step_impl(context):

    element = set_bundle_to_locator(FLIGHT_INTERVAL, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(BY_FLIGHT_PRICE, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(FLIGHT_AIRPORTS, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(DURATION, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(VEHICLE, context.bundle)
    assert_element_found(context, element)


@then("find the layover flight")
def step_impl(context):

    element = set_bundle_to_locator(STOP_OVER_FOOTER, context.bundle)
    while(not EC.presence_of_element_located(element)):
        do_scroll_jesture(context, 'down')


@then("assure layover flight elements are present")
def step_impl(context):
    pass


@then("hit layover flight footer")
def step_impl(context):

    pass


@then("assure footers elements are present")
def step_impl(context):

    pass


@then("choose certain flight")
def step_impl(context):

    pass