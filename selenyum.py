from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def ara(data):
    driver_paht = "E:\driver/chromedriver"
    browser = webdriver.Chrome(driver_paht)
    browser.get("https://www.google.com/")
    browser.maximize_window()
    ara = browser.find_element_by_xpath("// input [@ name = 'q']")
    ara.send_keys(data)
    ara.send_keys(Keys.ENTER)






