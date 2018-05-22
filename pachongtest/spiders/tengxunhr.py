# -*- coding: utf-8 -*-
import scrapy
import re
from  pachongtest import  items
import time
class TaengXunTeacher(scrapy.Spider):
    name = "pachongtest"
    allowd_domains = ["http://hr.tencent.com/"]
    start_urls = []
    start_num =raw_input("1.Please input you want spider start  page: ")
    end_num = raw_input("2.Please input you want spider end page: ")
    for  i in range(int(start_num),int(end_num)+1):
         page = (i-1)*10
         url ="https://hr.tencent.com/position.php?&start=%s"%page
         start_urls.append(url)
    def parse(self,response):
        job_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        print(job_list)
        for j  in  job_list:
            Tencent = items.PachongtestItem()
            jobName = j.xpath('./td[normalize-space(@class)="l square"]/a/text()').extract()
            # jobName = re.sub(r"[|]", " ",jobName);
            jobType =  j.xpath('./td/text()')[0].extract()
            peopleNum = j.xpath('./td/text()')[1].extract()
            addr = j.xpath('./td/text()')[2].extract()
            time = j.xpath('./td/text()')[3].extract()
            for  a,b in  zip(jobName,peopleNum,):
                Tencent["job_name"] = a
                Tencent["job_needpeople"] = b
            Tencent["job_type"] = jobType
            Tencent["job_address"] = addr
            Tencent["job_date"] = time
            # Tencent = json.dumps(dict(Tencent), ensure_ascii=False) + "\n"
            # Tencent = unicode.encode(str, 'utf-8');
            #     print(a.encode('utf-8'),b.encode('utf-8'),c.encode('utf-8'),d.encode('utf-8'),f.encode('utf-8') )
            # break

            yield Tencent



