#PYTHON LIB
import uuid
#DJANGO LIB
from django.core.urlresolvers import reverse
from django.test import TestCase
#APP LIB
from .forms import URLShortenForm 
from .models import Link
from .shortener import shorten

# Create your tests here.
def _generate_hashkey():
    hashkey = str(uuid.uuid4())[:7].replace('-', '').lower()
        #ref_id = '9f16a22615'
    try:
        url_exists = Link.objects.get(short_url=hashkey)
        _generate_hashkey()
    except:
        return hashkey

class URLShortenerModelTest(TestCase):
    def setUp(self):
        """
            For global vars
        """
        self.url = 'https://www.facebook.com/'

    ##########MODELS TESTING
    def test_shortened_url(self):
        """
            Test to ensure url gets shortened and it should be atleast shorter than the orig url
        """
        ln = Link(url=self.url)
        ln.short_url = _generate_hashkey() 
        ln.save()
        l = Link.objects.get(url=self.url)
        self.assertLess(len(l.short_url), len(self.url))

    def test_revert_shortened_url_to_orig_url(self):

        ln = Link(url=self.url)
        ln.short_url = _generate_hashkey() 
        ln.save()
        l = Link.revert_orig_url(ln.short_url)
        self.assertEquals(self.url, l)
        

    def test_existing_shortened_url(self):
        """
            Test to ensure existing shortened url must not generate another hash and return the same short url
        """
        #Create initial url w/ shortened url
        ln = Link(url=self.url)
        ln.short_url = _generate_hashkey() 
        ln.save()

        #Get existing URL and return 
        (l, exists) = Link.objects.get_or_create(url=self.url)
        if exists:
            self.assertEquals(ln.short_url, l.short_url)

    #########shortener.py module function testing
    def test_shortener_not_existing_url(self):
        su = shorten(self.url)
        l = Link.objects.get(url=self.url)
        self.assertEquals(su.short_url, l.short_url)
        
    def test_shortener_existing_url(self):
        su  = shorten(self.url)
        su2 = shorten(self.url)
        self.assertEquals(su, su2)


    #########VIEWS TESTING
    def test_homepage(self):
        """
        Tests that a home page exists and it contains a form.
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)

    def test_short_url_redirect_to_long_url(self):
        """
        Tests short url redirects to long/orig url.
        """
        su  = shorten(self.url)
        response = self.client.get(reverse("url_shorten_redirect", kwargs={"urlshort": su.short_url}))
        self.assertRedirects(response, self.url)

    def test_short_url_redirect_n_times(self): 
        """
        Tests short url redirects to long/orig url n times to ensure it's properly working
        """
        TIMES = 100
        for i in xrange(TIMES):
            uri = self.url +  _generate_hashkey()
            ln = shorten(uri)
            long_ln = Link.revert_orig_url(ln.short_url)
            print "%s = %s" %(uri, long_ln)
            self.assertEqual(uri, long_ln)


class URLShortenerFormTest(TestCase):
    def setUp(self):
        self.url = 'https://www.facebook.com/'
        self.invalid_url = 'testst123v'

    def test_shortener_form_blank(self):
        f = URLShortenForm({})
        self.assertFalse(f.is_valid())
        self.assertEquals(f.errors, { "url": ["This field is required."] })

    def test_shortener_form_invalid_url(self):
        f = URLShortenForm({"url": self.invalid_url})
        self.assertFalse(f.is_valid())
        self.assertEquals(f.errors, { "url": ["Enter a valid URL."] })

    def test_shortener_form_not_blank(self):
        f = URLShortenForm({"url": self.url})
        self.assertTrue(f.is_valid())

    def test_shortener_form_not_blank_twice(self):
        f = URLShortenForm({"url": self.url})
        self.assertTrue(f.is_valid())
