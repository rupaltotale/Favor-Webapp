from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from tests.factories import *
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from ui_tests.selenium_helper import SeleniumLoginHelper
import os
from favorApp.models import Favor
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProfileUITests(StaticLiveServerTestCase):

    def setUp(self):
        super(ProfileUITests, self).setUp()
        print("Running ProfileUITests...")
        using_custom_driver_path = os.getenv("USING_CUSTOM_WEBDRIVER_PATH")
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        if using_custom_driver_path == "YES":
            self.browser = webdriver.Chrome(
                options=options,
                executable_path=os.getenv("CHROMEDRIVER") + "/chromedriver.exe"
            )
        else:
            self.browser = webdriver.Chrome(options=options)

        user = UserFactory()
        user.save()
        user2 = UserFactory()
        user2.save()
        user3 = UserFactory()
        user3.save()
        favor = FavorFactory(owner=user)
        favor.save()
        favor.pendingUsers.add(user2)
        favor.pendingUsers.add(user3)
        self.user = user
        self.user2 = user2
        self.user3 = user3
        self.favor = favor
        self.wait = 0
        SeleniumLoginHelper.do_login(self.browser, self.live_server_url, user, wait=0)


    def do_click_and_wait(self, ele):
        if type(ele) == str:
            ele = WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable((By.ID, ele)))
        ele.click()
        time.sleep(self.wait)


    def tearDown(self):
        self.browser.quit()
        super(ProfileUITests, self).tearDown()


    def test_can_get_to_profile(self):
        expected_url = self.live_server_url + "/user/"

        self.browser.get(self.live_server_url + "/")
        self.browser.implicitly_wait(2)
        
        time.sleep(self.wait)

        avatar_element = self.browser.find_element_by_id("avatar").find_element_by_tag_name("a")
        self.do_click_and_wait(avatar_element)

        profile_element = self.browser.find_element_by_link_text("Profile")
        self.do_click_and_wait(profile_element)

        self.assertEqual(expected_url, self.browser.current_url)

        view_button = self.browser.find_element_by_id("pending-user-{}".format(self.favor.id))
        self.do_click_and_wait(view_button)

        self.do_click_and_wait("deny-{}-{}".format(self.user3.id, self.favor.id))

        self.assertTrue(self.user3 not in self.favor.pendingUsers.all())
        self.assertTrue(self.user3 not in self.favor.confirmedUsers.all())

        view_button = self.browser.find_element_by_id("pending-user-{}".format(self.favor.id))
        self.do_click_and_wait(view_button)

        self.do_click_and_wait("accept-{}-{}".format(self.user2.id, self.favor.id))

        self.assertTrue(self.user2 not in self.favor.pendingUsers.all())
        self.assertTrue(self.user2 in self.favor.confirmedUsers.all())

        view_button = self.browser.find_element_by_id("pending-user-{}".format(self.favor.id))
        self.do_click_and_wait(view_button)