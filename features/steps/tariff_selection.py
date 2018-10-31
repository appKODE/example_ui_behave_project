from behave import *
from features.helpers.utils import assert_elements_found, \
    set_bundle_to_locator, assert_element_found
from features.helpers.locators import *

use_step_matcher("re")


@then("assure tariff list elements are ok")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    element = set_bundle_to_locator(TARIFF_TOOLBAR, context.bundle)
    assert_element_found(context, element)

    elements = TARIFF_STEP
    assert_elements_found(context, elements, text='Шаг 2 из 7. Выберите тариф «Туда»')

    elements = set_bundle_to_locator(TARIFF_BACKGROUND, context.bundle)
    assert_elements_found(context, elements)

    element = set_bundle_to_locator(TARIFF_TITLE, context.bundle)
    context.tariff = assert_element_found(context, element, text='Лайт')

    element = set_bundle_to_locator(TOTAL_PRICE_DESC, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(TOTAL_PRICE_VIEW, context.bundle)
    assert_element_found(context, element)


@then("click tariffs options")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    elements = set_bundle_to_locator(TARIFF_TITLE, context.bundle)
    assert_elements_found(context, elements)

    elements = set_bundle_to_locator(TARIFF_PRICE, context.bundle)
    assert_elements_found(context, elements)

    elements = set_bundle_to_locator(TARIFF_SUBTITLE, context.bundle)
    assert_elements_found(context, elements)


@then("assure tariffs options ok")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.tariff.click()

    elements = set_bundle_to_locator(TARIFF_SERVICE_TITLE, context.bundle)
    assert_elements_found(context, elements)

    elements = set_bundle_to_locator(TARIFF_SERVICE_VALUE, context.bundle)
    context.tariff = assert_elements_found(context, elements)


@then("assure tariffs sum and common sum are equal")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("assure tariff back list elements are ok")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    element = set_bundle_to_locator(TARIFF_TOOLBAR, context.bundle)
    assert_element_found(context, element)

    elements = TARIFF_STEP
    assert_elements_found(context, elements, text='Шаг 4 из 7. Выберите тариф «Обратно»')

    elements = set_bundle_to_locator(TARIFF_BACKGROUND, context.bundle)
    assert_elements_found(context, elements)

    elements = set_bundle_to_locator(TARIFF_TITLE, context.bundle)
    assert_elements_found(context, elements, text='Стандарт').click()

    element = TARIFF_DISABLE
    assert_element_found(context, element)

    context.tariff.click()

    element = set_bundle_to_locator(TOTAL_PRICE_DESC, context.bundle)
    assert_element_found(context, element)

    element = set_bundle_to_locator(TOTAL_PRICE_VIEW, context.bundle)
    assert_element_found(context, element)