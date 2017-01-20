# coding:utf8
import urllib2
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return



        def waitForLoad(driver):
            elem = driver.find_element_by_tag_name("html")
            count = 0

            while True:
                print count
                count += 1
                if count > 4:
                    print("Timing out after 10 seconds and returning")
                    return
                time.sleep(0.5)
                try:
                    elem == driver.find_element_by_tag_name("html")
                except StaleElementReferenceException:
                    return


        driver = webdriver.PhantomJS(executable_path='/Users/zzr/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
        driver.get(url)
        waitForLoad(driver)

        return driver


        # print(driver.page_source)


        # driver = webdriver.PhantomJS(executable_path='/Users/zzr/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
        # driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
        # try:
        #     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
        # finally:
        #     print(driver.find_element_by_id("content").text)
        # driver.close()


        # import time
        # driver = webdriver.PhantomJS(executable_path='/Users/zzr/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
        # driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
        # time.sleep(1)
        # print(driver.find_element_by_id('content').text)
        # driver.close()



        # auth = HTTPBasicAuth('ryan', 'password')
        # r = requests.post(url="http://pythonscraping.com/pages/auth/login.php", auth=auth)
        # print(r.text)

        # session = requests.Session()
        # params = {'username': 'username', 'password': 'password'}
        # s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
        # print("Cookie is set to:")
        # print(s.cookies.get_dict())
        # print("-----------")
        # print("Going to profile page...")
        # s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
        # print(s.text)




        # params = {'username': 'Ryan', 'password': 'password'}
        # r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
        # print("Cookie is set to:")
        # print(r.cookies.get_dict())
        # print("-----------")
        # print("Going to profile page...")
        # r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",cookies=r.cookies)
        # print(r.text)








        # response = urllib2.urlopen(url)
        # print "---",(response.read())
        #
        # params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
        # r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
        # print(r.text)
        # return r




        # if url is None:
        #     return  None
        #
        # response = urllib2.urlopen(url)
        #
        # if response.getcode() != 200:
        #     return None
        # else:
        #     return  response.read()
