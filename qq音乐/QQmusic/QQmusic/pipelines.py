# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QqmusicPipeline:
    def process_item(self, item, spider):
        d = dict(item)
        with open('news.csv', 'a', encoding='utf-8') as f:
            f.write(d['name_star'] + ',' + d['sing_name']+ ',' + d['attention']+ ',' + d['sing_href']+ ',' + d['sing_id'])
            f.write('\n')
        return item
