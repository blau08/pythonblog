from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from post.views import home_page

# Create your tests here.

class HomePageViewTest(TestCase):

    def test_home_page_uses_home_template(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
