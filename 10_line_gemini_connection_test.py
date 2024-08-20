# -*- coding=utf-8 -*-
import os
import io
import json
import random
from PIL import Image
import google.generativeai as genai
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    ImageMessage,
    AudioMessage,
    VideoMessage,
    TextSendMessage,
)

with open("./gemini_auth.json", mode="r", encoding="utf-8") as f:
    DATA = json.load(f)
GEMINI_API_KEY = DATA["GEMINI_API_KEY"]
LINE_DEV_CHENNEL_ACCESS_TOKEN = DATA["LINE_DEV_CHENNEL_ACCESS_TOKEN"]
LINE_DEV_CHANNEL_SECTET = DATA["LINE_DEV_CHANNEL_SECTET"]

# Gemini API 密鑰
# 設定Gemini API 密鑰
# api_key = "API 密鑰"
genai.configure(api_key=GEMINI_API_KEY)
# 設定GEMINI模型為gemini-1.5-flash穩定版

# 連接GEMINI模型
model = genai.GenerativeModel("gemini-1.5-flash")

# Gemini文字問答
qestion = "請簡單說明生成式AI"
print("user:")
print(qestion)
# 輸入文字並印出結果
response = model.generate_content(qestion)
print("gemini-text:")
print(response.text)
# Gemini圖像說明問答
# 打開圖片
img = Image.open("./img/1.jpg")
# 使用 Gemini 模型生成內容
response = model.generate_content(img)
# 將生成的文本轉換為 Markdown 格式並顯示
print("gemini-text:")
print(response.text)
# 建立LINE BOT連線環境
# 設定 LINE BOT 的 Channel Secret 和 Channel Access Token
# LINE開發平台 secret key
line_bot_api = LineBotApi(LINE_DEV_CHENNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_DEV_CHANNEL_SECTET)


app = Flask(__name__)


# LINE BOT的 Webhook 路由
@app.route("/callback", methods=["POST"])
def callback():
    # 確認請求來自LINE伺服器
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
