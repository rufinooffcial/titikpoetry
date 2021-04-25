from selenium import webdriver 
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTesting(unittest.TestCase):


	def setUp(self):
		self.browser = webdriver.Firefox()
	

	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Titik Poetry Inc.', self.browser.title)


		hText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Audition Form', hText)

		
		paragraph = self.browser.find_element_by_tag_name('p').text
		self.assertIn('Personal Info', paragraph)
		
		
		label = self.browser.find_element_by_id('name1').text
		self.assertIn('Name:', label)
		Name = self.browser.find_element_by_name('name').send_keys("Rufino Araza Dela Cruz")
		time.sleep(.5)
		label1 = self.browser.find_element_by_id('date').text
		self.assertIn('Birthday', label1)
		Location = self.browser.find_element_by_name('bday').send_keys("Nov 11, 1998")
		time.sleep(.5)
		label2 = self.browser.find_element_by_id('mail').text
		self.assertIn('Email', label2)
		lastname = self.browser.find_element_by_name('email').send_keys("rufino.delacruz@gsfe.com")
		time.sleep(.5)
		label3 = self.browser.find_element_by_id('sample').text
		self.assertIn('Sample of your Piece', label3)
		lastname = self.browser.find_element_by_name('sample').send_keys("akoy isang makata")
		time.sleep(2.5)
		submitbutton = self.browser.find_element_by_id('clear').click()



		


if __name__ == '__main__':
	unittest.main()