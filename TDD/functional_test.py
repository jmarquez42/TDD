from selenium import webdriver
import unittest


class NewVisionTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="driver/chromedriver")
      #  self.browser.implicitly_wait(30)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)
       # self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
