from selenium import webdriver 
#import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

cWait = 3
class Testingan(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
	
	def wait_rows_in_listtable(self, row_text):                                   
		start_time = time.time()
		while time.time()-start_time<cWait:
			time.sleep(0.1)
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

	def testingan_sa_simula_list_one_user(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Titik Poetry Inc.', self.browser.title)
		UloText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Audition Form', UloText)

		Pangalanmo = self.browser.find_element_by_id('Newmember')
		Pangalanmo.click()
		Pangalanmo.send_keys('Rufino Delacruz')
		time.sleep(.1)
		Koneksyon = self.browser.find_element_by_id('contact')
		Koneksyon.click()
		Koneksyon.send_keys('Rufino.delacruz@gsfe.tupcavite.edu.ph')
		time.sleep(.1)
		Kasarian = self.browser.find_element_by_id('Sex')
		Kasarian.click()
		Kasarian.send_keys('Male')
		time.sleep(.1)
		Pamagat = self.browser.find_element_by_id('Title')
		Pamagat.click()
		Pamagat.send_keys('TDD ang sagot')
		time.sleep(.1)
		Link = self.browser.find_element_by_id('Link')
		Link.click()
		Link.send_keys('https://www.youtube.com/watch?v=50wBHY16Cg0')
		time.sleep(.1)
		inConfirm = self.browser.find_element_by_id('inConfirm')
		inConfirm.click()
		self.wait_rows_in_listtable('1: Rufino Delacruz')

		time.sleep(.1)
		Pangalanmo = self.browser.find_element_by_id('Newmember')
		Pangalanmo.click()
		Pangalanmo.send_keys('Lawrence')
		time.sleep(.1)
		Koneksyon = self.browser.find_element_by_id('contact')
		Koneksyon.click()
		Koneksyon.send_keys('Lawrence@gsfe.tupcavite.edu.ph')
		time.sleep(.1)
		Kasarian = self.browser.find_element_by_id('Sex')
		Kasarian.click()
		Kasarian.send_keys('Male')
		time.sleep(.1)
		Pamagat = self.browser.find_element_by_id('Title')
		Pamagat.click()
		Pamagat.send_keys('MagTDD na')
		time.sleep(.1)
		Link = self.browser.find_element_by_id('Link')
		Link.click()
		Link.send_keys('https://www.youtube.com/watch?v=0wdkvw-TaQQ')
		time.sleep(.1)
		inConfirm = self.browser.find_element_by_id('inConfirm')
		inConfirm.click()
		self.wait_rows_in_listtable('2: Lawrence')

	def testingan_other_users_different_urls(self):
		self.browser.get(self.live_server_url)
		time.sleep(.1)
		Pangalanmo = self.browser.find_element_by_id('Newmember')
		Pangalanmo.click()
		Pangalanmo.send_keys('Lovely Joy')
		time.sleep(.1)
		Koneksyon = self.browser.find_element_by_id('contact')
		Koneksyon.click()
		Koneksyon.send_keys('Lovely.joy@gsfe.tupcavite.edu.ph')
		time.sleep(.1)
		Kasarian = self.browser.find_element_by_id('Sex')
		Kasarian.click()
		Kasarian.send_keys('Female')
		time.sleep(.1)
		Pamagat = self.browser.find_element_by_id('Title')
		Pamagat.click()
		Pamagat.send_keys('Silakbo')
		time.sleep(.1)
		Link = self.browser.find_element_by_id('Link')
		Link.click()
		Link.send_keys('youtube.com')
		time.sleep(.1)
		inConfirm = self.browser.find_element_by_id('inConfirm')
		inConfirm.click()
		self.wait_rows_in_listtable('1: Lovely Joy')
		kitalistahan_url = self.browser.current_url
		self.assertRegex(kitalistahan_url, '/TitikPoetryApp/.+')

		self.browser.quit()
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)
		pahinakatawan = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Lovely Joy', pahinakatawan)
		time.sleep(.1)
		Pangalanmo = self.browser.find_element_by_id('Newmember')
		Pangalanmo.click()
		Pangalanmo.send_keys('Eljohn Torres')
		time.sleep(.1)
		Koneksyon = self.browser.find_element_by_id('contact')
		Koneksyon.click()
		Koneksyon.send_keys('Eljohn.torres@gsfe.tupcavite.edu.ph')
		time.sleep(.1)
		Kasarian = self.browser.find_element_by_id('Sex')
		Kasarian.click()
		Kasarian.send_keys('Male')
		time.sleep(.1)
		Pamagat = self.browser.find_element_by_id('Title')
		Pamagat.click()
		Pamagat.send_keys('Itatali kita')
		time.sleep(.1)
		Link = self.browser.find_element_by_id('Link')
		Link.click()
		Link.send_keys('youtube.com/Eljohn')
		time.sleep(.1)
		inConfirm = self.browser.find_element_by_id('inConfirm')
		inConfirm.click()
		self.wait_rows_in_listtable('1: Eljohn Torres')
		gagamit_url = self.browser.current_url
		self.assertRegex(gagamit_url, 'TitikPoetryApp/.+')
		self.assertNotEqual(kitalistahan_url, gagamit_url)
		pahinakatawan = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Lovely Joy', pahinakatawan)
		self.assertIn('Eljohn Torres', pahinakatawan)





