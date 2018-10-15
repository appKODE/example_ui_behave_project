from behave import *
from selenium.webdriver.common.by import By
use_step_matcher("re")


@then("user sees finish button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    start = context.driver.find_element(By.ID, '{}:id/onboardingPageImage')
    try:
        assert start.is_displayed() is True
    except AssertionError as error:
        error.args += ('Activity didn`t start',)
        raise


@given("activity started normally")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.driver
    on_board = context.driver.find_element(By.ID, '%s:id/onboardingPageImage' % context.bundle)
    try:
        assert on_board.is_displayed() is True
    except AssertionError as error:
        error.args += ('Onboarding not displayed',)
        raise


@then("user swipes on-boarding")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass