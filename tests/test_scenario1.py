import unittest
from tests.base_test import BaseTest
from pages.home_page import *
from pages.products_page import *
from pages.product_page import *

class TestScenarioOne(BaseTest):

    # Test to find mens Hoodies & Sweatshirts section
    def test_find_mens_hoodies(self):
        page = HomePage(self.driver)
        page.hover(HomePageLocators.MEN)
        page.wait_for_element(HomePageLocators.MENS_TOPS)
        page.hover(HomePageLocators.MENS_TOPS)
        page.wait_for_element(HomePageLocators.MENS_HOODIES)
        page.find_element(HomePageLocators.MENS_HOODIES).click()
        element = page.find_element(ProductsPageLocators.PAGE_TITLE)
        self.assertEqual("Hoodies & Sweatshirts", element.text)
    
    # Test to check that displayed items match items per page
    def test_jackets_per_page(self):
        page = ProductsPage(self.driver)
        items_per_page = page.get_items_per_page()
        displayed_items = page.get_displayed_items_count()
        self.assertEqual(items_per_page, displayed_items)

    # Test to open “Frankie Sweatshirt” page
    def test_open_frankie_sweatshirt(self):
        page = ProductsPage(self.driver)
        element = page.find_product_by_name("Frankie Sweatshirt")
        element.click()
        self.assertEqual("Frankie Sweatshirt", page.get_title())

        
    size = "M"
    color = "Green"
    quantity = 2

    # Test to select size, colour and quantity
    def test_select_size_colour_quantity(self):
        page = ProductPage(self.driver)
        page.select_size(self.size)
        page.select_color(self.color)
        page.select_quantity(self.quantity)
    
    # Test to add item to cart and if cart icon is updated
    def test_add_to_cart(self):
        page = ProductPage(self.driver)
        page.add_to_cart()
        self.assertEqual(page.cart_count(), self.quantity)