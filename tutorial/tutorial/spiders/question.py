import scrapy

class QuestionSpider(scrapy.Spider):
    name = 'question'

    start_urls = ['http://wufazhuce.com/question/8',]

    def parse(self,response):
        try:
            title = response.css('div h4::text').extract_first().strip().encode('utf-8')
            detail = response.css('div.cuestion-contenido::text')[0].extract().strip().encode('utf-8')
            answer =  response.css('div.cuestion-contenido::text')[1].extract().strip().encode('utf-8')

            yield {
                'title': title,
                'detail': detail,
                'answer': answer,
            }
        except:
            pass

        for i in range(9,1500):
            next_page = response.urljoin(str(i))
            yield scrapy.Request(next_page, callback=self.parse)
