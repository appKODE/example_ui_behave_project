import os
from os.path import isfile, join, abspath, dirname, getmtime
from appium import webdriver
from locators import MainPageLocators


# Returns abs path relative to this file and not cwd
PATH = lambda p: abspath(
    join(dirname(__file__), p)
)

def get_recent_file(mypath):
    files_tuple = [(f, int(getmtime(join(mypath, f)))) for f in os.listdir(mypath) if isfile(join(mypath, f))]
    sort_by_update = sorted(files_tuple, key=lambda file: file[1])
    return sort_by_update[-1][0]


class UITestsDriver:
    def __init__(self):
        recent_file = get_recent_file('/qa-builds')
        full_path = '/home/kode/android-ut-builds/{}'.format(recent_file)
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'Android Emulator',
            'app': PATH(full_path)
            }
        self.driver = webdriver.Remote('http://192.168.100.95:4723/wd/hub', desired_caps)


class MainPage(UITestsDriver):
    """Home page action methods come here."""

    def click_onboarding(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.ONBOARDING_PAGE)
        element.click()

    def swipe_onboarding(self):
        size = self.driver.get_window_size()
        startx, starty = int(size['width']) * 0.8, int(size['height']) * 0.5
        endx, endy = int(size['width']) * 0.2, int(size['height']) * 0.5
        self.driver.swipe(startx, starty, endx, endy, 4000)

class CheckinPage(UITestsDriver):
    """Search results page action methods come here"""
    pass
