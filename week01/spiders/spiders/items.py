# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoYanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    moviename = scrapy.Field()
    movietype = scrapy.Field()
    release_time = scrapy.Field()
