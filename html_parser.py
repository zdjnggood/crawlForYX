# coding:utf8


import time

from selenium.common.exceptions import StaleElementReferenceException



class HtmlParser(object):
    def parse(self, page_url, driver):
        print "_"*25
        print "downloading: ",page_url

        if  page_url is None or driver is None:
            return

        # soup = BeautifulSoup(html_cont,"html.parser",from_encoding='utf-8')
        new_urls = self._get_new_urls(driver)
        new_data = self._get_new_data(driver)
        
        return new_urls,new_data





    def _get_new_urls(self,  driver):
        new_urls = set()
        nav = driver.find_element_by_class_name("tab-nav")
        nav_urls = nav.find_elements_by_class_name("j-nav-item")
        #print "len of url:",len(nav_urls)
        for item_url in nav_urls:
            print "class",item_url.get_attribute("class")
            try:
                url = item_url.find_element_by_xpath("./a").get_attribute("href")
            except:
                continue
            new_urls.add(url)
        #print "new_urls: ",new_urls
        return new_urls


        # driver.find_element_by_id("kw")
        # driver.find_element_by_name("wd")
        # driver.find_element_by_tag_name("input")
        # driver.find_element_by_class_name("s_ipt")
        # driver.find_element_by_css_selector("#kw")
        # driver.find_element_by_xpath("//input[@id='kw']")
        # driver.quit()

        # links = soup.find_all('a',href = re.compile(r"/view/\d+\.htm"))
        # for link in links:
        #     new_url = link['href']
        #     new_full_url = urlparse.urljoin(page_url,new_url)
        #     new_urls.add(new_full_url)
        # return new_urls

    def _get_new_data(self,  driver):
        res_data = {}
        # driver = webdriver.PhantomJS(executable_path='/Users/zzr/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
        # waitForLoad(driver)

        content = driver.find_elements_by_class_name("m-content")
        # print "type(content): ", type(content)

        for item_content in content:
            # print "type(item_content): ", type(item_content)
            class_list = item_content.find_elements_by_class_name("m-itemList")
            # print "type(itemList): ", type(class_list)
            for item_of_class_list in class_list:
                # print "------------------"
                # print class_of_items_list.text
                items_list = item_of_class_list.find_elements_by_class_name("item")
                for item_of_items_list in items_list:
                    # print "\n"*2
                    # print "-"*25
                    # print item_of_items_list.text
                    photo = item_of_items_list.find_element_by_xpath("./div/div[@class='hd']")
                    info_url = photo.find_element_by_xpath("./a").get_attribute("href")
                    info_photo_url = photo.find_element_by_xpath("./a/img").get_attribute("src")
                    detail = item_of_items_list.find_element_by_xpath("./div/div[@class='bd']")
                    info_name = detail.find_element_by_xpath("./h4").text
                    info_price = detail.find_element_by_xpath("./p").text
                    info_description = detail.find_element_by_xpath("./div").text

                    # print  "-*" * 25
                    # print "info_url", info_url
                    # print "info_photo_url", info_photo_url
                    # print "info_name", info_name
                    # print "info_price", info_price
                    # print "info_description", info_description
                    res_data["info_url"] = info_url
                    res_data["info_photo_url"] = info_photo_url
                    res_data["info_name"] = info_name
                    res_data["info_price"] = info_price
                    res_data["info_description"] = info_description

                    fout = open('output.html', 'a')

                    fout.write("<html>")
                    fout.write("<body>")
                    fout.write("<table>")

                    # res_data["info_url"] = info_url
                    # res_data["info_photo_url"] = info_photo_url
                    # res_data["info_name"] = info_name
                    # res_data["info_price"] = info_price
                    # res_data["info_description"] = info_description


                    fout.write("</tr>")
                    fout.write("<td>%s</td>" % (res_data['info_url']).encode('utf-8'))
                    # fout.write("<td>%s</td>" % (data['info_photo_url']).encode('utf-8'))
                    fout.write("<td>%s</td>" % (res_data['info_name']).encode('utf-8'))
                    fout.write("<td>%s</td>" % (res_data['info_price']).encode('utf-8'))
                    fout.write("<td>%s</td>" % (res_data['info_description']).encode('utf-8'))
                    # fout.write("<td>%s</td>"%(data['url']))
                    # fout.write("<td>%s</td>" % (data['title']).encode('utf-8'))
                    # fout.write("<td>%s</td>" % (data['summary']).encode('utf-8'))
                    fout.write("</tr>")
                    fout.write("</tr>")
                    fout.write("</tr>")

                    fout.write("</table>")
                    fout.write("</body>")
                    fout.write("</html>")

        return res_data
        # res_data = {}
        #
        # res_data["url"] = page_url
        #
        # title_node = soup.find('dd',class_= "lemmaWgt-lemmaTitle-title").find("h1")
        # res_data['title'] = title_node.get_text()
        #
        # summary_node = soup.find('div',class_="lemma-summary")
        # res_data["summary"] = summary_node.get_text()
        #
        # return  res_data