# learning-scrapy

# tutorial

## 1.使用scrapy框架,爬取了《一个》上的所有问题 (截止到 `2016-9-25 12:33:04`)

`start_time`  : 2016-9-25 12:33:04
`finish_time` : 2016-9-25 12:38:32

`有效数据`: 1452条

### 代码
```python
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
```
## 数据截图

![1](http://p1.bqimg.com/567571/5e8a46cba7e8196d.png)
