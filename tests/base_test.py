import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--disable-search-engine-choice-screen")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("https://magento.softwaretestingboard.com")

    @classmethod
    def tearDownClass(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()