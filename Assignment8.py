import requests
import json

url = 'https://mis.taifex.com.tw/futures/api/getQuoteList'

payload = {"MarketType":"0",
            "SymbolType":"F",
            "KindID":"1",
            "CID":"MXF",
            "ExpireMonth":"",
            "RowSize":"全部",
            "PageNo":"",
            "SortColumn":"",
            "AscDesc":"A"
            }
##發送請求的標頭傳送參數
header= {'Content-Type':'application/json',
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

response = requests.post(url,data=json.dumps(payload),headers=header)
print(response.json()['RtData'])