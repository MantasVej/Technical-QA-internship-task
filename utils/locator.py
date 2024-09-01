from selenium.webdriver.common.by import By

class HomePageLocators(object):
    MEN = (By.ID, 'ui-id-5')
    MENS_TOPS = (By.ID, 'ui-id-17')
    MENS_HOODIES = (By.ID, 'ui-id-20')

class ItemsPageLocators(object):
    PAGE_TITLE = (By.ID, 'page-title-heading')