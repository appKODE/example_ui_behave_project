from selenium.webdriver.common.by import By


# группа локаторов онбординга
ONBOARD_TITLE = (By.ID, '%s:id/onboardingPageTitle')
BEGIN_BUTTON = (By.ID, '%s:id/beginButton')

# группа локаторов экрана после онбординга
PROFILE = (By.ID, '%s:id/profile')
SETTINGS = (By.ID, '%s:id/settings')
NOTIFICATIONS = (By.ID, '%s:id/notifications')
TABBAR = (By.CLASS_NAME, 'android.widget.TextView')
