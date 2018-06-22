from locators import MainPageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    """Home page action methods come here."""

    def click_onboarding(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.ONBOARDING_PAGE)
        element.click()

    def swipe_onboarding(self):
        size = self.driver.get_window_size()
        startx, starty = int(size['width']) - 10, int(size['height']) * 0.5
        endx, endy = int(size['width']) * 0.2, int(size['height']) * 0.5
        self.driver.swipe(startx, starty, endx, endy, 300)

class CheckinPage(BasePage):
    """Search results page action methods come here"""
    pass
