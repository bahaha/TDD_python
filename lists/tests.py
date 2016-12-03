from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import homepage

from django.http import HttpRequest

# Create your tests here.
class HomepageTest(TestCase):

	def test_root_url_resolves_to_homepage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, homepage)

	def test_homepage_returns_correct_html(self):
		request = HttpRequest()
		response = homepage(request)

		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>To-Do lists</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))