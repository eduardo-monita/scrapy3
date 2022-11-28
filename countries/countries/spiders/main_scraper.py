import scrapy
from countries.items import CountryItem

class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['scrapethissite.com']
    start_urls = ['https://www.scrapethissite.com/pages/simple/']

    def parse(self, response):
        coutries = response.xpath('//*[@class="col-md-4 country"]')
        for data in coutries:
            country = CountryItem()
            country["name"] = data.css("h3.country-name::text").getall()[1]
            country["capital"] = data.css("div.country-info span.country-capital::text").get()
            country["population"] = data.css("div.country-info span.country-population::text").get()
            country["area"] = data.css("div.country-info span.country-area::text").get()
            yield country
