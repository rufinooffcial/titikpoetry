from selenium import webdriver 
import unittest

from selenium.webdriver.common.keys import Keys
import time

class PageTesting(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
	
	def check_rows_in_listtable(self, row_text):
		table = self.browser.find_element_by_id('Table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Titik Poetry Inc.', self.browser.title)
		hText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Audition Form', hText)
		inputName = self.browser.find_element_by_id('Newmember')
		inputContact = self.browser.find_element_by_id('contact')
		btnConfirm = self.browser.find_element_by_id('btnConfirm')

		inName = self.browser.find_element_by_id('Newmember')
		inName.click()
		time.sleep(1)
		inName.send_keys('Rufino Delacruz')
		time.sleep(1)
		inContact = self.browser.find_element_by_id('contact')
		inContact.click()
		time.sleep(1)
		inContact.send_keys('Rufino.delacruz@gsfe.tupcavite.edu.ph')
		time.sleep(1)
		inSex = self.browser.find_element_by_id('Sex')
		time.sleep(1)
		inSex.click()
		inSex.send_keys('Male')
		inTitle = self.browser.find_element_by_id('Title')
		inTitle.click()
		time.sleep(1)
		inTitle.send_keys('TDD ang sagot')
		inputLink = self.browser.find_element_by_id('Link')
		time.sleep(1)
		inputLink.click()
		inputLink.send_keys('https://www.youtube.com/watch?v=50wBHY16Cg0')
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		time.sleep(2)
		self.check_rows_in_listtable('1: Rufino Delacruz')

		inName1 = self.browser.find_element_by_id('Newmember')
		time.sleep(1)
		inName1.click()
		inName1.send_keys('Lawrence')
		inContact1 = self.browser.find_element_by_id('contact')
		time.sleep(1)
		inContact1.click()
		inContact1.send_keys('Lawrence@gsfe.tupcavite.edu.ph')
		inSex1 = self.browser.find_element_by_id('Sex')
		time.sleep(1)
		inSex1.click()
		inSex1.send_keys('Male')
		time.sleep(1)
		inTitle1 = self.browser.find_element_by_id('Title')
		time.sleep(1)
		inTitle1.click()
		inTitle1.send_keys('MagTDD na')
		inputLink = self.browser.find_element_by_id('Link')
		time.sleep(1)
		inputLink.click()
		inputLink.send_keys('https://www.youtube.com/watch?v=0wdkvw-TaQQ')
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		time.sleep(1)
		btnConfirm.click()
		time.sleep(1)
		self.check_rows_in_listtable('2: Lawrence')


if __name__ == '__main__':
	unittest.main(warnings='ignore')