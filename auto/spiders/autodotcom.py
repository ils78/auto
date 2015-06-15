# -*- coding: utf-8 -*-
import scrapy
from auto.items import AutoItem
import re
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc


class AutodotcomSpider(scrapy.Spider):
    name = "autodotcom"
    allowed_domains = ["auto.com"]
    start_urls = (
        'http://chicago-il.auto.com/cars-for-sale/ford-mustang?&page=1',
    )

    def parse(self, response):
        for car in response.xpath('//li[@class="car"]'):
            item = AutoItem()
            item['price'] = ''.join(car.xpath('a/div[@class="price"]/text()').extract()).strip()
            item['title'] = ' '.join(car.xpath('div/a[@class="car_title"]/span/text()').extract()).strip()
            keys = car.xpath('div/a/div/div[@class="tile_key"]/text()').extract()
            values = car.xpath('div/a/div/div[@class="tile_data"]/text()').extract()
            for key, value in zip(keys, values):
                key = re.sub(r'\s+', '_', key.lower())
                key = re.sub(r':$', '', key)
                item[key] = value
            item['phone'] = ' '.join(car.xpath('div/div/address/div/span[@class="phone"]/text()').extract()).strip()
            item['dealer'] = ' '.join(car.xpath('div/div/address/div/a[@data-dtm-linkname="dealer-name"]/text()').extract()).strip()
            item['dealer_url'] = ' '.join(car.xpath('div/div/address/div/a[@data-dtm-linkname="dealer-name"]/@href').extract()).strip()
            item['url'] = car.xpath('a[@class="summary"]/@href').extract()
            yield item

        last_page_url = response.xpath('//div[@class="pagination"]/div[@class="pages"]/a[@class="next_page"]/preceding-sibling::a/@href').extract()
        if len(last_page_url) > 0:
            last_page_url = last_page_url[-1]
            m = re.match(r'^(.+&page=)(\d+)$', last_page_url)
            if m:
                last_page_index = int(m.group(2))
                base_url = get_base_url(response)
                for page_index in xrange(2, last_page_index + 1):
                    url = urljoin_rfc(base_url, '{0}{1}'.format(m.group(1), page_index))
                    yield scrapy.Request(url)



