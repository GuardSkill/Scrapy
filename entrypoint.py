from scrapy import cmdline


# cmdline.execute(['scrapy','runspider','basic.py'])

# cmdline.execute(['scrapy','runspider','basic.py','-s','CLOSESPIDER_ITEMCOUNT=90'])

cmdline.execute(['scrapy','runspider','basic.py','-o','data.json','-s','FEED_EXPORT_ENCODING=utf-8'])

# scrapy runspider basic.py -o data.json -s FEED_EXPORT_ENCODING=utf-8