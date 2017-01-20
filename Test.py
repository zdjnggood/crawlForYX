# import time
# from selenium import webdriver
# from selenium.common.exceptions import StaleElementReferenceException
#
#
# def waitForLoad(driver):
#     elem = driver.find_element_by_tag_name("html")
#     count = 0
#
#     while True:
#         print count
#         count += 1
#         if count > 4:
#             print("Timing out after 10 seconds and returning")
#             return
#         time.sleep(0.5)
#         try:
#             elem == driver.find_element_by_tag_name("html")
#         except StaleElementReferenceException:
#             return
#
# base_url = "http://you.163.com"
# url = "http://you.163.com/item/list?categoryId=1005000&_stat_area=nav_2&_stat_referer=index"
# driver = webdriver.PhantomJS(executable_path='/Users/zzr/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
# driver.get(url)
# waitForLoad(driver)
#
# content = driver.find_elements_by_class_name("m-content")
# print "type(content): ",type(content)
#
# for item_content in content:
#     print "type(item_content): ", type(item_content)
#     class_list = item_content.find_elements_by_class_name("m-itemList")
#     print "type(itemList): ", type(class_list)
#     for item_of_class_list in  class_list:
#         #print "------------------"
#         #print class_of_items_list.text
#         items_list = item_of_class_list.find_elements_by_class_name("item")
#         for item_of_items_list in items_list:
#             # print "\n"*2
#             # print "-"*25
#             # print item_of_items_list.text
#             photo = item_of_items_list.find_element_by_xpath("./div/div[@class='hd']")
#             info_url = photo.find_element_by_xpath("./a").get_attribute("href")
#             info_photo_url = photo.find_element_by_xpath("./a/img").get_attribute("src")
#             detail = item_of_items_list.find_element_by_xpath("./div/div[@class='bd']")
#             info_name = detail.find_element_by_xpath("./h4").text
#             info_price = detail.find_element_by_xpath("./p").text
#             info_description = detail.find_element_by_xpath("./div").text
#
#             print  "-*"*25
#             print "info_url",info_url
#             print "info_photo_url", info_photo_url
#             print "info_name", info_name
#             print "info_price", info_price
#             print "info_description", info_description
#
#
#
#
#
#     # for item_itemList in itemList:
#     #     product = item_itemList.find_elements_by_class_name("m-product j-product product-s")
#     #     for item_product in product:
#     #         #driver.find_element_by_css_selector("a[title=\"web\"]").click()
#     #         total_info = item_product.find_element_by_css_selector("/div")
#     #         print  total_info