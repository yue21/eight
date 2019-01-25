import pytest, sys, os
sys.path.append(os.getcwd())
from Base.initdriver import get_driver
from Base.page import Page


class Test_set_network():
    def setup_class(self):
        # 实例化driver
        self.driver = get_driver('com.android.settings', '.Settings')
        # 实例化page对象
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    # 依赖条件
    @pytest.fixture(scope="class", autouse=True)
    def click_more_and_mobile_network(self):
        '''点击更多和移动网络'''
        self.page_obj.get_page_setting_obj().click_more_but()
        self.page_obj.get_page_more_obj().click_mobile_network_but()

    def test_set_network(self):
        '''点击首选网络和3G'''
        self.page_obj.get_page_mobile_network().click_one_network_but()
        self.page_obj.get_page_mobile_network().set_network_type(1)
        '''获取结果列表--断言'''
        assert "3G" in self.page_obj.get_page_mobile_network().get_result_list()
