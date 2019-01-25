from Base.Base import Base
import Page


# 更多页面
class Page_more(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_mobile_network_but(self):
        '''点击移动网络按钮'''
        self.click_element(Page.mobile_network_xpath)
