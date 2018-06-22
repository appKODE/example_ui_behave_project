import pytest
from time import sleep
from page import UITestsDriver, MainPage


class TestUM:


    def test_find_elements(self):
        main_page = MainPage()
        main_page.click_onboarding()
