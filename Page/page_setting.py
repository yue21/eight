from Base.Base import Base
import Page


# 设置页面
class Page_setting(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_more_but(self):
        '''点击更多按钮'''
        self.click_element(Page.more_btn_xpath)