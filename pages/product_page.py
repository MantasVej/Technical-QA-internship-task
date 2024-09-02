from pages.base_page import BasePage
from utils.locator import *

class ProductPage(BasePage):
    def select_size(self, size):
        sizes = self.find_elements(ProductPageLocators.SIZES)
        for s in sizes:
            if s.text == size:
                s.click()
                break
    
    def select_color(self, color):
        colours = self.find_elements(ProductPageLocators.COLORS)
        for c in colours:
            if c.get_attribute('option-label') == color:
                c.click()
                break
    
    def select_quantity(self, quantity):
        self.find_element(ProductPageLocators.QUANTITY_FILLED).clear()
        self.find_element(ProductPageLocators.QUANTITY_FILLED).send_keys(quantity)
    
    def add_to_cart(self):
        element = self.find_element(ProductPageLocators.ADD_TO_CART)
        element.click()

    def cart_count(self):
        return int(self.find_element(ProductPageLocators.CART_COUNT).text)