# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

class BeautyImagesSpiderMiddleware(object):

    def process_request(self, request, spider):
        '''设置headers和切换请求头'''
        # referer = request.url
        # if referer:
        #     request.headers['referer'] = referer
        pass
