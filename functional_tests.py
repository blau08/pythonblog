import unittest
from selenium import webdriver
import selenium.webdriver.chrome.webdriver
from selenium.webdriver import Chrome as Browser

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit

    def test_start_a_new_blog(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('Django', self.browser.title)

if __name__ == '__main__':
    unittest.main()
