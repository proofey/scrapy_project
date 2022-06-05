import scrapy
from TASK_1.items import DeviceItem



class DeviceSpider(scrapy.Spider):
    name = 'devices'
    start_urls = [
        'https://gplay.bg/гейминг-периферия', #The starting point.Since we have
        'https://gplay.bg/гейминг-хардуер'    #interest in only these 2 categories
    ]

    def parse(self, response):
        for link in response.css('div.categories-grid-item a::attr(href)'):         #We start crawling deeper to reach
            yield response.follow(link.get(), callback=self.parse_subcategories)    #the subcategories


    def parse_subcategories(self, response):
        for link in response.css('div.catalog-container a::attr(href)'):            #We keep crawling deeper to reach
            yield response.follow(link.get(), callback=self.parse_product)          #the products in the subcategory

    
    def parse_product(self, response):                                                      #We end up in the individual post details page
        products = response.css('html')                                                     #and start scraping the data that we need
        price = round(float(response.css('.normal-price price').get().split('"')[1]), 2)
        in_stock = response.css('.fa.bg-success').get() or None
        for product in products:
            if int(price) < 200 and in_stock is not None:
                yield DeviceItem({                                                          #We yield back the data and use it to
                    'category': product.css('.path a::text')[1].get(),                      #instantiate our Item object
                    'subcategory': product.css('.path a::text')[2].get(),
                    'name': product.css('.large-title::text').get().strip(),
                    'subtitle': product.css('title::text').get().strip(),
                    'product_number': product.css('.product-ref-number strong::text').get(),
                    'price': round(float(response.css('.normal-price price').get().split('"')[1]), 2)
                })