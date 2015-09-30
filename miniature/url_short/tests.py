from django.test import TestCase
from .models import Link

# Create your tests here.
class URLShortenerTest(TestCase):
    def setUp(self):
        """
            For global vars
        """
        self.url = 'https://www.facebook.com/'

    def test_shortened_url_greater_than_orig_url(self):


