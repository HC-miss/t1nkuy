# import time
# import datetime as dt
#
# # list = re.findall(r'"([A-Z]+?)"', response.text)
# url = 'https://booking.airasia.com/Flight/Select?o1={start}&d1={end}&dd1={date}&culture=zh-CN&r=true&ADT=2&CHD=0&inl=0&mon=true'
# for i in range(10):
#     for j in range(10):
#         # print(response.meta['arrive'], i, j)
#         print(type(time))
#         select_time = dt.datetime.now() + dt.timedelta(days=j)
#         timeStamp = int(time.mktime(select_time.timetuple()))
#         time = select_time.strftime("%Y-%m-%d")
#         # new_url = url.format(start=response.meta['arrive'], end=i, date=time)
#         new_url = url.format(start='abc', end=i, date=time)
#         print(new_url)
#         # yield scrapy.Request(url=new_url, dont_filter=True, callback=self.next2)
from html import unescape
print(unescape('&#243;'))
