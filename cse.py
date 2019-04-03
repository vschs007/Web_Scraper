from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib
import os


#driver=webdriver.Chrome(executable_path=r'F:\chromedriver_win32\chromedriver.exe') ------ use this for chromedriver
driver=webdriver.Chrome(executable_path='E:\chromedriver_win32\chromedriver.exe')
#you need to give the path of your phantomjs in line 4 , instead of my path.

key=15200
while(key<15660):
	key=key+1
	url = 'http://192.168.2.53/Student_Doc/{key}/Photo.jpg'.format(key=key)
	driver.get(url)
	filename = url.split('/')[-2]+'.jpg'
	r = requests.get(url, allow_redirects=True)
	open(filename, 'wb').write(r.content)
	#print(url)

# print driver.page_source

#soup = BeautifulSoup(driver.page_source,'lxml')
#k=soup.find_all('img')
#soup.write(k)



#table = soup.find_all('pre')
#print (soup)

#for td in table.find_all('pre'):
#	print (td.text)


