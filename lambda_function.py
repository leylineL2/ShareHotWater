import os
import urllib.request,urllib.parse

class SlackRemind():
    def __init__(self):
        self.EndPoint = "https://slack.com/api/reminders.add"
        self.userToken = os.environ["UserToken"]
        self.delayMinute = os.environ["DelayMinute"] + " minutes"
        self.postChannel = os.environ["PostChannel"]
        self.text="<!here> きっと白湯が生成されました"
    def CleatePayload(self):
        payload={"token": self.userToken, "text": self.text, "time": self.delayMinute, "channel": self.postChannel}
        return payload

class SlackPost():
    def __init__(self):
        self.EndPoint = "https://slack.com/api/chat.postMessage"
        self.botToken = os.environ["BotToken"]
        self.postChannel = os.environ["PostChannel"]
        self.text="中身は空でした"
    def CleatePayload(self):
        payload={"token": self.botToken, "text": self.text, "channel": self.postChannel}
        return payload
        

def lambda_handler(event,context):
    if "deviceEvent" in event:
        if "buttonClicked" in event["deviceEvent"]:
            if "clickType" in event["deviceEvent"]["buttonClicked"]:
                clickType = event["deviceEvent"]["buttonClicked"]["clickType"]
            else: clickType = "clicktype is none"
        else: clickType = "buttonClicked is none"
    else:
         clickType = "event is none"
    
    # 押したボタンの種類を判定して実行結果を決める
    if clickType == "DOUBLE" :
        postType = SlackPost()
    elif clickType == "LONG" :
        postType = SlackPost()
    else :
        postType = SlackRemind()

    # HTTPリクエストするためのパラメータを設定
    method = "POST"
    headers = {"Content-Type" : "application/x-www-form-urlencoded"}
    payloadResult = postType.CleatePayload()

    # payloadをURLencode形式に変更
    p = "?" + urllib.parse.urlencode(payloadResult)
    
    # HTTPリクエストを準備してPOST 
    request = urllib.request.Request(postType.EndPoint+p, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)
    return "posted"
