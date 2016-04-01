# -*- coding: utf-8 -*-
import unittest

import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class buying_process_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def css_selector(self, loc):
        dr = self.driver
        return dr.find_element_by_css_selector(loc)

    def test_search_in_python_org(self):
        driver = self.driver
        loc = self.css_selector
        driver.get("http://makeup.com.ua/")
        element = driver.find_element_by_name("searchstring")
        element.send_keys("Kenzo", Keys.RETURN)
        ActionChains(driver).move_to_element(loc('.simple-slider-list__image')).perform()
        loc(".simple-slider-list__item:nth-of-type(1) .button.buy").click()
        loc("div.popup-content div.button").click()
        loc("#name").send_keys(u"Евгений")
        loc("#surname").send_keys(u"Нестеренко")
        loc("#additional_field_1").send_keys(u"0953977833")
        loc("#email").send_keys(u"lightnem33@ya.ru")
        loc(".button.short").click()
        time.sleep(2)
        el4 = driver.find_element_by_css_selector("#city")
        el4.clear()
        el4.send_keys(u"Запорожье")
        time.sleep(2)
        driver.find_element_by_css_selector(".search-value__list_item[data-id='38088']").click()
        time.sleep(2)
        loc(".custom-select__value-wrap").click()
        dropdown = loc(".custom-select__list")
        #FOR i created only for my experience
        for option in dropdown.find_elements_by_class_name("custom-select__item"):
            if option.get_attribute("data-value") == u"9":
                option.click()
                break
        time.sleep(2)
        loc("#store_list .custom-select__value-wrap").click()
        time.sleep(2)
        loc(".custom-select__item[data-value='9707']").click()
        assert u"Відділення №5" in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()