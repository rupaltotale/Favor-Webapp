from django.test import LiveServerTestCase
from selenium import webdriver
from tests.factories import *
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from ui_tests.selenium_helper import SeleniumLoginHelper
import os
from favorApp.models import Favor
import time

class ProfileUITests(LiveServerTestCase):

    def setUp(self):
        super(ProfileUITests, self).setUp()
        print("Running ProfileUITests...")
        using_custom_driver_path = os.getenv("USING_CUSTOM_WEBDRIVER_PATH")
        if using_custom_driver_path == "YES":
            self.browser = webdriver.Chrome(
                executable_path=os.getenv("CHROMEDRIVER") + "/chromedriver.exe"
            )
        else:
            self.browser = webdriver.Chrome()

        user = UserFactory()
        user.save()
        SeleniumLoginHelper.do_login(self.browser, self.live_server_url, user)


    def tearDown(self):
        self.browser.quit()
        super(ProfileUITests, self).tearDown()


    def test_can_get_to_profile(self):
        expected_url = self.live_server_url + "/user/"
        self.browser.get(self.live_server_url + "/")
        self.browser.implicitly_wait(2)
        
        avatar_element = self.browser.find_element_by_id("avatar").find_element_by_tag_name("a")

        avatar_element.click()

        profile_element = self.browser.find_element_by_link_text("Profile")
        profile_element.click()

        self.assertEqual(expected_url, self.browser.current_url)


