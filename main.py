import pytest
from time import sleep
from page import UITestsDriver, MainPage


class TestUM:


    def test_find_elements(self):
        main_page = MainPage()
        sleep(6)
        main_page.click_onboarding()
        main_page.swipe_onboarding()
