from django.test import TestCase



	
class HomePageTest(TestCase):

	def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'mainpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', data={'Newmember': 'New entry'})	
		self.assertIn('New entry', response.content.decode())
		self.assertTemplateUsed(response,'mainpage.html')


	'''
		from django.urls import resolve
		from django.http import HttpRequest 
		from django.template.loader import render_to_string


		def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		string_html = render_to_string('mainpage.html')
		self.assertEqual(html, string_html)
		self.assertTemplateUsed(response, 'mainpage.html')

		def test_root_url_resolves_to_mainpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, MainPage)
		def test_mainpage_returns_correct_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('utf8')
		string_html = render_to_string('mainpage.html')
		self.assertEqual(html, string_html)'''

	'''def test_mainpage_returns_correct_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.strip().startswitch('<html>'))
		self.assertIn('<title>Book Now in PPPC</title>', html)
		self.assertTrue(html.endswith('</html>'))'''