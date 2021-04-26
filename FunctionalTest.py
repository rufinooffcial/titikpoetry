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
		inputName = self.browser.find_element_by_id('Newmember')
		inputContact = self.browser.find_element_by_id('contact')
		inputSex = self.browser.find_element_by_id('Sex')
		inputTitle = self.browser.find_element_by_id('Title')
		btnConfirm = self.browser.find_element_by_id('btnConfirm')

		inName = self.browser.find_element_by_id('Newmember')
		time.sleep(1)
		inName.click()
		time.sleep(1)
		inName.send_keys('Rufino Delacruz')
		inContact = self.browser.find_element_by_id('contact')
		time.sleep(1)
		inContact.click()
		time.sleep(1)
		inContact.send_keys('Rufino.delacruz@gsfe.tupcavite.edu.ph')
		inSex = self.browser.find_element_by_id('Sex')
		inSex.click()
		time.sleep(1)
		inSex.send_keys('Male')
		time.sleep(1)
		inTitle = self.browser.find_element_by_id('Title')
		time.sleep(1)
		inTitle.click()
		time.sleep(1)
		inTitle.send_keys('Ang makatang hibang')
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		time.sleep(1)
		btnConfirm.click()
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		time.sleep(1)

		inName = self.browser.find_element_by_id('Newmember')
		time.sleep(1)
		inName.click()
		time.sleep(1)
		inName.send_keys('Lawrence')
		inContact = self.browser.find_element_by_id('contact')
		time.sleep(1)
		inContact.click()
		time.sleep(1)
		inContact.send_keys('Lawrence@gsfe.tupcavite.edu.ph')
		inSex = self.browser.find_element_by_id('Sex')
		inSex.click()
		time.sleep(1)
		inSex.send_keys('Male')
		time.sleep(1)
		inTitle = self.browser.find_element_by_id('Title')
		time.sleep(1)
		inTitle.click()
		time.sleep(1)
		inTitle.send_keys('Ang makatang haba')
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		time.sleep(1)
		btnConfirm.click()
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		time.sleep(1)
		table = self.browser.find_element_by_id('Table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Rufino Delacruz in Rufino.delacruz@gsfe.tupcavite.edu.ph', [row.text for row in rows])
		self.assertIn('2: Lawrence in Lawrence@gsfe.tupcavite.edu.ph', [row.text for row in rows])


if __name__ == '__main__':
	unittest.main(warnings='ignore')