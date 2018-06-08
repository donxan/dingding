
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: aiker@gdedu.ml
# My blog http://m51cto.51cto.blog.com 
import requests
import re
import urllib2
import json
import sys
import os
  
headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=37e23308d1b84eb4ac3xxxxxxxxxx02e6305bab9d4068c333"
  
def msg(text):
    json_text= {
     "msgtype": "text",
        "at": {
            "atMobiles": [
                "1xxxxxxxxx"
            ],
            "isAtAll": False
        },
        "text": {
            "content": text
        }
    }
    print requests.post(api_url,json.dumps(json_text),headers=headers).content
      

hearders = "User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"

url = "https://tianqi.moji.com/weather/china/guangdong/shenzhen" 
par = '(<meta name="description" content=")(.*?)(">)'

opener = urllib2.build_opener()
opener.addheaders = [hearders]
urllib2.install_opener(opener)

html = urllib2.urlopen(url).read().decode("utf-8")

data = re.search(par,html).group(2)
msg(data)

