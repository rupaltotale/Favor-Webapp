from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from tests.factories import *
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
import os
import time

class LandingPageUITests(StaticLiveServerTestCase):

    def setUp(self):
        super(LandingPageUITests, self).setUp()
        print("Running LandingPageUITests...")
        using_custom_driver_path = os.getenv("USING_CUSTOM_WEBDRIVER_PATH")
        if using_custom_driver_path == "YES":
            self.browser = webdriver.Chrome(
                executable_path=os.getenv("CHROMEDRIVER") + "/chromedriver.exe"
            )
        else:
            self.browser = webdriver.Chrome()

        self.browser.implicitly_wait(2)



    def tearDown(self):
        self.browser.quit()
        super(LandingPageUITests, self).tearDown()


    def test_login(self):
        expected_url = self.live_server_url + "/login"
        self.browser.get(self.live_server_url + '/landing/')

        slideshow_container = self.browser.find_element_by_class_name("slideshow-container")
        caption = slideshow_container.find_element_by_id("caption").get_attribute("innerHTML")
        get_started_button = self.browser.find_element_by_link_text("Get Started")

        get_started_button.click()

        self.assertTrue(expected_url in self.browser.current_url)

        self.browser.close()
