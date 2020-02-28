from django.test import LiveServerTestCase
from selenium import webdriver
from tests.factories import *
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
import os
import time

class LoginUITests(LiveServerTestCase):

    def setUp(self):
        super(LoginUITests, self).setUp()
        print("Running LoginUITests...")
        using_custom_driver_path = os.getenv("USING_CUSTOM_WEBDRIVER_PATH")
        if using_custom_driver_path == "YES":
            self.browser = webdriver.Chrome(
                executable_path=os.getenv("CHROMEDRIVER") + "/chromedriver.exe"
            )
        else:
            self.browser = webdriver.Chrome()

        user = UserFactory()
        user.save()
        self.user = user


    def tearDown(self):
        self.browser.quit()
        super(LoginUITests, self).tearDown()


    def test_login(self):
        expected_url = self.live_server_url + "/"
        self.browser.get(self.live_server_url + '/login')

        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')

        submit = self.browser.find_element_by_id('login-but')

        #Fill the form with data
        username.send_keys(self.user.username)
        password.send_keys('password')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        self.assertEqual(expected_url, self.browser.current_url)
        self.browser.close()
