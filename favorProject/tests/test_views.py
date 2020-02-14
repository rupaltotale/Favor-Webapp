from django.test import TestCase

# Create your tests here.
# Test template based off of https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

class TestViews(TestCase):
   @classmethod
   # setUpTestData: Run once to set up non-modified data for all class methods.
   def setUpTestData(cls):
      pass
   
   # setUp: Run once for every test method to setup clean data.
   def setUp(self):
      pass

   def test_false_is_false(self):
      self.assertFalse(False)

   def test_false_is_true(self):
      self.assertTrue(True)

   def test_one_plus_one_equals_two(self):
      self.assertEqual(1 + 1, 2)


