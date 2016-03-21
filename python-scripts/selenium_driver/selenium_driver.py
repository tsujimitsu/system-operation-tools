# -*- coding: utf-8 -*-
# 
# 

from selenium import webdriver


def main():
    """
    """
    driver = webdriver.Ie("C:\work\selenium-IEDriverServer\IEDriverServer.exe")
    driver.implicitly_wait(10)
    driver.get("https://google.com/")


if __name__ == '__main__':
    main()