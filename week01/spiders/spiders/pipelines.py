# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#import pandas as pd


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        moviename = item['moviename']
        movietype = item['movietype']
        release_time = item['release_time']
        #list = [moviename,movietype,release_time]
        
        #output = pd.DataFrame(data=list)
        output = f'{moviename},{movietype},{release_time}\n'

        with open('./maoyanmovie.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
