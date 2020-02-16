from django.test import TestCase

class TestViews(TestCase):
   @classmethod
   def setUpTestData(cls):
      print("Running FavorHomeViewTest...")
      cls.home_url = "/"

   def test_view_url_exists(self):
      expected_status_code = 200

      response = self.client.get(self.home_url)

      self.assertEqual(expected_status_code, response.status_code)


   def test_view_uses_base_template(self):
      expected_status_code = 200
      expected_template = "base.html"

      response = self.client.get(self.home_url)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTemplateUsed(response, expected_template)


   def test_view_uses_slideshow_template(self):
      expected_status_code = 200
      expected_template = "slideshow.html"

      response = self.client.get(self.home_url)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTemplateUsed(response, expected_template)


   def test_view_uses_home_template(self):
      expected_status_code = 200
      expected_template = "home.html"

      response = self.client.get(self.home_url)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTemplateUsed(response, expected_template)