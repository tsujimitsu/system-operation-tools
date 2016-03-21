# -*- coding: utf-8 -*-

# selenium driver ie11
# http://selenium-release.storage.googleapis.com/index.html
# http://stackoverflow.com/questions/31134408/unable-to-find-element-on-closed-window-on-ie-11-working-with-selenium

# selenium driver chrome
# https://chromedriver.storage.googleapis.com/index.html

# reference
# http://qiita.com/gluelan2013/items/6977cde545e2bcf08081
# http://miya-jan.hatenablog.com/entry/2014/04/22/232919


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


def search_to_google(driver, keyword):
    """
    """
    driver.get("http://www.google.com/xhtml")
    time.sleep(5)
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(keyword)
    search_box.submit()
    time.sleep(5)


def main():
    """
    """
    #driver = webdriver.Firefox()
    #driver = webdriver.Chrome("C:\work\chromedriver_win32\chromedriver.exe")
    
    # if you use IEdriver, change browser setting
    # Internet Option > Secutiry
    # All security zone "Enable Protected Mode" unchecked.
    driver = webdriver.Ie("C:\work\selenium-IEDriverServer\IEDriverServer.exe")


    driver.implicitly_wait(10)
    search_to_google(driver, u"日本語")
    
    driver.quit()
    #driver.back()
    #driver.forward()


if __name__ == '__main__':
    main()