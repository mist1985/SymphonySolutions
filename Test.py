import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from Base import BasePage
from HomePage import HomePage
from VacancyPage import VacancyPage


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://www.symphony-solutions.eu/")


vac_button = HomePage(driver)
vac_button.click_on_vacancy()

vacancies = VacancyPage(driver)
vacancies.cookie()
vacancies.arrow_down()
vacancies.click_macedonia()
vacancies.ads_present()

if ('QA' in driver.page_source):
    print("QA position is available")
else:
    print("QA position is not available")

driver.quit()