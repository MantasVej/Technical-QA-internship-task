import unittest
from tests.base_test import BaseTest
from pages.home_page import *

class TestScenarioOne(BaseTest):

    # Test to find mens Hoodies & Sweatshirts section
    def test_find_mens_hoodies(self):
        page = HomePage(self.driver)
        page.hover(HomePageLocators.MEN)
        page.wait_for_element(HomePageLocators.MENS_TOPS)
        page.hover(HomePageLocators.MENS_TOPS)
        page.wait_for_element(HomePageLocators.MENS_HOODIES)
        page.find_element(HomePageLocators.MENS_HOODIES).click()
        element = page.find_element(ItemsPageLocators.PAGE_TITLE)
        self.assertEqual("Hoodies & Sweatshirts", element.text)