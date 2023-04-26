# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QqmusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_star = scrapy.Field()
    sing_name = scrapy.Field()
    attention = scrapy.Field()
    sing_href = scrapy.Field()
    sing_id = scrapy.Field()

    pass
