# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#import pandas as pd
import pymysql
from spiders.settings import DATABASES

class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        moviename = item['moviename']
        movietype = item['movietype']
        release_time = item['release_time']
        #list = [moviename,movietype,release_time]
        print(type(moviename),type(movietype),type(release_time))

        #建立连接
        db = pymysql.connect(host=DATABASES['host'], user=DATABASES['user'], password=DATABASES['password'], port=DATABASES['port'],db=DATABASES['db'],charset=DATABASES['charset'])
        #建立游标
        cursor = db.cursor()
        #创建数据表
        sql = 'CREATE TABLE IF NOT EXISTS maoyanmovie ( moviename VARCHAR(255) NOT NULL, movietype VARCHAR(255) NOT NULL, release_time VARCHAR(255) NOT NULL, PRIMARY KEY (moviename)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4'
        cursor.execute(sql)
        #插入数据
        sql = "INSERT INTO maoyanmovie (moviename, movietype, release_time) values(%s, %s, %s)"
        try:
            cursor.execute(sql, (moviename, movietype, release_time))
            db.commit()
            print('插入数据成功')
            # 关闭游标
            cursor.close()
            db.commit()
        except:
            print('数据插入失败')
            db.rollback()

        # 关闭数据库连接
        db.close()

        return item
