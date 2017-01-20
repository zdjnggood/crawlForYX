# coding:utf8
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.Urlmanager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url,pages):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s '%(count,new_url)
                html_driver = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_driver)
                self.urls.add_new_urls(new_urls)
                #self.outputer.collect_data(new_data)

                if count == pages:
                    break

                count = count + 1
            except Exception,e:
                print 'craw failed:',e

        #self.outputer.output_html()

if __name__=="__main__":
    root_url = "http://you.163.com/item/list?categoryId=1005000"
    pages = 2000   #要爬的页数
    obj_spider = SpiderMain()
    obj_spider.craw(root_url,pages)