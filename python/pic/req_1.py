import urllib
import re
import ssl
import requests
import os
import random

from urllib.request import urlopen, Request

url = "http://www.baidu.com"
 
my_headers = ["Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"]

def get_content(url, headers):
    randdom_header = {'User-Agent':random.choice(headers)}
    print(randdom_header)
    print()
    
    req = Request(url, headers = randdom_header)
    print(req)
    print()

    content = urlopen(req).read().decode('utf-8')
    # return content.decode('utf-8')
    # print(content)
if __name__ =='__main__':
    get_content(url, my_headers)
 