from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class SignupViewTests(TestCase):
   @classmethod
   def setUpTestData(cls):
      print("Running FavorSignupViewTest...")
      cls.url = reverse('signup')

   def test_view_url_exists(self):
      expected_status_code = 200

      response = self.client.get(self.url)

      self.assertEqual(expected_status_code, response.status_code)


   def test_view_ignores_base_template(self):
      expected_status_code = 200
      expected_template_to_ignore = "base.html"

      response = self.client.get(self.url)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTemplateNotUsed(response, expected_template_to_ignore)


   def test_view_uses_signup_template(self):
      expected_status_code = 200
      expected_template = "signup.html"

      response = self.client.get(self.url)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTemplateUsed(response, expected_template)


   def test_view_with_valid_singup_request(self):
      expected_status_code = 302
      expected_redirect_url = reverse('home')
      test_username = "TEST"
      test_password = "TEST$1131ADda"
      
      response = self.client.post(self.url, data={
            "username" : test_username,
            "first_name" : test_username,
            "last_name" : test_username,
            "email" : "test@test.com",
            "password1" : test_password,
            "password2" : test_password
         }
      )

      self.assertEqual(expected_status_code, response.status_code)
      self.assertEqual(response.url, expected_redirect_url)

      try:
         created_user = User.objects.get(username=test_username)
         created_user.delete()
      except User.DoesNotExist:
         self.assertTrue(False)


   def test_view_with_invalid_singup_request(self):
      expected_status_code = 200

      response = self.client.post(self.url, data={})

      self.assertEqual(expected_status_code, response.status_code)