from favorApp.models import User
from dateutil.parser import parse
from selenium.webdriver.common.keys import Keys
from time import sleep

class SeleniumHelperException(Exception):
    def __init__(self, error):
        self.error = error


class SeleniumLoginHelper:

    @staticmethod
    def do_login(browser, base_url, user, wait=0):
        expected_url = base_url + "/"
        browser.get(base_url + '/login')
        
        if wait > 0:
            sleep(wait)

        username = browser.find_element_by_id('id_username')
        password = browser.find_element_by_id('id_password')

        submit = browser.find_element_by_id('login-but')

        #Fill the form with data
        username.send_keys(user.username)

        if wait > 0:
            sleep(wait)

        password.send_keys('password')

        if wait > 0:
            sleep(wait)
            
        #submitting the form
        submit.send_keys(Keys.RETURN)

        assert(expected_url == browser.current_url)


class SeleniumFavorHelper:

    def __init__(self, card=None):
        self.card = card
        self.id = self.get_id_from_favor_card(card) if card is not None else None
        self.title = self.get_favor_card_title(card) if card is not None else None
        self.description = self.get_favor_card_description(card) if card is not None else None
        self.number_of_favors = self.get_favor_card_favors(card) if card is not None else None
        inner_card_items = self.__parse_inner_card() if card is not None else [None, None, None]
        self.owner = User.objects.get(username=inner_card_items[0]) if inner_card_items[0] is not None else None
        self.username = self.owner.username if self.owner is not None else None
        self.location = inner_card_items[1]
        self.date = parse(inner_card_items[2])
    
    def get_id_from_favor_card(self, card):
        a_element = card.find_element_by_tag_name("button")
        value = a_element.get_attribute("value")
        return int(value)

    def get_favor_card_title(self, card):
        if card is not None:
            return card.find_element_by_class_name("my-card-title").get_attribute("innerHTML")
        return self.title

    def get_favor_card_description(self, card):
        if card is not None:
            return card.find_element_by_class_name("my-card-desc").get_attribute("innerHTML")
        return self.description

    def get_favor_card_favors(self, card):
        if card is not None:
            favorHtml = card.find_element_by_class_name("num-favors").get_attribute("innerHTML")
            for word in favorHtml.split():
                if word.isdigit():
                    return int(word)
            raise SeleniumHelperException("No Favor Amount Found")
        return self.number_of_favors

    def __parse_inner_card(self, specific_search=False, card=None, specific_search_value=""):
        order = ["owner", "location", "date"]
        inner_values = [None] * 3
        if card == None and self.card is not None:
            card = self.card
        container_elements = card.find_element_by_class_name("icons-container").find_elements_by_class_name("icon-text-container")
        assert(len(container_elements) == 3)
        for i, element in enumerate(container_elements):
            # Verify correct insides
            element.find_element_by_tag_name("i")
            inner_value_element = element.find_element_by_tag_name("p")
            if specific_search is True and specific_search_value == order[i]:
                return inner_value_element.get_attribute("innerHTML")
            inner_values[i] = inner_value_element.get_attribute("innerHTML")
        return inner_values

    def get_favor_card_owner(self, card):
        if card is not None:
            return User.objects.get(username=self.__parse_inner_card(specific_search=True, card=card, specific_search_value="owner"))
        return self.owner

    def get_favor_card_location(self, card):
        if card is not None:
            return self.__parse_inner_card(specific_search=True, card=card, specific_search_value="location")
        return self.location

    def get_favor_card_date(self, card):
        if card is not None:
            return parse(self.__parse_inner_card(specific_search=True, card=card, specific_search_value="date"))
        return self.date