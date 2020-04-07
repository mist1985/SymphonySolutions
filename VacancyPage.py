import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from Locators import Locators
from Base import BasePage

class VacancyPage(BasePage):

    def arrow_down(self):

        self.is_visible(Locators.ARROW_DOWN)
        self.click(Locators.ARROW_DOWN)

    # def click_macedonia(self):

    #     self.is_visible(Locators.COUNTRY_MACEDONIA)
    #     self.click(Locators.COUNTRY_MACEDONIA)

    def ads_present(self):
        self.is_visible(Locators.BOX_VACANCIES)