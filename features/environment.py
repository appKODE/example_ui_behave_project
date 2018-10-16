from appium import webdriver
from features.helpers.utils import *
from features.helpers.configs import *

def before_all(context):
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', get_capabilities())
    recent_file = get_recent_file(HOME_LOCATION)
    context.bundle = get_bundle(recent_file)


def after_all(context):
    context.driver.quit()
