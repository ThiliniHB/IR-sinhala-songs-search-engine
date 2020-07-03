# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LyricsItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()
    lyricist = scrapy.Field()
    musicComposer = scrapy.Field()
    genre = scrapy.Field()
    views = scrapy.Field()
    shares = scrapy.Field()
    lyrics = scrapy.Field()
