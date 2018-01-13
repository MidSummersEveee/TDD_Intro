from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from lists.models import Item
from django.http import HttpRequest
from lists.views import home_page

class HomePageTest(TestCase):

	# been implicitly tested by client at the bottom
	# def test_root_url_resolves_to_home_page_view(self):
	# 	found = resolve('/')
	# 	self.assertEqual(found.func, home_page)

	# def test_home_page_returns_correct_html(self):
		
		# old school version of test
		# request = HttpRequest()
		# response = home_page(request)
		# html = response.content.decode('utf8')
		# expected_html = render_to_string('home.html')
		# assertEqual(expected_html, html)


	def test_uses_home_template(self):
		# modern version applying ready to use check templates module
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')


	# def test_try(self):
	# 	response = self.client.post('/', data={'item_text': ''})
	# 	self.assertEqual(Item.objects.count(), 0)


	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'item_text': 'A new list item'})
		# check orm correction
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertIn(new_item.text, 'A new list item')

	def test_redirects_after_POST(self):
		# check for PRG
		response = self.client.post('/', data={'item_text': 'A new list item'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')


	def test_only_save_items_when_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)


	def test_displays_all_list_items(self):
		Item.objects.create(text='item 1')
		Item.objects.create(text='item 2')

		response = self.client.get('/')

		self.assertIn('item 1', response.content.decode())
		self.assertIn('item 2', response.content.decode())


class ItemModelTest(TestCase):
	
	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()

		second_item = Item()
		second_item.text = 'The second item'
		second_item.save()

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)
		
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(second_saved_item.text, 'The second item')