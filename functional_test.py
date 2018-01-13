from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = find_elements_by_tag_name('tr')
		assertIn(row_text, row.text for row in rows)

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Alice heard about a cool new online to-do app
		# she goes to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a to-do items straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# She types "Buy peacock feathers into a text box"
		inputbox.send_keys('1:Buy peacock feathers')

		# When she hits enter, the page updates, and now the page
		# lists "1: Buy peacock feathers" as an item in a to-do list table
		inputbox.send_keys(Keys.ENTER)
		time.sleep(5)
		self.check_for_row_in_list_table("1:Buy peacock feathers")

		# There is still a text box inviting her to add another item.
		# She enters "Use peacock feathers to make a fly"
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		# The page updates again, and now shows both items on her list
		self.check_for_row_in_list_table('1:Buy peacock feathers')
		self.check_for_row_in_list_table('Use peacock feathers to make a fly')

		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')