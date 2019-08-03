# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl
from tutspluscrawl import settings

def write_to_xl(item):
    #    writer = csv.writer(open(settings.csv_file_path, 'a'), lineterminator='\n')
    #    writer.writerow([item[key] for key in item.keys()])
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'Sheet1'
    
    wb.save('')

class tutsplusxlPipeline(object):
    def process_item(self, item, spider):
        return item
