from selenium import webdriver 
#import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

cWait = 3
class PageTesting(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
	
	def wait_rows_in_listtable(self, row_text):
		start_time = time.time()
		while time.time()-start_time<cWait:
			time.sleep(0.2)
		try:
			table = self.browser.find_element_by_id('Table')
			rows = table.find_elements_by_tag_name('tr')
			self.assertIn(row_text, [row.text for row in rows])
			return
		except(AssertionError, WebDriverException) as e:
			if time.time()-start_time>cWait:
				raise e

		#table = self.browser.find_element_by_id('Table')
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_and_retrieve_it(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Titik Poetry Inc.', self.browser.title)
		hText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Audition Form', hText)
		inputName = self.browser.find_element_by_id('Newmember')
		inputContact = self.browser.find_element_by_id('contact')
		btnConfirm = self.browser.find_element_by_id('btnConfirm')

		inName = self.browser.find_element_by_id('Newmember')
		inName.click()
		inName.send_keys('Rufino Delacruz')
		time.sleep(.1)
		inContact = self.browser.find_element_by_id('contact')
		inContact.click()
		inContact.send_keys('Rufino.delacruz@gsfe.tupcavite.edu.ph')
		time.sleep(.1)
		inSex = self.browser.find_element_by_id('Sex')
		inSex.click()
		inSex.send_keys('Male')
		inTitle = self.browser.find_element_by_id('Title')
		inTitle.click()
		inTitle.send_keys('TDD ang sagot')
		time.sleep(.1)
		inputLink = self.browser.find_element_by_id('Link')
		inputLink.click()
		inputLink.send_keys('https://www.youtube.com/watch?v=50wBHY16Cg0')
		time.sleep(.1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		self.wait_rows_in_listtable('1: Rufino Delacruz')

		time.sleep(.1)
		inName1 = self.browser.find_element_by_id('Newmember')
		inName1.click()
		inName1.send_keys('Lawrence')
		time.sleep(.1)
		inContact1 = self.browser.find_element_by_id('contact')
		inContact1.click()
		inContact1.send_keys('Lawrence@gsfe.tupcavite.edu.ph')
		time.sleep(.1)
		inSex1 = self.browser.find_element_by_id('Sex')
		inSex1.click()
		inSex1.send_keys('Male')
		time.sleep(.1)
		inTitle1 = self.browser.find_element_by_id('Title')
		inTitle1.click()
		inTitle1.send_keys('MagTDD na')
		time.sleep(.1)
		inputLink = self.browser.find_element_by_id('Link')
		inputLink.click()
		inputLink.send_keys('https://www.youtube.com/watch?v=0wdkvw-TaQQ')
		time.sleep(.1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		self.wait_rows_in_listtable('2: Lawrence')


#if __name__ == '__main__':
	#unittest.main(warnings='ignore')