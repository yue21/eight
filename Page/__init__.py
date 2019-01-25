from selenium.webdriver.common.by import By

"""设置页面"""
# 更多按钮
more_btn_xpath = (By.XPATH, "//*[contains(@text,'更多')]")
"""设置页面 -更多页面"""
# 移动网络
mobile_network_xpath = (By.XPATH, "//*[contains(@text,'移动')]")
"""设置页面 -更多页面 -移动网络页面"""
# 首选网络类型
one_network_xpath = (By.XPATH, "//*[contains(@text,'首选')]")
# 3G
set_network_3G_xpath = (By.XPATH, "//*[contains(@text,'3G')]")
# 取结果列表
set_network_list_ids = (By.ID, "android:id/summary")