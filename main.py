import os
from time import sleep

import pytest

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class UITestsDriver:
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH('/home/kode/android-ut-builds/Utair*.apk')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


class TestUM:
    def setUp(self):
        self.uidriver = UITestsDriver()

    def tearDown(self):
        self.uidriver.driver.quit()

    def test_find_elements(self):
        sleep(5)
        el = self.uidriver.driver.find_element_by_id('com.appkode.utair.dev:id/onboardingPageImage')
