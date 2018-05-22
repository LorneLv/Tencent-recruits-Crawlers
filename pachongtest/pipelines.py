# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings
import  time
import json
# from  scrapy.contrib.exporter import BaseItemExporter
# # from  scrapy.contrib.exporter import JsonItemExporter
# class JsonItemExporter(BaseItemExporter):
#     exporter = MyJsonExporter(fi, encoding='utf-8')
class PachongtestPipeline(object):

    def __init__(self):
        settings = get_project_settings()
        dbparams ={
            'host':settings['MYSQL_HOST'],
            'db':settings['MYSQL_DBNAME'],
            'user':settings['MYSQL_USER'],
            'passwd': settings['MYSQL_PASSWD'],
            'port': settings['MYSQL_PORT'],
            'charset': 'utf8',
            'cursorclass':MySQLdb.cursors.DictCursor,
            'use_unicode': False,
        }
        dbpool = adbapi.ConnectionPool('MySQLdb',**dbparams)
        self.dbpool = dbpool
    def process_item(self, item, spider):
        sql = "insert into tencenthrlist(job_name,job_type,job_needpeople,job_address,job_date) values(%s,%s,%s,%s,%s)"
        query=self.dbpool.runInteraction(self._conditional_insert,sql,item)
        query.addErrback(self._handle_error)
        return item

    def _conditional_insert(self, tx,sql, item):

        # print item['name']
        # items = item['job_date']
        # item['job_date'] = ('%s-%s-%s 05:06:41'%(items[0:4],items[6:8],items[8:]))
        params = (item["job_name"], item["job_type"],item["job_needpeople"],item["job_address"],item["job_date"])
        tx.execute(sql, params)



    def _handle_error(self, failue):
        print('------------------11111---------------------')
        print failue