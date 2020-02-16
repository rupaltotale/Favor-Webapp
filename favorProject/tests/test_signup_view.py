from django.test import TestCase

class TestViews(TestCase):
   @classmethod
   def setUpTestData(cls):
      print("Running FavorSignupViewTest...")
      cls.signup_url = "/signup/"

   def test_view_url_exists(self):
      expected_status_code = 200

      response = self.client.get(self.signup_url)

      self.assertEqual(expected_status_code, response.status_code)


   def test_view_ignores_base_template(self):
      expected_status_code = 200
      expected_template_to_ignore = "base.html"

      response = self.client.get(self.signup_url)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTemplateNotUsed(response, expected_template_to_ignore)


   def test_view_uses_signup_template(self):
      expected_status_code = 200
      expected_template = "signup.html"

      response = self.client.get(self.signup_url)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTemplateUsed(response, expected_template)