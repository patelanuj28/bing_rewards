#!/usr/bin/env python

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class BingTest(unittest.TestCase):
    def setUp(self):
        binary = FirefoxBinary("/Applications/Firefox.app/Contents/MacOS/firefox")
        self.driver = webdriver.Firefox(firefox_binary=binary)

        #self.driver = webdriver.Firefox()
        #/Applications/Firefox.app/Contents/MacOS/firefox
        self.driver.implicitly_wait(30)
        #import pdb; pdb.set_trace()
        self.base_url = "http://www.bing.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bing(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("id_s").click()
        driver.find_element_by_css_selector("span.id_name").click()
        driver.find_element_by_id("i0116").clear()
        driver.find_element_by_id("i0116").send_keys("<bing rewards username>")
        driver.find_element_by_id("i0118").clear()
        driver.find_element_by_id("i0118").send_keys("<bing rewards password>!")
        driver.find_element_by_id("idChkBx_PWD_KMSI0Pwd").click()
        driver.find_element_by_id("idSIButton9").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("1")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("12")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("123")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("1234")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("12345")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("123456789")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("1234567890")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("12345678901")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("123456789012")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("1234567890123")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("12345678901234")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("123456789012345")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("1234567890123456")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("12345678901234567")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("123456789012345678")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("1234567890123456789")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("12345678901234567890")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("123456789012345678901")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("1234567890123456789012")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("12345678901234567890123")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("123456789012345678901234")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("1234567890123456789012345")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("12345678901234567890123456")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("123456789012345678901234567")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("1234567890123456789012345678")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("12345678901234567890123456789")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("123456789012345678901234567890")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("1234567890123456789012345678901")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("12345678901234567890123456789012")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("123456789012345678901234567890123")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("1234567890123456789012345678901234")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("12345678901234567890123456789012345")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("sb_form_q").click()
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("123456789012345678901234567890123456")
        driver.find_element_by_id("sb_form_go").click()
        driver.find_element_by_id("id_l").click()
        driver.find_element_by_css_selector("span.id_name").click()
        driver.find_element_by_id("id_l").click()
        driver.find_element_by_css_selector("span.id_name").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
