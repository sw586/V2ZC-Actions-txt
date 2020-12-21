# 最速度注册
#发送post请求，模拟浏览器的登录最云会员中心1
# 组件安装：
# pip install requests
# pip install beautifulsoup4
# pip install requests_html
#!/usr/bin/python
#coding=utf-8
import requests
import re
from bs4 import BeautifulSoup
import random
import string


#访问订阅跳转链接
r=requests.get('http://sw.qiji.pw/i2.php',headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}, )
print (r.text)

# 打开一个txt文件将V2订阅内容写入i.txt文件
fo = open("i2.txt", "w")
fo.write(r.text)
# 关闭打开的文件
fo.close()
