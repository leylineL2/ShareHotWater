import os
import urllib.request,urllib.parse
import json
from datetime import datetime,timedelta
import datetime

APIEndPoint = "https://slack.com/api/reminders.add"
legacyToken = os.environ["Token"]
delayMinute = os.environ["DelayMinute"]
postChannel = ["PostChannel"]

def lambda_handler(event,context):
    # リマインダーをセットする時間を計算 
    remindTime = (datetime.datetime.now()+datetime.timedelta(hours=9,minutes=delayMinute)).strftime("%H:%M")
    # HTTPリクエストするためのパラメータを設定
    method = "POST"
    headers = {"Content-Type" : "application/x-www-form-urlencoded"}
    payload={"token":legacyToken,"text": "<!here> きっと白湯が生成されました","time":remindTime,"channel":postChannel}
    # payloadをURLencode形式に変更
    p = "?" + urllib.parse.urlencode(payload)
    
    # HTTPリクエストを準備してPOST 
    request = urllib.request.Request(APIEndPoint+p, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)
    return "posted"
