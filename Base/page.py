from Page.page_setting import Page_setting
from Page.page_more import Page_more
from Page.page_mobile_network import Page_mobile_network


class Page:
    def __init__(self, driver):
        self.driver = driver

    def get_page_setting_obj(self):
        return Page_setting(self.driver)

    def get_page_more_obj(self):
        return Page_more(self.driver)

    def get_page_mobile_network(self):
        return Page_mobile_network(self.driver)
