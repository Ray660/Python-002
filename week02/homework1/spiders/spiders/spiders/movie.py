import scrapy
from scrapy.selector import Selector
from spiders.items import MaoYanMovieItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self,response):
        print(response.url)
        print('..............................')

        movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        for movie in movies[:10]:
            link = movie.xpath('./a/@href').extract_first()

            yield scrapy.Request(url='https://maoyan.com'+link, callback=self.parse2, dont_filter=True)

    def parse2(self,response):
        #print(response.text)
        item = MaoYanMovieItem()
        movie = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        #电影名称
        moviename = movie.xpath('./h1/text()').extract_first()
        #print(moviename)
        #电影类型
        movietypes = movie.xpath('./ul/li[1]/a/text()').extract()
        movietype = ''
        for atype in movietypes:
            movietype = movietype + atype + ''
        #print(movietype)

        release_time = movie.xpath('./ul/li[3]/text()').extract_first()[0:9]
        #print(release_time)

        item['moviename'] = moviename
        item['movietype'] = movietype
        item['release_time'] = release_time

        yield item
