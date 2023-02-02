import time

from base import BaseCommands
from locators import LocatorsYandexSearchCatalog
from executor import Executor


class TestStart():
    def test_start(self, driver):
        main_url = 'https://partner.market.yandex.ru/business/1030699/assortment?campaignId=22031686&activeTab=mappings&mappingChangePeriod=all&mappingChecking=processed'
        main_page = Executor(driver, url=main_url)
        main_page.open()
        main_page.executor()



