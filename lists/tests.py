from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
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

	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'item_text': 'A new list item'})
		self.assertEqual(response.status_code, 200)
		self.assertIn('A new list item', response.content.decode())