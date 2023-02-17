import scrapy
from real_estate2.items import RealEstate2Item

class Listings2Spider(scrapy.Spider):
    name = "listings2"
    allowed_domains = ["arizonarealestate.com"]
    start_urls = [
        "https://www.arizonarealestate.com/maricopa/",
        "https://www.arizonarealestate.com/goodyear/",
        "https://www.arizonarealestate.com/gilbert/"
        ]

    def parse(self, response):
       gallary=response.xpath("//div[@class='si-listings-column']")
       print(len(gallary))
       for listing in gallary:
           item=RealEstate2Item()
           item['name']=listing.xpath(".//div[@class='si-listing__title-main']/text()").get()
           item['description']=listing.xpath(".//div[@class='si-listing__title-description']/text()").get()
           item['price']=listing.xpath(".//div[@class='si-listing__photo-price']/span/text()").get()
           item['agency']=listing.xpath(".//div[@class='si-listing__footer']//div/text()").get()
           yield item
