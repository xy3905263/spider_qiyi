#coding:utf-8
from bs4 import BeautifulSoup
import requests
import MySQLdb

print('连接到mysql服务器...')
db = MySQLdb.connect(host="192.186.3.70",user="pachong_test",passwd="3905263qqq!@#",db="pachong_test",charset="utf8")
print('连接上了!')

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS COLOR_NEW")

sql = """CREATE TABLE COLOR_NEW (
        Color VARCHAR(255) COLLATE utf8_bin NOT NULL,
        Value VARCHAR(255) COLLATE utf8_bin,
        Style mediumtext COLLATE utf8_bin)"""

cursor.execute(sql)

#获取电视剧列表页各电视剧单独链接
url = "http://list.iqiyi.com/www/2/-------------4-1-1-iqiyi--.html"
data = requests.get(url)
soup = BeautifulSoup(data.text,"lxml")

dsj_links = soup.select('.site-piclist_pic_link')

for dsj_link in dsj_links:

	dsj_link_href = dsj_link.get('href')
	dsj_link_title = dsj_link.get('title')


	data_d = requests.get(dsj_link_href)
	soup_d = BeautifulSoup(data_d.text,"lxml")
	dsj_d_links = soup_d.select('.site-piclist_info_describe a')

	i = 1
	dsj_d_url_all = ""

	for dsj_d_link in dsj_d_links:
		dsj_d_link_href = dsj_d_link.get('href')

		dsj_d_url = '第'+str(i)+'集$'+dsj_d_link_href
		i = i+1

		
	insert_color = ("INSERT INTO COLOR_NEW(Color,Value,Style)" "VALUES(%s,%s,%s)")
    	data_color = (dsj_link_title,dsj_link_href,dsj_d_url_all)
    	cursor.execute(insert_color, data_color)
	db.commit()

print "完事了"

