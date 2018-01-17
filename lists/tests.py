from django.template.loader import render_to_string

# for django 1.10 & 2.0
# from django.urls import resolve
# for django 1.8+
from django.core.urlresolvers import resolve

from django.test import TestCase
from lists.models import Item, List
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
	
	def test_only_save_items_when_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)


	# def test_displays_all_list_items(self):
	# 	Item.objects.create(text='item 1')
	# 	Item.objects.create(text='item 2')

	# 	response = self.client.get('/')

	# 	self.assertIn('item 1', response.content.decode())
	# 	self.assertIn('item 2', response.content.decode())


class ListAndItemModelTest(TestCase):
	
	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.list = list_
		first_item.save()

		second_item = Item()
		second_item.text = 'The second item'
		second_item.list = list_
		second_item.save()

		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)
		
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(first_saved_item.list, list_)
		self.assertEqual(second_saved_item.text, 'The second item')
		self.assertEqual(second_saved_item.list, list_)

class ListViewTest(TestCase):

	def test_list_template(self):
		list_ = List.objects.create()
		response = self.client.get(f'/lists/{list_.id}/')
		self.assertTemplateUsed(response, 'list.html')

	def test_displays_only_items_for_that_list(self):
		correct_list = List.objects.create()
		Item.objects.create(text='itemey 1', list=correct_list)
		Item.objects.create(text='itemey 2', list=correct_list)
		other_list = List.objects.create()
		Item.objects.create(text='other list item 1', list=other_list)
		Item.objects.create(text='other list item 2', list=other_list)

		response = self.client.get(f'/lists/{correct_list.id}/')

		self.assertContains(response, 'itemey 1')
		self.assertNotContains(response, 'other list item 1')
		self.assertNotContains(response, 'other list item 2')

	def test_passes_correct_list_to_template(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		response = self.client.get(f'/lists/{correct_list.id}/')
		self.assertEqual(response.context['list'], correct_list)


class NewListTest(TestCase):

	def test_can_save_a_POST_request(self):
		response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
		# check orm correction
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertIn(new_item.text, 'A new list item')

	def test_redirects_after_POST(self):
		# check for PRG
		response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
		new_list = List.objects.first()
		self.assertEqual(response.status_code, 302)
		# self.assertEqual(response['location'], '/')
		# self.assertEqual(response['location'], 'http://testserver/')
		self.assertRedirects(response, f'/lists/{new_list.id}/')


class NewItemTest(TestCase):

	def test_can_save_a_POST_to_an_existing_list(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()

		self.client.post(
			f'/lists/{correct_list.id}/add_item',
			data={'item_text': 'a new item for an exsiting list'}
			)
	
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'a new item for an exsiting list')
		# when we comparing two objects, django checks for their primary key
		self.assertEqual(new_item.list, correct_list)

	def test_redirects_to_list_view(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()

		response = self.client.post(
			f'/lists/{correct_list.id}/add_item',
			)

		self.assertRedirects(response, f'/lists/{correct_list.id}/')