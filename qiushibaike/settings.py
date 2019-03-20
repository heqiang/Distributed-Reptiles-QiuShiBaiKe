# -*- coding: utf-8 -*-

# Scrapy settings for qiushibaike project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qiushibaike'

SPIDER_MODULES = ['qiushibaike.spiders']
NEWSPIDER_MODULE = 'qiushibaike.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "max-age=0",
        "Cookie": "CAMPUS_CHECKED=0; JYERN=0.6521779221948236; CAMPUS_CHECKED=0; QS_ED=6; JYERN=0.26531747193075716; QS_GD=7; QS_TM=1; jyean=ZnkIgT1JW7dtwnfPBYUOaQMQ9EHw9Hrhs72JCf4tOTiBEDLIHPZF72BzqUmmVHNWAvt1xk4aizTajtIpfTvTrEE39lecGsS2bVqdUtacbOjnYA2_qVZSih0wl0Ao7Xe00; LF_Email=njxczx08@xyh.com; jy=34C4C600E19323AE7A3588D4651301956A3437AFB5608381E05974D4BC275FA19D4906C1AEFC7D6B868F1A2D306BA4CB38C39F61AB200E02C4A6E6C5F2E1F98D0DBDA7E364FF1E25FB83D488DADBAD62E34C4D6FCA3E4AC9D210FD33668A9E3668258E09AFEF7516B65E7FFEB527606F357ED5F7D5BA8F058BE2EAAE46A7E9403003873D2D71D7DFB3F3C856AD2FFF3AE152FC747C3A7365F0F303CA534515EC779046E472AC790853495CA08517EC6095A325835A7019E2906974067015501F864B8B9CBD1F6AF16CDC4B8BD248876DD343B4367C517BAB05B6701AD2E488A1C3E320B7AD676CFC15E219850E12EBAB82B63CC4ED9A740E8511C4EF3449BE09; jye_notice_show=1|2015/8/31 15:08:32|0|false; JYERN=0.39406700897961855; CAMPUS_CHECKED=0; jye_math_ques_s=0; jye_math_ques_d=0; jye_math_ques_t=1; jye_math_ques_0_q=070eac9c-ad95-44f1-909c-869dbb4c874a~803641a7-c36b-483b-9f8d-ac0a5522e3c3~; CNZZDATA2018550=cnzz_eid%3D484121901-1440586726-http%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1441002725; _cnzz_CV2018550=%E7%94%A8%E6%88%B7%E4%BB%98%E8%B4%B9%7C%E9%9D%9EVIP%E7%94%A8%E6%88%B7%7C1441006330746%26%E7%94%A8%E6%88%B7%E8%A7%92%E8%89%B2%7C%E8%80%81%E5%B8%88%7C14",
        "Host": "www.qiushibaike.com",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://www.qiushibaike.com/",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/40.0.2214.111 Chrome/40.0.2214.111 Safari/537.36"
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qiushibaike.middlewares.QiushibaikeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'qiushibaike.middlewares.customMiddlewares.CusetomUserAgent': 3,
    'scrapy.contrib.downloadmiddleware.useragent.UserAgentMiddleware': None,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'qiushibaike.pipelines.QiushibaikePipeline': 10,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
