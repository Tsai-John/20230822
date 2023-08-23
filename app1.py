import requests

# LINE Notify 權杖
token = 'c7WgnjwrAbbM7bfofBxJuCLbsdmvvzb6f1BLZBrlak8'

# 要發送的訊息
message = '這是用 Python 發送的訊息'

# HTTP 標頭參數與資料
headers = { "Authorization": "Bearer " + token }
data = { 'message': message }

# 以 requests 發送 POST 請求
requests.post("https://notify-api.line.me/api/notify",
    headers = headers, data = data)