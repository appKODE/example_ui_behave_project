from selenium.webdriver.common.by import By


# группа локаторов онбординга
ONBOARD_TITLE = (By.ID, '%s:id/onboardingPageTitle')
BEGIN_BUTTON = (By.ID, '%s:id/beginButton')

# группа локаторов экрана после онбординга
PROFILE = (By.ID, '%s:id/profile')
SETTINGS = (By.ID, '%s:id/settings')
NOTIFICATIONS = (By.ID, '%s:id/notifications')
TABBAR = (By.CLASS_NAME, 'android.widget.TextView')

# группа локаторов экрана регистрации
BOOKID_HELP = (By.ID, '%s:id/bookingIdentifierHelp')
SURNAME_HELP = (By.ID, '%s:id/lastNameHelp')
FIND_BUTTON = (By.ID, '%s:id/findSegmentButton')

# группа локаторов на экране Покупка
FROM = (By.ID, '%s:id/departCityLayout')
TO = (By.ID, '%s:id/arriveCityLayout')
REVERSE = (By.ID, '%s:id/swapDestinations')
DATE_TO = (By.ID, '%s:id/departDate')
DATE_BACK = (By.ID, '%s:id/returnDate')
DATE_BACK_EMPTY = (By.ID, '%s:id/returnDateButton')
DATE_BACK_CANCEL = (By.ID, '%s:id/returnDateClearButton')
PLUS_ADULT = (By.ID, '%s:id/buttonIncAdults')
PLUS_CHILD = (By.ID, '%s:id/buttonIncChildren')
PLUS_INFANT = (By.ID, '%s:id/buttonIncInfants')
MINUS_ADULT = (By.ID, '%s:id/buttonDecAdults')
MINUS_CHILD = (By.ID, '%s:id/buttonDecChildren')
MINUS_INFANT = (By.ID, '%s:id/buttonDecInfants')
NEXT_MONTH = (By.ID, '%s:id/mdtp_next_month_arrow')
DATE_OK = (By.ID,'%s:id/mdtp_ok')
DATE_CANCEL = (By.ID,'%s:id/mdtp_cancel')
DATE_CHOICE = (By.CLASS_NAME, 'android.view.View')