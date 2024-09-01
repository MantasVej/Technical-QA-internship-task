import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://magento.softwaretestingboard.com")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()