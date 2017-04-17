from django.test import TestCase

from .utils import *
# Create your tests here.

class AnimalTestCase(TestCase):
    # def setUp(self):
        # Animal.objects.create(name="lion", sound="roar")
        # Animal.objects.create(name="cat", sound="meow")

    def test_flickr_image(self):
        get_latest_flickr_image()