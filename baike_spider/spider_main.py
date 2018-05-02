# -*- coding: UTF-8 -*-
import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManeger()
        self.downloader = html_downloader.Downloader()
        self.parser = html_parser.Parser()
        self.outputer = html_outputer.Outputer()

    def craw(self, root_url):
        count = 1
        # 添加目标url
        self.urls.add_new_url(root_url)
        # 循环，判断是否有新的待爬取得url
        while self.urls.has_new_url():
            try:
                # 得到新的待爬取得url
                new_url = self.urls.get_new_url()
                print 'count = %d ,%s' % (count, new_url)

                # 下载网页存到html_cont，此为数据
                html_cont = self.downloader.download(new_url)

                # 解析网页，得到新的url列表和新的数据
                new_urls, url_data = self.parser.parse(new_url, html_cont)

                # 批量添加新的url
                self.urls.add_new_urls(new_urls)

                # 收集数据
                self.outputer.collect_data(url_data)

                count += 1
                if count == 100:
                    break
            except:
                print 'craw fail'

        self.outputer.HTML_outputer()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
