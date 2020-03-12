from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from tests.factories import *
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from ui_tests.selenium_helper import *
import os
from favorApp.models import Favor
import time

class ShowServicesUITests(StaticLiveServerTestCase):

    def setUp(self):
        super(ShowServicesUITests, self).setUp()
        print("Running ShowServicesUITests...")
        using_custom_driver_path = os.getenv("USING_CUSTOM_WEBDRIVER_PATH")
        if using_custom_driver_path == "YES":
            self.browser = webdriver.Chrome(
                executable_path=os.getenv("CHROMEDRIVER") + "/chromedriver.exe"
            )
        else:
            self.browser = webdriver.Chrome()

        user = UserFactory()
        user.save()
        tempUser = UserFactory()
        tempUser.save()
        favor1 = FavorFactory(owner=tempUser)
        favor1.save()
        favor2 = FavorFactory(title="DIFFERENT", owner=tempUser)
        favor2.save()
        self.user = user
        SeleniumLoginHelper.do_login(self.browser, self.live_server_url, user)


    def tearDown(self):
        self.browser.quit()
        super(ShowServicesUITests, self).tearDown()


    def test_cards_show_correctly(self):
        expected_num_favors = len(Favor.objects.all())
        assert(expected_num_favors > 0)
        self.browser.get(self.live_server_url + "/")
        
        cards = self.browser.find_elements_by_class_name("my-card")

        for element in cards:
            helper_card = SeleniumFavorHelper(element)
            favor_obj = Favor.objects.get(id=helper_card.id)
            favor_obj_date = favor_obj.date.replace(second=0, microsecond=0, tzinfo=None)
            self.assertEqual(favor_obj.title, helper_card.title)
            self.assertEqual(favor_obj.description, helper_card.description)
            self.assertEqual(favor_obj.number_of_favors, helper_card.number_of_favors)
            self.assertEqual(favor_obj.owner, helper_card.owner)
            self.assertEqual(favor_obj.location, helper_card.location)
            self.assertEqual(favor_obj_date, helper_card.date)

        self.assertEqual(expected_num_favors, len(cards))