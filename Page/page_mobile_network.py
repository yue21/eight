from Base.Base import Base
import Page


class Page_mobile_network(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_one_network_but(self):
        '''点击首选网络'''
        self.click_element(Page.one_network_xpath)

    def set_network_type(self, num):
        '''设置网络类型'''
        if str(num) == '1':
            self.click_element(Page.set_network_3G_xpath)

    def get_result_list(self):
        '''获取结果列表'''
        result_list = self.search_elements(Page.set_network_list_ids)
        return [i.text for i in result_list]
