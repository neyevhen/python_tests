# -*- coding: utf-8 -*-
import unittest

import time
from selenium.webdriver import ActionChains
from selenium import webdriver

class buying_process_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def css_selector(self, loc):
        dr = self.driver
        return dr.find_element_by_css_selector(loc)

    def test_search_in_python_org(self):
        driver = self.driver
        loc = self.css_selector
        driver.get("http://makeup.com.ua/brand/24729/")
        ActionChains(driver).move_to_element(loc('.simple-slider-list__image')).perform()
        loc(".simple-slider-list__item:nth-of-type(1) .button.buy").click()
        loc("div.popup-content div.button").click()
        enter_text = {"#name": u"Евгений",
                      "#surname": u"Нестеренко",
                      "#additional_field_1": u"0953977833",
                      "#email": u"lightnem33@ya.ru"}
        for key in enter_text:
            loc(key).send_keys(enter_text[key])
        loc(".button.short").click()
        time.sleep(2)
        el = loc("#city")
        el.clear()
        el.send_keys(u"Запорожье")
        dropdown_input = [".search-value__list_item[data-id='38088']",
                          ".custom-select__value-wrap",
                          ".custom-select__item[data-value='9']",
                          "#store_list .custom-select__value-wrap",
                          ".custom-select__item[data-value='9707']"]
        for input in dropdown_input:
            time.sleep(2)
            loc(input).click()
        # ...... SUBMIT.........
        assert u"Відділення №5" in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


    #from selenium.webdriver.common.keys import Keys
    # element = driver.find_element_by_name("searchstring")
    # element.send_keys("Kenzo", Keys.RETURN)

    # dropdown = loc(".custom-select__list")
    # for option in dropdown.find_elements_by_class_name("custom-select__item"):
    #    if option.get_attribute("data-value") == u"9":
    #        option.click()
    #        break