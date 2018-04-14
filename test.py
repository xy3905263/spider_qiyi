#coding:utf-8
from bs4 import BeautifulSoup
import requests

#获取电视剧列表页各电视剧单独链接
url = "http://www.iqiyi.com/a_19rrgynilx.html"
data = requests.get(url)
soup = BeautifulSoup(data.text,"lxml")

dsj_d_links = soup.select('.site-piclist_info_describe a')
for dsj_d_link in dsj_d_links:
	dsj_d_link_href = dsj_d_link.get('href')
	print dsj_d_link_href
