import os
from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()


api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

stop_words = ["прекрасно", "ожидать"]

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash
)
