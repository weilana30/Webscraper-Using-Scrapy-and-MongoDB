# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
print(scrapy.__doc__)


class BooksItem(scrapy.Item):
   _id = scrapy.Field()
   url = scrapy.Field()
   title = scrapy.Field()
   price = scrapy.Field()
