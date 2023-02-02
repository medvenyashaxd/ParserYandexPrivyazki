from selenium.webdriver.common.by import By


class LocatorsYandexSearchCatalog:
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[class="___Input___E6cRF __name___YfK9N __type___U_XjK __use--empty___ChJLN __use--clearable___vFgII __use--align___mxVE9 __use--align_left___kgkCe"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'span[data-e2e="offer-name"]')
    CARD_MARKET = (By.CSS_SELECTOR, 'span[class="style-linkWrapper___H264c"]')


class LocatorsAuthorization:
    FIELD_LOGIN = (By.CSS_SELECTOR, 'input[id="passp-field-login"]')
    SIGN_IN_BUTTON_1 = (By.CSS_SELECTOR, 'button[id="passp:sign-in"]')
    FIELD_PASSWD = (By.CSS_SELECTOR, 'input[id = "passp-field-passwd"]')
    SIGN_IN_BUTTON_2 = (By.CSS_SELECTOR, 'button[id="passp:sign-in"]')
