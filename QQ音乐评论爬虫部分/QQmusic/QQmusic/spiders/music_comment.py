import scrapy
import parsel,re,requests

from ..items import QqmusicItem


class MusicCommentSpider(scrapy.Spider):
    name = 'music_comment'
    allowed_domains = ['y.qq.com']
    start_urls = ['https://y.qq.com/n/ryqq/singer_list']

    def parse(self, response):
        lis = response.css('.singer_list_txt li')
        for li in lis:
            name_star = li.css('a::text').get()
            href = li.css('a::attr(href)').get()
            href = 'https://y.qq.com' + href  # 有评论页面的链接
            singer_res = requests.get(href).text
            sing_id_list = re.findall('.*?,"id":(\d\d\d\d+),"isonly"', singer_res, re.S)
            sing_html = parsel.Selector(singer_res)
            lis = sing_html.css('.songlist__list li')
            num = 0
            for li in lis:
                sing_name = li.css('.songlist__songname_txt a::text').get()
                sing_href = 'https://y.qq.com' + li.css('.songlist__songname_txt a::attr(href)').get()
                attention = sing_html.css('.data__cont .data__actions .mod_btn span::text').get()
                sing_id = sing_id_list[num]
                num+=1
                yield QqmusicItem(name_star=name_star,sing_name=sing_name,attention=attention,sing_href=sing_href,sing_id=sing_id)
        pass
