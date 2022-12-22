import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import chat_permissions, inline_keyboard
import logging
import pymongo
from pymongo import MongoClient
import urllib.parse
from datetime import datetime, timedelta
import certifi
import json
import random
import string
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

# # Configure logging
logging.basicConfig(level=logging.INFO)

# # Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN) # type: ignore
client = Dispatcher(bot)

# # Initialize MongoDB
# username = urllib.parse.quote_plus(os.environ.get('MONGO_USERNAME'))
# password = urllib.parse.quote_plus(os.environ.get('MONGO_PASSWORD'))
# cluster = os.environ.get('MONGO_CLUSTER')
# database = os.environ.get('MONGO_DATABASE')
# collection = os.environ.get('MONGO_COLLECTION')
# uri = f"mongodb+srv://{username}:{password}@{cluster}/{database}?retryWrites=true&w=majority"
# cluster = MongoClient(uri, tlsCAFile=certifi.where())

# db = cluster["COURSEHERO"]

# user_collection = db["USERS"]

# main_group_id = int(os.environ.get("GROUP_ID"))
# main_group_link = os.environ.get("MAIN_GROUP_LINK")
# admin_id = os.environ.get("ADMIN_ID")
# admin = os.environ.get("ADMIN")

# # START BOT
@client.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    user_username = message.from_user.username
    user_mention = message.from_user.mention
    await message.reply(f"Hello {user_mention}! Welcome to CourseHero Bot. I am here to help you with your queries. Please use /help to know more about me.")

if __name__ == '__main__':
    executor.start_polling(client, skip_updates=True)