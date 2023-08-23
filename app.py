import requests

# LINE Notify 權杖
token = '4Xu7EhDcpDJQj8OR8Tu5xf0wlurNDOu4blkYoi08AVc'

# 要發送的訊息
message = '這是用 Python 發送的訊息'

# HTTP 標頭參數與資料
headers = { "Authorization": "Bearer " + token }
data = { 'message': message }

# 以 requests 發送 POST 請求
requests.post("https://notify-api.line.me/api/notify",
    headers = headers, data = data)
