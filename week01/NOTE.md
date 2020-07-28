学习笔记
四个步骤：
	1. 新建项目:新建爬虫以及设置settings.py
	2. 明确目标：编写items.py
	3. 制作爬虫：编写spiders/xxspider.py
	4. 存储内容：编写pipelines.py


新建项目:新建爬虫以及设置settings.py
	新建爬虫：
	在自定义目录中输入：
	scrapy startproject mySpider  (mySpider为项目名称，就是那个文件夹的名字)
	文件夹内容：
	mySpider/
		scrapy.cfg
		mySpider/
			__init__.py
			items.py
			pipelines.py
			settings.py
			spiders/
				__init__.py
				(爬虫放在这个地方)
	设置settings.py：
	
	USER_AGENT_LIST=[
	'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
	    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
	    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
	    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40"
	]
	import random
	USER_AGENT = random.choice(USER_AGENT_LIST)
	
	DOWNLOAD_DELAY = 3
	
	ITEM_PIPELINES = {
	    'spiders.pipelines.MaoyanmoviePipeline（注意pipeline的名称要和自己设置的相同）': 300,
	}
	
明确目标：编写items.py
	import scrapy
	
	class MaoYanMovieItem(scrapy.Item):
	    moviename = scrapy.Field()
	    movietype = scrapy.Field()
	    release_time = scrapy.Field()
	需要爬取什么，就设置什么
	
制作爬虫：编写spiders/xxspider.py
	在mySpider/spider目录下创建：
	scrapy genspider  movie(爬虫名称)  "maoyan.com"(限制域名)
	
	修改默认代码：
	import scrapy
	
	class DoubanSpider(scrapy.Spider):
	    # 定义爬虫名称
	    name = 'douban'
	    allowed_domains = ['movie.douban.com']  （就是限制域名，爬取范围不会超过该域名）
	    # 起始URL列表
	    start_urls = ['https://movie.douban.com/top250'] （第一个网页）
	
	   def parse(self, response):
	        pass
	
	一些要注意的代码：
	yield scrapy.Request(url=url, callback=self.parse（callback 回调函数，引擎会将下载好的页面(Response对象)发给该方法，执行数据解析这里可以使用callback指定新的函数，不是用parse作为默认的回调参数，就是可以从这运行下一个函数，很有用）, dont_filter=False（当这为True时，可以不受限制域名影响）)
	（这之后就有response了）
	
	from scrapy.selector import Selector   （要使用xpath）
	movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
	
	moviename = movie.xpath('./h1/text()').extract_first()
	
存储内容：编写pipelines.py
	output = f'{moviename},{movietype},{release_time}\n'
	        with open('./maoyanmovie.csv', 'a+', encoding='utf-8') as article:
            article.write(output)   （write只能适用于str类型）