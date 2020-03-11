from django.test import TestCase, RequestFactory
from tests.factories import *
from django.urls import reverse
from favorApp.models import Favor
from favorApp.views import process_profile_page_req

class ProcessPendingRequestChangeTests(TestCase):
   @classmethod
   def setUpTestData(cls):
      print("Running ProcessPendingRequestChangeTest...")
      user = UserFactory()
      user.save()
      user2 = UserFactory()
      user2.save()
      favor = FavorFactory(owner=user)
      favor.save()
      favor.pendingUsers.add(user2)
      cls.user = user
      cls.user2 = user2
      cls.favor = favor
      cls.url = "/process-pending-user-change/"
      cls.request_factory = RequestFactory()


   def setUp(self):
      self.client.login(
         username=self.user.username, password='password'
      )


   def test_view_url_exists(self):
      expected_status_code = 405

      response = self.client.get(self.url)

      self.assertEqual(expected_status_code, response.status_code)


   def test_view_returns_forbidden(self):
      expected_status_code = 403
      request = self.request_factory.post(self.url, {
         "user_id" : self.user2.id,
         "favor_id" : self.favor.id,
         "action" : "ACCEPT"
      })
      request.user = self.user2

      response = process_profile_page_req(request)

      self.assertEqual(expected_status_code, response.status_code)


   def test_view_allows_confimation(self):
      expected_status_code = 302
      expected_redirect_url = '/user/'
      request = self.request_factory.post(self.url, {
         "user_id" : self.user2.id,
         "favor_id" : self.favor.id,
         "action" : "ACCEPT"
      })
      request.user = self.user

      response = process_profile_page_req(request)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertEqual(expected_redirect_url, response.url)
      self.assertTrue(self.user2 in self.favor.confirmedUsers.all())
      self.assertTrue(self.user2 not in self.favor.pendingUsers.all())


   def test_view_allows_deny(self):
      expected_status_code = 302
      expected_redirect_url = '/user/'
      request = self.request_factory.post(self.url, {
         "user_id" : self.user2.id,
         "favor_id" : self.favor.id,
         "action" : "DENY"
      })
      request.user = self.user

      response = process_profile_page_req(request)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertEqual(expected_redirect_url, response.url)
      self.assertTrue(self.user2 not in self.favor.confirmedUsers.all())
      self.assertTrue(self.user2 not in self.favor.pendingUsers.all())


   def test_view_invalid_action(self):
      expected_status_code = 405
      request = self.request_factory.post(self.url, {
         "user_id" : self.user2.id,
         "favor_id" : self.favor.id,
         "action" : "FAKE"
      })
      request.user = self.user

      response = process_profile_page_req(request)

      self.assertEqual(expected_status_code, response.status_code)
      self.assertTrue(self.user2 in self.favor.pendingUsers.all())
