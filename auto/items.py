# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    mileage = scrapy.Field()
    exterior = scrapy.Field()
    interior = scrapy.Field()
    color = scrapy.Field()
    car_type = scrapy.Field()
    body_style = scrapy.Field()
    fuel_type = scrapy.Field()
    stock = scrapy.Field()
    vin = scrapy.Field()
    engine = scrapy.Field()
    transmission = scrapy.Field()
    drivetrain = scrapy.Field()
    doors = scrapy.Field()
    title = scrapy.Field()
    dealer = scrapy.Field()
    dealer_url = scrapy.Field()
    phone = scrapy.Field()
    images = scrapy.Field()
    city_mpg = scrapy.Field()
    highway_mpg = scrapy.Field()
    url = scrapy.Field()
