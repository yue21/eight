from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def search_element(self, loc, timeout=15, poll_frequency=1):
        ''' 定位单个元素'''
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_elements(self, loc, timeout=15, poll_frequency=1):
        '''定位一组元素'''
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=15, poll_frequency=1):
        '''点击定位对象'''
        self.search_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text, timeout=15, poll_frequency=1):
        '''定位元素发送内容'''
        input_text = self.search_element(loc, timeout, poll_frequency)
        input_text.clear()
        input_text.send_keys(text)
