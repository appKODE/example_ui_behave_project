from behave import *

use_step_matcher("re")


@given("the screen is open")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(context.bundle)
    assert context.driver
    assert context.bundle


@then("user chooses date of flight")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("user chooses cities")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("user chooses passengers")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass