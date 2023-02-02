import time

from base import BaseCommands
from locators import LocatorsYandexSearchCatalog


class Executor(BaseCommands):
    def executor(self, loc_main=LocatorsYandexSearchCatalog):
        try:
            self.element_is_visible(loc_main.SEARCH_FIELD).send_keys('44032DBS')

            time.sleep(4)

            product_text = self.elements_are_visible(loc_main.PRODUCT_NAME)

            get_len = len(product_text)

            for l in range(get_len):
                print(product_text[l].text)

            href = self.elements_are_visible(loc_main.CARD_MARKET)
            print(len(href))
            print(type(href))
            for l in len(href):
                print(href[l].get_attribute('href'))
            print(href)

        except Exception as ex:
            print(ex)
