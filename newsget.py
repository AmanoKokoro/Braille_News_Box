#!/usr/bin/env python3
import json

from newsapi import NewsApiClient


class NewsGet:

    #initialize
    def __init__(self):
        self.newsapi = NewsApiClient(
            api_key='Your API Key')
        self.sources = self.newsapi.get_sources(language='en')

    #news_data get
    def headline_get(self, headline_num):
        headline_news = self.sources['sources'][headline_num]['description']
        self.newsdata = list(headline_news)
        #print('NewsGet', self.newsdata)
        return self.newsdata

    #news data re_get
    def refresh(self):
        self.sources = self.newsapi.get_sources(language='en')





if __name__ == '__main__':
    n = NewsGet()

    print(n.headline_get(0))
    print(n.headline_get(1))
    print(n.headline_get(2))
    print(n.headline_get(3))
    print(n.headline_get(4))
    print(n.headline_get(5))
    print(n.headline_get(6))
    print(n.headline_get(7))
