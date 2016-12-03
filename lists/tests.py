from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import homepage

from django.template.loader import render_to_string

from django.http import HttpRequest

# Create your tests here.
class HomepageTest(TestCase):

	def test_root_url_resolves_to_homepage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, homepage)

	def test_homepage_returns_correct_html(self):
		request = HttpRequest()
		response = homepage(request)

		expected_html = render_to_string('index.html')
		self.assertEqual(response.content.decode(), expected_html)