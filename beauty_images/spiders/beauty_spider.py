import scrapy

from beauty_images.items import BeautyImagesItem


class beautySpider(scrapy.Spider):
    name = 'beauty_spider'
    allowed_domains = ["www.mm131.com"]
    start_urls = ['http://www.mm131.com/xinggan/'
                  # 'http://www.mm131.com/qingchun/',
                  # 'http://www.mm131.com/xiaohua/',
                  # 'http://www.mm131.com/chemo/',
                  # 'http://www.mm131.com/qipao/',
                  # 'http://www.mm131.com/mingxing/'
                  ]

    def parse(self, response):
        imgUrls = response.css(".list-left dd:not(.page)")
        for imgUrl in imgUrls:
            imageUrl = imgUrl.css("a::attr(href)").extract_first()
            next_url = response.css(".page-en:nth-last-child(2)::attr(href)").extract_first()
            if next_url is not None:
                # 下一页
                yield response.follow(next_url, callback=self.parse)
            yield scrapy.Request(imageUrl, callback=self.content)

    def content(self,response):
        item = BeautyImagesItem()  # 实例化item
        item['imageUrl'] = response.css(".content-pic img::attr(src)").extract()
        item['imageName'] = response.css(".content h5::text").extract_first()
        yield item

        # 提取图片,存入文件夹
        next_url = response.css(".page-ch:last-child::attr(href)").extract_first()
        print(next_url)
        if next_url is not None:
            # 下一页
            yield response.follow(next_url, callback=self.content)
