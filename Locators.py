from selenium import webdriver

from selenium.webdriver.common.by import By

class Locators:

    #Page locator

    # -- Vacancy Button Locator --
    VACANCY_BUTTON = (By.LINK_TEXT, "Vacancies")

    # -- ARROW --

    ARROW_DOWN = (By.CLASS_NAME,"select2-selection__arrow")

    # -- Choose country locator --
    CHOOSE_COUNTRY = (By.ID, "select2-country-container")

    # -- Macedonia locator --
    COUNTRY_MACEDONIA = (By.XPATH, "select2-country-result-qick-skopje-macedonia")


    # -- Blocks for open vacancies --

    BOX_VACANCIES = (By.CLASS_NAME, "sy-block-box-inner")

