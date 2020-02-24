from django.test import TestCase
from tests.factories import *
from django.urls import reverse
from favorApp.models import Favor

class AddFavorViewTests(TestCase):
   @classmethod
   def setUpTestData(cls):
      print("Running FavorAddFavorViewTest...")
      user = UserFactory()
      user.save()
      cls.user = user
      cls.url = "/add-favor/"


   def setUp(self):
      self.client.login(
         username=self.user.username, password='password'
      )
      
   
   def test_view_url_exists(self):
      expected_status_code = 200

      response = self.client.get(self.url)

      self.assertEqual(expected_status_code, response.status_code)


   def test_view_redirects_on_not_logged_in(self):
      expected_status_code = 302
      expected_redirect_url = reverse('login') + "?next="

      self.client.logout()
      response = self.client.get(self.url)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTrue(expected_redirect_url in response.url)


   def test_view_uses_base_template(self):
      expected_status_code = 200
      expected_template = "base.html"

      response = self.client.get(self.url)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTemplateUsed(response, expected_template)


   def test_view_uses_own_template(self):
      expected_status_code = 200
      expected_template = "add_favor.html"

      response = self.client.get(self.url)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTemplateUsed(response, expected_template)


   def test_view_with_valid_add_request(self):
      expected_status_code = 200
      expected_redirect_url = reverse('home')
      temp_favor = FavorFactory()
      response = self.client.post(self.url, data={
            "owner" : self.user.username,
            "description" : temp_favor.description,
            "title" : temp_favor.title,
            "date" : temp_favor.date,
            "location" : temp_favor.location,
            "number_of_favors" : temp_favor.number_of_favors,
            "volunteer_event" : False,
            "requester_signed" : False,
            "giver_signed" : False
         }
      )

      self.assertEqual(expected_status_code, response.status_code)
      """ print("Last", Favor.objects.latest('id'))

      try:
         created_favor_id = Favor.objects.get(id=Favor.objects.latest('id'))
         print(created_favor_id)
      except Favor.DoesNotExist:
         self.assertTrue(False) """