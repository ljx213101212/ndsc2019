import scrapy
from tutorial.utils.helper import *

##This spider is for Ebay mobile only.
class MobilesSpider(scrapy.Spider):
    name = "mobiles"
    trans_table = {ord(c): None for c in u'\r\n\t'}
    accLabels = ["Brand","Network Technology", "Model", "Processor","Style","Storage Capacity","Manufacturer Color"
    "Color","Memory Card Type", "Network","Camera Resolution","Screen Size"]
    
    def start_requests(self):
        urls = [
            'https://www.ebay.com/itm/Excellent-Samsung-Galaxy-S8-Plus-G955U-64-GB-Orchid-Gray-Verizon-GSM-Unlocked-/163407137164?hash=item260bd3098c',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #/tr/td[contains(@width,"50%")/text()]
        items = response.xpath("//div[@class='itemAttr']/*/table/tr/td")
        for item in items:
            # label = item.xpath("//td[@class='attrLabels']/text()").get()
            itemTexts = item.xpath("text()").getall()
            for itemText in itemTexts:
                clean = getEnglishSentenseOnly(itemText)
                if clean and clean.upper() in (name.upper() for name in self.accLabels):
                    print(clean)
            
        # yield{
        #     'Brand': attribute.xpath("//tr/following-sibling::td[@class='attrLabels' and contains(.//test(),'Brand')]/td[contains(@width,'50%')/text()]").get(),
        # }