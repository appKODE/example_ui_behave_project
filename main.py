import os
from os.path import isfile, join, abspath, dirname, getmtime
from time import sleep

import pytest

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: abspath(
    join(dirname(__file__), p)
)

def get_recent_file(mypath):
    files_tuple = [(f, int(getmtime(join(mypath,f)))) for f in os.listdir(mypath) if isfile(join(mypath, f))]
    sort_by_update = sorted(files_tuple, key=lambda file: file[1])
    return sort_by_update[-1][0]

class UITestsDriver:
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH('/home/kode/android-ut-builds/Utair-4.14.344.dev.int-vc50-18062018.apk')
        self.driver = webdriver.Remote('http://192.168.100.95:4723/wd/hub', desired_caps)
        print(get_recent_file('/home/kode/android-ut-builds/'))


class TestUM:
    def setup_class(self):
        self.uidriver = UITestsDriver()

    def teardown_class(self):
        self.uidriver.driver.quit()

    def test_find_elements(self):
        sleep(5)
        el = self.uidriver.driver.find_element_by_id('com.appkode.utair.dev:id/onboardingPageImage')
