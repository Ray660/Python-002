import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd

#获取首页全部网页信息
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40'
cookiesss = '__mta=209133101.1595572897212.1595682598723.1595682611049.8; uuid_n_v=v1; uuid=B7D09050CD7811EABF7AA517BC081B30641FD80B858B484689141CB728FD5F0F; mojo-uuid=955b6044c7c909073dd1e2c9068d6773; _lxsdk_cuid=1737f8e458630-0f7dd60fdd5586-5d37194f-e1000-1737f8e4587c8; _lxsdk=B7D09050CD7811EABF7AA517BC081B30641FD80B858B484689141CB728FD5F0F; _csrf=2e63d6d67fac241ca51f1b328363a8eb304d7240c5a0a7064a67b70400c6ed28; mojo-session-id={"id":"ea159b1ab3f95d1b8eb82f1e40d1238e","time":1595690095243}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595572897,1595681842,1595690387; mojo-trace-id=4; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595690623; __mta=209133101.1595572897212.1595682611049.1595690623183.9; _lxsdk_s=173868a9234-16c-5fa-962%7C%7C7'
header = {'user-agent':user_agent,'Cookie':cookiesss}


#print(response.text)


#获取页面详细信息

def pages_details(url):

    father_page = requests.get(url , headers = header)
    print('获取首页信息状态码：', father_page.status_code)

    bs_fg = bs(father_page.text,'html.parser')
    mylist = []
    for tags in bs_fg.find_all('div', attrs={'class': 'movie-item film-channel'},limit=10):
        tag = tags.find_all('a')[0]
        apage = tag.get('href')

        #进入子页面，并获取页面内容
        page = requests.get('https://maoyan.com' + apage,headers=header)

        selector = lxml.etree.HTML(page.text)
        #电影名字
        moviename = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
        #电影类型
        bs_page = bs(page.text,'html.parser')
        types = bs_page.find_all('a',attrs={'class':'text-link'})
        movietype = ''
        for type in types:
            atype = type.get_text()
            movietype = movietype + atype + ''
        #上映时间
        times = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')

        list = [moviename,movietype,times]


        mylist.append(list)
    #print(mylist)
    #创建csv文件
    movie = pd.DataFrame(data = mylist,columns = ['moviename','movietype','release_time'])
    #print(movie1)
    #movie1 = pd.DataFrame(data = mylist, index = [moviename,movietype,times])
    movie.to_csv('./movie.csv', encoding='gbk', index=False)

pages_details('https://maoyan.com/films?showType=3')
