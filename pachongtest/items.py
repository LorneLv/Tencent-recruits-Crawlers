# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PachongtestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    job_type = scrapy.Field()
    job_needpeople = scrapy.Field()
    job_address = scrapy.Field()
    job_date = scrapy.Field()

class BilibiliItem(scrapy.Item):
    voide_title = scrapy.Field()#视频标题
    voide_common = scrapy.Field()#视频详细内容
    voide_people = scrapy.Field()#视频作者
    voide_playnum = scrapy.Field()#视频播放数
    voide_httpaddress = scrapy.Field() #视频网页地址
    voide_remark = scrapy.Field()#视频评论数

