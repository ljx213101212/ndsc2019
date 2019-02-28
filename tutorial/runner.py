from scrapy.cmdline import execute


SPIDER_NAME = "mobiles"

try:
    # execute(
    #     [
    #         'scrapy',
    #         'crawl',
    #         SPIDER_NAME,
    #         '-o',
    #         SPIDER_NAME + '.json',
    #     ]
    # )
    # execute(['scrapy','runspider', 'C://Work/sourceCodeTest/ndsc2019/ndsc2019/tutorial/tutorial/spiders/quotes_spider.py'])
    execute(['scrapy','runspider', 'C://Work/sourceCodeTest/ndsc2019/ndsc2019/tutorial/tutorial/spiders/'+SPIDER_NAME+'_spider.py'])
except SystemExit:
    pass