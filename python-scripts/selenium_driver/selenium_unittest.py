# -*- coding: utf-8 -*-
#
# Reference:
# http://selenium-python.readthedocs.org/getting-started.html
# 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class TestGoogleDotCom(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie("C:\work\selenium-IEDriverServer\IEDriverServer.exe")
        self.driver.implicitly_wait(30)    
    
    def test_access_webpage(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        
        self.assertIn("Google", driver.title)
   
    def test_search_in_google(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        elem = driver.find_element_by_name("q")
        
        elem.send_keys(u"日本語")
        #elem.send_keys(u"laoweahoahfjoafroiehwoh")
        elem.send_keys(Keys.RETURN)
        
        try:
            element = WebDriverWait(driver, 10).until(
                lambda driver : driver.find_element_by_id("msg_box")
            )
        
        except:
            pass
        
        assert u"一致する情報は見つかりませんでした。" not in driver.page_source
    
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
