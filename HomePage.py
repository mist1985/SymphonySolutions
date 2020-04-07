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

class HomePage (BasePage):


    def click_on_vacancy (self):
        self.is_visible(Locators.VACANCY_BUTTON)
        self.click(Locators.VACANCY_BUTTON)