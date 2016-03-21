# -*- coding: utf-8 -*-

# selenium driver ie11
# http://selenium-release.storage.googleapis.com/index.html
# http://stackoverflow.com/questions/31134408/unable-to-find-element-on-closed-window-on-ie-11-working-with-selenium

# selenium driver Microsoft Edge
# default install path: C:\Program Files (x86)\Microsoft Web Driver\
# https://www.microsoft.com/en-us/download/details.aspx?id=48212

# selenium driver chrome
# https://chromedriver.storage.googleapis.com/index.html

# reference
# http://qiita.com/gluelan2013/items/6977cde545e2bcf08081
# http://miya-jan.hatenablog.com/entry/2014/04/22/232919
# http://yyyank.blogspot.jp/2015/01/selenium2webdrivertips8.html
# https://www.qoosky.net/techs/58


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


def search_to_google(driver, keyword):
    """Display result of google search
    """
    # Access
    driver.get("http://www.google.com/xhtml")
    time.sleep(5)
    
    # Search
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(keyword)
    search_box.submit()
    time.sleep(5)
    
    # Display result page titles
    result_titles = driver.find_elements_by_css_selector('.r a')
    for title in result_titles:
        print title.text
    time.sleep(5)
    

def search_to_yahoo(driver, keyword):
    """Display result of yahoo search and capture
    """
    # Access
    driver.get("http://www.yahoo.co.jp/")
    time.sleep(5)
    
    # Search
    search_box = driver.find_element_by_name('p')
    search_box.send_keys(keyword)
    search_box.submit()
    time.sleep(5)
    
    # Capture screenshot
    driver.save_screenshot("./yahoo_search_page.png")
        

def main():
    """
    """
    #driver = webdriver.Firefox()
    #driver = webdriver.Chrome("C:\work\chromedriver_win32\chromedriver.exe")
    
    # open Edge browser and crash. Maybe Edge driver dont support python.
    #driver = webdriver.Edge("C:\Program Files (x86)\Microsoft Web Driver\MicrosoftWebDriver.exe")
    
    # if you use IEdriver, change browser setting
    # Internet Option > Secutiry
    # All security zone "Enable Protected Mode" unchecked.
    # and change browser display magnification to "100%"
    driver = webdriver.Ie("C:\work\selenium-IEDriverServer\IEDriverServer.exe")


    driver.implicitly_wait(10)
    search_to_google(driver, u"日本語")
    search_to_yahoo(driver, u"ニュース")
    
    driver.quit()
    #driver.back()
    #driver.forward()


if __name__ == '__main__':
    main()