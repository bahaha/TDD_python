from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import homepage

# Create your tests here.
class HomepageTest(TestCase):
	def test_root_url_resolves_to_homepage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, homepage)