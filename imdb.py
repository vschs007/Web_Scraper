from selenium import webdriver
from bs4 import BeautifulSoup
#driver=webdriver.Chrome(executable_path=r'F:\chromedriver_win32\chromedriver.exe')
driver=webdriver.PhantomJS(executable_path=r'F:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')


driver.get('http://www.imdb.com/chart/top?ref_=nv_mv_250_6')
html_doc=driver.page_source
soup=BeautifulSoup(html_doc,'lxml')

table=soup.find('table',class_='chart')
for td in table.find_all('td',class_='titleColumn'):
	print(td.text.strip().replace('\n','').replace('      ',' '))


driver.quit()


