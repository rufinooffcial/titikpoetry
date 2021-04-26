from django.test import TestCase
from Emergency.models import Item



	
class HomePageTest(TestCase):

	def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'mainpage.html')

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)

	def test_save_POST_request(self):
		response = self.client.post('/',data={'Newmember':'New entry'})	
		'''self.assertIn('New entry',response.content.decode())
		self.assertTemplateUsed(response,'mainpage.html')'''

		self.assertEqual(Item.objects.count(),1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'New entry')

	def test_redirects_POST(self):
		response = self.client.post('/',data={'Newmember':'New entry'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_template_displays_list(self):
		Item.objects.create(text='List item 1')
		Item.objects.create(text='List item 2')
		response = self.client.get('/')
		self.assertIn('List item 1', response.content.decode())
		self.assertIn('List item 2', response.content.decode())
		
class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
		txtItem1 = Item()
		txtItem1.text = 'Item one'
		txtItem1.save()
		txtItem2 = Item()
		txtItem2.text = 'Item two'
		txtItem2.save()
		savedItems = Item.objects.all()
		self.assertEqual(savedItems.count(), 2)
		savedItem1 = savedItems[0]
		savedItem2 = savedItems[1]
		self.assertEqual(savedItem1.text, 'Item one')
		self.assertEqual(savedItem2.text, 'Item two')

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