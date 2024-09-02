from selenium.webdriver.common.by import By

class HomePageLocators(object):
    MEN = (By.ID, 'ui-id-5')
    MENS_TOPS = (By.ID, 'ui-id-17')
    MENS_HOODIES = (By.ID, 'ui-id-20')

class ProductsPageLocators(object):
    PAGE_TITLE = (By.ID, 'page-title-heading')
    ITEMS_PER_PAGE = (By.ID, 'toolbar-amount')
    PRODUCT_ITEM = (By.CLASS_NAME, 'item.product.product-item')
    PRODUCT_NAME = (By.CLASS_NAME, 'product.name.product-item-name')

class ProductPageLocators(object):
    SIZES = (By.CLASS_NAME, 'swatch-option.text')
    COLORS = (By.CLASS_NAME, 'swatch-option.color')
    QUANTITY_FILLED = (By.ID, 'qty')
    ADD_TO_CART = (By.ID, 'product-addtocart-button')
    CART_COUNT = (By.CLASS_NAME, 'counter-number')