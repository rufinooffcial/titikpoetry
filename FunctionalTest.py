from selenium import webdriver 
import unittest

class Pagetesting(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	#def tearDown(self):
		#self.browser.quit()

	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Call an Emergency', self.browser.title)
		#self.fail('Finish the test NOW')


if __name__ == '__main__':
	unittest.main()
