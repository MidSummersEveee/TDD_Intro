from selenium import webdriver
import unittest

calss NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# She is invited to enter a to-do items straight away


if__name__ == '__main__':
	unittest.main(warnings='ignore')