from selenium import webdriver 
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTesting(unittest.TestCase):


	def setUp(self):
		self.browser = webdriver.Firefox()
	

	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Titik Poetry Inc.', self.browser.title)
		hText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Audition Form', hText)
		inputName1 = self.browser.find_element_by_id('Newmember')
		inputContact1 = self.browser.find_element_by_id('contact')
		inputSex1 = self.browser.find_element_by_id('Sex')
		inputTitle1 = self.browser.find_element_by_id('Title')
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		time.sleep(.5)
		inputName1.send_keys('Rufino delacruz')
		time.sleep(.5)
		inputContact1.send_keys('Rufino.delacruz@gsfe.tupcavite.edu.ph')
		time.sleep(.5)
		inputSex1.send_keys('Male')
		time.sleep(.5)
		inputTitle1.send_keys('Makata hibang')
		time.sleep(2)
		btnConfirm.click()
		time.sleep (1)
		table = self.browser.find_element_by_id('Table')
		rows = table.find_element_by_tag_name('tr')
		self.assertIn('1: Rufino delacruz in Rufino.delacruz@gsfe.tupcavite.edu.ph',[row.text for row in rows])


if __name__ == '__main__':
	unittest.main(warnings='ignore')
