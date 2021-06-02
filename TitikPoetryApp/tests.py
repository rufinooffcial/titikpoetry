from django.test import TestCase
from TitikPoetryApp.models import Item, Recruit
	
class Tahanantestingan(TestCase):
	def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'Titikpoetry.html')
		
class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
		newRecruit = Recruit()
		newRecruit.save()
		txtItem1 = Item()
		txtItem1.text = 'Item one'
		txtItem1.RecId = newRecruit
		txtItem1.save()
		txtItem2 = Item()
		txtItem2.RecId = newRecruit
		txtItem2.text = 'Item two'
		txtItem2.save()
		savedItems = Item.objects.all()
		savedRecruit = Recruit.objects.first()
		self.assertEqual(savedItems.count(), 2)
		self.assertEqual(savedRecruit,newRecruit)
		savedItem1 = savedItems[0]
		savedItem2 = savedItems[1]
		self.assertEqual(savedItem1.text, 'Item one')
		self.assertEqual(savedItem2.text, 'Item two')
		self.assertEqual(savedItem1.RecId, newRecruit)
		self.assertEqual(savedItem2.RecId, newRecruit)			

class ViewTest(TestCase):
	def test_displays_each_recruit(self):
		newRecruit = Recruit.objects.create()
		Item.objects.create(RecId=newRecruit, text='MJ')
		Item.objects.create(RecId=newRecruit, text='LJ')
		response = self.client.get(f'/TitikPoetryApp/{newRecruit.id}/')
		self.assertContains(response, 'MJ')
		self.assertContains(response, 'LJ')
		self.assertNotContains(response, 'Jay Em')
		self.assertNotContains(response, 'Em Jay')
		
		newRecruit_2 = Recruit.objects.create()
		Item.objects.create(RecId=newRecruit_2, text='Jay Em')
		Item.objects.create(RecId=newRecruit_2, text='Em Jay')
		response = self.client.get(f'/TitikPoetryApp/{newRecruit_2.id}/')
		self.assertContains(response, 'Jay Em')
		self.assertContains(response, 'Em Jay')

		
	def test_listview_uses_listpage(self):
		newRecruit = Recruit.objects.create()
		response = self.client.get(f'/TitikPoetryApp/{newRecruit.id}/')
		self.assertTemplateUsed(response, 'TitikTheSecond.html')

	def test_pass_list_to_template(self):
		dummyList1 = Recruit.objects.create()
		dummyList2 = Recruit.objects.create()
		pasalista = Recruit.objects.create()
		response = self.client.get(f'/TitikPoetryApp/{pasalista.id}/')
		self.assertEqual(response.context['RecId'], pasalista)

class CreateListTest(TestCase):
	def test_save_POST_request(self):
		response = self.client.post('/TitikPoetryApp/kitalistahan_url',data={'Newmember':'New entry'})	
		self.assertEqual(Item.objects.count(),1)
		Itemnew = Item.objects.first()
		self.assertEqual(Itemnew.text, 'New entry')

	def test_redirects_POST(self):
		response = self.client.post('/TitikPoetryApp/kitalistahan_url',data={'Newmember':'New entry'})
		newList = Recruit.objects.first()
		self.assertRedirects(response, f'/TitikPoetryApp/{newList.id}/')

class AddItemTest(TestCase):
	def test_add_POST_request_to_existing_list(self):
		DummyList1 = Recruit.objects.create()
		DummyList2 = Recruit.objects.create()
		kasalukuyangList = Recruit.objects.create()
		self.client.post(f'/TitikPoetryApp/{kasalukuyangList.id}/addItem',data={'Newmember': 'New item list'})
		self.assertEqual(Item.objects.count(),1)
		Itemnew = Item.objects.first()
		self.assertEqual(Itemnew.text, 'New item list')
		self.assertEqual(Itemnew.RecId, kasalukuyangList)

	def test_redirects_to_list_view(self):
	 	DummyList1 = Recruit.objects.create()
	 	DummyList2 = Recruit.objects.create()
	 	DummyList3 = Recruit.objects.create()
	 	kasalukuyangList = Recruit.objects.create()
	 	response = self.client.post(f'/TitikPoetryApp/{kasalukuyangList.id}/addItem',data={'Newmember': 'New item list'})
	 	self.assertRedirects(response, f'/TitikPoetryApp/{kasalukuyangList.id}/')		