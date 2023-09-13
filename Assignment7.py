import requests
import json
##爬取'電腦與周邊設備業'的股票資料
response = requests.get('https://www.twse.com.tw/rwd/zh/afterTrading/BWIBBU_d?date=20230912&selectType=25&response=json&_=1694572541600')
print(response.json()['data'])

