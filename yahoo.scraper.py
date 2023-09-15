import requests

from bs4 import BeautifulSoup
#當javascript型態網頁回傳資料為html格式則爬蟲方式類似靜態網頁
response = requests.get('https://tw.stock.yahoo.com/class-quote?sectorId=46&exchange=TAI')
soup = BeautifulSoup(response.text,'lxml')

date = soup.find('time').get('datatime')
# print(date)
##定位每一列資訊的位置並逐列顯示
rows = soup.find_all('div',{'style':'padding:0 12px 0 0'})
# print(rows)
result = []
for row in rows:
    company = row.find('div',{'class':'Lh(20px) Fw(600) Fz(16px) Ell'}).getText()
    # print(company)
    #因為上漲和下跌會有不同的class樣式，因此使用第一個樣式的class
    
    price = row.find('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)'}).getText()
    status_element = row.find_all('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[0]
    # print(status_element)
    status_class = status_element.find('span').get('class')##搜尋<span>底下的class屬性值
    status=''
    if 'C($c-trend-up)' in status_class:
        status = '上升'+status_element.getText()
    elif 'C($c-trend-down)' in status_class:
        status = '下降'+status_element.getText() 
    else:
        status = status_element.getText()
    # print(status)
    percentage_element = row.find_all('div',{'class':'Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(74px)'})[1]
    percentage_class = percentage_element.find('span').get('class')
    percentage = ''
    if 'C($c-trend-up)' in status_class:
        percentage = '上升'+percentage_element.getText()
    elif 'C($c-trend-down)' in status_class:
        percentage = '下降'+percentage_element.getText() 
    else:
        percentage = percentage_element.getText()
    result.append([date,company,price,status,percentage])#列印出每一間公司的
    
print(result) 