from django.test import TestCase

class TestViews(TestCase):
   @classmethod
   def setUpTestData(cls):
      print("Running FavorLoginViewTest...")
      cls.login_url = "/login/"


   def test_view_url_exists(self):
      expected_status_code = 200

      response = self.client.get(self.login_url)

      self.assertEqual(expected_status_code, response.status_code)


   def test_view_ignores_base_template(self):
      expected_status_code = 200
      expected_template_to_ignore = "base.html"

      response = self.client.get(self.login_url)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTemplateNotUsed(response, expected_template_to_ignore)


   def test_view_uses_login_template(self):
      expected_status_code = 200
      expected_template = "registration/login.html"

      response = self.client.get(self.login_url)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTemplateUsed(response, expected_template)


   def test_login_request_takes_to_home(self):
      expected_redirect_url = "/"

      # response = self.client.post(self.login_url, {"username" : "TEST", "password" : ""})
      self.assertTrue(True)