import unittest
from selenium import webdriver

class YandexTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://yandex.ru')
        self.assertIn('Яндекс', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)