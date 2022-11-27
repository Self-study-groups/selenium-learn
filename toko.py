import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.bukalapak.com/products?search%5Bkeywords%5D=sepatu&search%5Bsort_by%5D=bestratingratio',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'Nama' : response.css('div.flex-wrap:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(1) > p:nth-child(1) > a:nth-child(1)::text').extract(),
            'Harga' : response.css('div.flex-wrap:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > p:nth-child(2)::text').extract(),
        }