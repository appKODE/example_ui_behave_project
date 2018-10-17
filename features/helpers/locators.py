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
SEARCH_BUTTON = (By.ID, '%s:id/primaryButton')
CITY = (By.ID, '%s:id/cityName')

# группа локаторов на экране выбора Рейса Туда
HEADER = (By.ID, '%s:id/stationsView')
STEP = (By.ID, '%s:id/topProgressView')
DATE_CAROUSEL = (By.ID, '%s:id/calendarLayout')
DATE_CAROUSEL_MIN_PRICE = (By.ID, '%s:id/minPrice')
DIRECT_FLIGHT = (By.ID, '%s:id/itemHeader')
BY_FLIGHT_TIME = (By.ID, '%s:id/sortByTimeButton')
BY_FLIGHT_PRICE = (By.ID, '%s:id/sortByPriceButton')
DIRECT_FLIGHT_CARD = (By.ID, '%s:id/itemContent')
STOP_OVER_FLIGHT = (By.ID, '%s:id/itemHeader')
STOP_OVER_FLIGHT_CARD = (By.ID, '%s:id/itemContent')
STOP_OVER_FOOTER = (By.ID, '%s:id/layoverInfo')
STOP_OVER_FOOTER_EXP = (By.ID, '%s:id/layoverSegmentsContent')
DAY_NUMBER = (By.ID, '%s:id/dayNumber')
DAY_NAME = (By.ID, '%s:id/dayName')
TAXES_TEXT = (By.ID, '%s:id/itemHeaderSubtitle')
FLIGHT_INTERVAL = (By.ID, '%s:id/flightTimeInterval')
FLIGHT_PRICE = (By.ID, '%s:id/price')
FLIGHT_AIRPORTS = (By.ID, '%s:id/flightNumberAirports')
DURATION = (By.ID, '%s:id/duration')
VEHICLE = (By.ID, '%s:id/vehicle')
LAYOVER_TIME = (By.ID, '%s:id/segmentLayoverInfo')