# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import urllib3
import os

class QiushibaikePipeline(object):
    def process_item(self, item, spider):
        today=time.strftime('%Y%m%d',time.localtime())
        fileName=today+'qiubai.txt'

        with open(fileName,'a') as fp:
            fp.write("作者:%s"%(item["author"]+'\t'))
            fp.write("评论内容:%s"%(item["content"]+'\t'))
            fp.write("搞笑指数:%s"%(item["fullName"]+'\t'))
            fp.write("评论数：%s"%(item['sum_comment']+'\n'))

        return item
