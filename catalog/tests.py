from django.test import TestCase, Client
from django.core import urlresolvers
import httplib


class NewUserTestCase(TestCase):
    def test_view_homepage(self):
        client = Client()
        home_url = urlresolvers.reverse('catalog_home')
        response = client.get(home_url)
        # check that we did get a response
        self.failUnless(response)
        # check that status code of response was success
        # (httplib.OK = 200)
        self.assertEqual(response.status_code, httplib.OK)
