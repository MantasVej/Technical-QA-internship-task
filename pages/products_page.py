from pages.base_page import BasePage
from utils.locator import *

class ProductsPage(BasePage):
    
    def get_items_per_page(self):
        elements = self.find_element(ProductsPageLocators.ITEMS_PER_PAGE).text.split()
        items_range = elements[1]
        end_range = int(items_range.split('-')[1])
        return int(end_range)
    
    def get_displayed_items_count(self):
        items = self.find_elements(ProductsPageLocators.PRODUCT_ITEM)
        return len(items)
    
    def find_product_by_name(self, product_name):
        items = self.find_elements(ProductsPageLocators.PRODUCT_NAME)
        for item in items:
            if item.text == product_name:
                return item
        return None
        