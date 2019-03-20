from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware


class  CusetomUserAgent(UserAgentMiddleware):
        def process_request(self, request, spider):
            ua="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
            request.headers.setdefault('User-Agent',ua)