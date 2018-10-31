from behave import *
from time import sleep
from features.helpers.utils import assert_elements_found, \
    set_bundle_to_locator, do_scroll_jesture, \
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
    assert_element_found(context, element).click()

    element = set_bundle_to_locator(BY_FLIGHT_TIME, context.bundle)
    assert_element_found(context, element).click()


@then("find direct flight")
def step_impl(context):

    element = set_bundle_to_locator(DIRECT_FLIGHT_CARD, context.bundle)
    assert_element_found(context, element)


@then("assure direct flight elements are present")
def step_impl(context):

    element = set_bundle_to_locator(ARRIVAL_TIME, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(DEPARTURE_TIME, context.bundle)
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
    for i in range(5):
        do_scroll_jesture(context, 'down')
        sleep(2)
    assert_element_found(context, element, text='Пересадка').click()


@then("assure layover flight elements are present")
def step_impl(context):

    element = set_bundle_to_locator(STOP_OVER_FOOTER_EXP, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(SEG_ARRIVAL_TIME, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(SEG_DEPARTURE_TIME, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(SEG_AIRPORTS_INFO, context.bundle)
    assert_element_found(context, element)


@then("choose certain flight")
def step_impl(context):

    element = set_bundle_to_locator(DIRECT_FLIGHT_CARD, context.bundle)
    assert_element_found(context, element).click()