import time

from behave import given, when, then, use_step_matcher, step

use_step_matcher("re")

pause = 1


@given("I am on the home page")
def step_impl(context):
    context.browser.get('http://localhost:' + str(context.port))
    time.sleep(pause)


@when("I click on the welcome link")
def step_impl(context):
    time.sleep(pause)
    context.browser.find_element_by_id('my_welcome').click()


@then("I should see the welcome page")
def step_impl(context):
    assert context.browser.title == "Scuba Portugal - Welcome"