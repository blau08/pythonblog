import unittest
from selenium import webdriver
import selenium.webdriver.chrome.webdriver
from selenium.webdriver import Chrome as Browser
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_start_a_new_blog(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('Python Blog', self.browser.title)

        new_post_button = self.browser.find_element_by_id('new_post_button')
        self.assertIn('New Post', new_post_button.text)
        new_post_button.send_keys(Keys.ENTER)
        input_box = self.browser.find_element_by_id('input_box')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Title')



if __name__ == '__main__':
    unittest.main()
