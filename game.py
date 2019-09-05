import scrapy

class GameRecord(scrapy.Item):
    name1 = scrapy.Field()
    name2 = scrapy.Field()
    time = scrapy.Field()
    series = scrapy.Field()
    score1 = scrapy.Field()
    score2=scrapy.Field()
    last_updated = scrapy.Field(serializer=str)