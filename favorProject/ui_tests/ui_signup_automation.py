from django.test import LiveServerTestCase
from selenium import webdriver
from tests.factories import *
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
import os
import time

class SignUpUITests(LiveServerTestCase):

    def setUp(self):
        super(SignUpUITests, self).setUp()
        print("Running SignUpUITests...")
        using_custom_driver_path = os.getenv("USING_CUSTOM_WEBDRIVER_PATH")
        if using_custom_driver_path == "YES":
            self.browser = webdriver.Chrome(
                executable_path=os.getenv("CHROMEDRIVER") + "/chromedriver.exe"
            )
        else:
            self.browser = webdriver.Chrome()

        user = UserFactory()
        self.user = user
        self.temp_password = "12345ABCDef$"


    def tearDown(self):
        self.browser.quit()
        super(SignUpUITests, self).tearDown()


    def test_login(self):
        expected_url = self.live_server_url + "/"
        self.browser.get(self.live_server_url + '/signup')

        username = self.browser.find_element_by_name('username')
        first_name = self.browser.find_element_by_name('first_name')
        last_name = self.browser.find_element_by_name('last_name')
        email = self.browser.find_element_by_name('email')
        password1 = self.browser.find_element_by_name('password1')
        password2 = self.browser.find_element_by_name('password2')

        submit = self.browser.find_element_by_tag_name("form").find_element_by_tag_name("button")

        #Fill the form with data
        username.send_keys(self.user.username)
        first_name.send_keys(self.user.first_name)
        last_name.send_keys(self.user.last_name)
        email.send_keys(self.user.email)
        password1.send_keys(self.temp_password)
        password2.send_keys(self.temp_password)

        #submitting the form
        submit.send_keys(Keys.RETURN)

        self.assertEqual(expected_url, self.browser.current_url)

        try:
            created_user = User.objects.get(username=self.user.username)
            created_user.delete()
        except User.DoesNotExist:
            self.fail("User object was not created!")

        self.browser.close()
