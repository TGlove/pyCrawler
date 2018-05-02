# -*- coding: UTF-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup


class Parser():

    def parse(self, new_url, html_cont):
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

        new_urls = self.get_new_urls(soup, new_url)

        new_data = self.get_new_data(soup, new_url)

        return new_urls, new_data

    def get_new_urls(self, soup, new_url):
        new_urls = set()

        # /item/Guido%20van%20Rossum
        links = soup.find_all('a', href=re.compile(r'/item/'))
        for link in links:
            url = link['href']
            full_url = urlparse.urljoin(new_url, url)
            new_urls.add(full_url)

        return new_urls

    def get_new_data(self, soup, new_url):
        new_data = {}

        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        new_data['title'] = title
        # <div class="lemma-summary" label-module="lemmaSummary">
        content = soup.find('div', class_='lemma-summary')
        new_data['content'] = content
        new_data['url'] = new_url

        return new_data
