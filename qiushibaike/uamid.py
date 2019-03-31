import  random
from .settings import MY_USER_AGENT
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class Uamid(UserAgentMiddleware):
     #初始化 必须加User_agent
     def __init__(self,user_agent=""):
         self.user_agent=user_agent
     #请求处理
     def process_request(self, request, spider):
         #随机选择代理
         thisua=random.choice(MY_USER_AGENT)
         print("当前User_Agent是："+thisua)
         request.headers.setdefault('User-Agent',thisua)
