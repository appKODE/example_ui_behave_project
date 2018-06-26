import pytest
import os
from os.path import isfile, join, abspath, dirname, getmtime
from appium import webdriver
from time import sleep
from page import MainPage

# Returns abs path relative to this file and not cwd
PATH = lambda p: abspath(
    join(dirname(__file__), p)
)


def get_recent_file(mypath):
    files_tuple = [(f, int(getmtime(join(mypath, f)))) for f in os.listdir(mypath) if isfile(join(mypath, f))]
    sort_by_update = sorted(files_tuple, key=lambda file: file[1])
    return sort_by_update[-1][0]


def get_bundle(filename):
    if 'dev' in filename:
        return 'com.appkode.utair.dev'
    elif 'alpha' in filename:
        return 'com.appkode.utair.alpha'
    else:
        return 'ru.utair.android'


class TestUM:
    def setup_class(self):
        recent_file = get_recent_file('/qa-builds')
        full_path = '/home/kode/android-ut-builds/{}'.format(recent_file)
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'Android Emulator',
            'app': PATH(full_path)
        }
        self.bundle = get_bundle(recent_file)
        self.driver = webdriver.Remote('http://192.168.100.95:4723/wd/hub', desired_caps)

    def teardown_class(self):
        self.driver.quit()

    def test_find_elements(self):
        main_page = MainPage(self.driver, self.bundle)
        sleep(6)
        main_page.click_onboarding()
        main_page.swipe_onboarding()
