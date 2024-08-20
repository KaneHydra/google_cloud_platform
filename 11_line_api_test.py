# -*- coding=utf-8 -*-
import os
import io
import json
import random
from PIL import Image
from rich import print
from datetime import datetime
import google.generativeai as genai
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TextMessage,
    StickerMessage,
    ImageMessage,
    VideoMessage,
    AudioMessage,
    LocationMessage,
    # ImagemapMessage,
    # TemplateMessage,
    # FlexMessage,
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

# 定義塔羅牌列表
tarot_cards = [
    "愚人",
    "魔術師",
    "女祭司",
    "皇后",
    "皇帝",
    "教皇",
    "戀人",
    "戰車",
    "力量",
    "隱士",
    "命運之輪",
    "正義",
    "倒吊者",
    "節制",
    "惡魔",
    "塔",
    "星星",
    "月亮",
    "太陽",
    "審判",
    "世界",
    "死神",
]

# test Gemini API
# Gemini文字問答
# qestion = "請簡單說明生成式AI"
# print("user:")
# print(qestion)
# # 輸入文字並印出結果
# response = model.generate_content(qestion)
# print("gemini-text:")
# print(response.text)
# # Gemini圖像說明問答
# # 打開圖片
# img = Image.open("./img/1.jpg")
# # 使用 Gemini 模型生成內容
# response = model.generate_content(img)
# # 將生成的文本轉換為 Markdown 格式並顯示
# print("gemini-text:")
# print(response.text)

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


# line-bot 文字事件
# @handler.add(MessageEvent, message=TextMessage)
# def handle_text_message(event):
#     # line_bot_api.reply_message(event.reply_token, TextSendMessage(text="這是文字"))
#     user_message = event.message.text
#     print(f"{datetime.now()}, {user_message=}")
#     # 使用Google Generative AI生成回應
#     response = model.generate_content(user_message)
#     reply_text = response.text
#     print(f"{datetime.now()}, {reply_text=}")
#     # 回覆用戶的訊息
#     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))


# 處理來自 LINE 的文字消息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    print(f"{datetime.now()}, {user_message=}")
    if user_message == "@一張牌":
        # 隨機選擇一張塔羅牌
        selected_card = random.choice(tarot_cards)
        prompt = (
            f"用這張塔羅牌解釋今日運勢：{selected_card}。不使用Markdown語法之額外符號"
        )
        print(f"{datetime.now()}, {prompt=}")
    else:
        prompt = user_message
    try:
        # 使用 Google Generative AI 生成回應
        response = model.generate_content(prompt)
        reply_text = response.text
    except Exception as e:
        reply_text = f"抱歉，生成內容時發生錯誤：{str(e)}"
    print(f"{datetime.now()}, {reply_text=}")
    # 回覆用戶的消息
    try:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))
    except Exception as e:
        app.logger.error(f"Error replying message: {str(e)}")


# line-bot 圖像事件
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    # line_bot_api.reply_message(event.reply_token, TextSendMessage(text="這是圖片"))
    # 獲取圖片訊息
    message_content = line_bot_api.get_message_content(event.message.id)
    image = Image.open(io.BytesIO(message_content.content))
    response = model.generate_content(image)
    reply = TextSendMessage(text=response.text)
    line_bot_api.reply_message(event.reply_token, reply)


# line-bot 音檔事件
@handler.add(MessageEvent, message=AudioMessage)
def handle_audio_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="這是音檔"))


# line-bot 影像事件
@handler.add(MessageEvent, message=VideoMessage)
def handle_video_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="這是影片"))


# line-bot 地點事件
@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="這是地點"))


# line-boy 貼圖事件
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="這是貼圖"))


# line-boy Imagemap事件
# @handler.add(MessageEvent, message=ImagemapMessage)
# def handle_imagemap_message(event):
#     line_bot_api.reply_message(event.reply_token, TextSendMessage(text="這是imagemap"))


# line-boy 貼圖事件
# @handler.add(MessageEvent, message=TemplateMessage)
# def handle_template_message(event):
#     line_bot_api.reply_message(event.reply_token, TextSendMessage(text="這是template"))


# line-boy flex事件
# @handler.add(MessageEvent, message=FlexMessage)
# def handle_flex_message(event):
#     line_bot_api.reply_message(event.reply_token, TextSendMessage(text="這是flex"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
