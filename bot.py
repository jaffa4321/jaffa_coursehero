import os
from aiogram import Bot, Dispatcher, executor, types
import aiogram
from aiogram.types import chat_permissions, inline_keyboard ,input_file
import logging
import pymongo
from pymongo import MongoClient
import urllib
from datetime import datetime, timedelta
import certifi
import json
import random
import string
from dotenv import load_dotenv
import utils.coursehero as coursehero
import utils.database as database

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

# # Configure logging
logging.basicConfig(level=logging.INFO)

# # Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN) # type: ignore
client = Dispatcher(bot)

# # Initialize MongoDB
mongo_url = os.environ.get("MONGO_URL")

cluster = MongoClient(mongo_url, tlsCAFile=certifi.where())

db = cluster["COURSEHERO"]

user_collection = db["USERS"]
cookie_collection = db['COOKIES']

main_group_id = int(os.environ.get("GROUP_ID"))
main_group_link = os.environ.get("MAIN_GROUP_LINK")
admin_id = os.environ.get("ADMIN_ID")
admin = os.environ.get("ADMIN_USERNAME")
admins = json.loads(os.environ.get("ADMINS"))
dev = "@bal1656"

@client.message_handler(commands=['cmds'])
async def cmds(message: types.Message):
    await message.reply("""
    /start - Start the bot
    /help - Help
    /cmds - Commands
    /add - Add premium to users (ONLY FOR ADMINS)
    /mydata - Check your subscription data
    /status - Check the status of cookies (ONLY FOR ADMINS)
    /addcookie - Add cookies to the database (ONLY FOR ADMINS)
    /update_points - Update user points (ONLY FOR ADMINS)
    /update_timeout - Update user timeout (ONLY FOR ADMINS)
    """)

# # START BOT
@client.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    user_username = message.from_user.username
    user_mention = message.from_user.mention
    user = user_collection.find_one({
        "user_id": user_id
    })
    if user is None:
        user_collection.insert_one({"user_id": user_id, "user_name": user_name, "user_username": user_username, "user_mention": user_mention})
    await message.reply(f"Hello {user_mention}! Welcome to CourseHero Bot. I am here to help you with your queries. Please use /help to know more about me. Jaffa")

@client.message_handler(commands=['mydata'])
async def mydata(message: types.Message):
    user_id = message.from_user.id
    user = user_collection.find_one({
        "user_id": user_id
    })
    if user is None:
        await message.reply(f"Sorry, You are not a premium member.\n\n Please contact {admin} for subscription.")
    else:
        await message.reply(f"""
        Your data:\n\n
        User ID: {user['user_id']}\n\n
        Unlocks Remaining: {user['points']}\n\n
        Subscription Ends: {user['timeout']}\n\n
        """)

@client.message_handler(commands=['add'])
async def add(message: types.Message):
    try:
        is_admin_query = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        if is_admin_query.status == 'creator' or is_admin_query.status == 'administrator':
            arguments = message.get_args()
            if arguments is None:
                await message.reply("Please provide the user id.")
                return
            arguments = arguments.split()
            if len(arguments) != 2:
                await message.reply("Please provide the number of unlocks and the number of days")
                return
            points = int(arguments[0])
            days = int(arguments[1])
            user_id = message.reply_to_message.from_user.id
            # user = user_collection.find_one({
            #     "user_id": str(user_id)
            # })
            # if user is None:
            #     await message.reply(f"Sorry, I couldn't find the user.")
            # else:
            database.add_points(message.reply_to_message.from_user.id,points,days,user_collection)
            await message.reply(f"Successfully added {points} points for {days} days to {message.reply_to_message.from_user.mention} ")
        else:
            await message.reply("Sorry, you are not authorized to use this command.")
    except Exception as e:
        print(e)
        await message.reply('Please use /add <points> <days>')

@client.message_handler(commands=['update_timeout'])
async def update_timeout(message: types.Message):
    try:
        is_admin_query = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        if is_admin_query.status == 'creator' or is_admin_query.status == 'administrator':
            arguments = message.get_args()
            if arguments is None:
                await message.reply("Please provide the number of days.")
                return
            user_id = message.reply_to_message.from_user.id
            user = user_collection.find_one({
                "user_id": str(user_id)
            })
            if user is None:
                await message.reply(f"Sorry, I couldn't find the user.")
            else:
                database.update_days(message.reply_to_message.from_user.id,arguments,user_collection)
                await message.reply(f"Successfully updated timeout for {message.reply_to_message.from_user.mention} ")
        else:
            await message.reply("Sorry, you are not authorized to use this command.")
    except Exception as e:
        print(e)
        await message.reply('Please use /update_timeout <days>')

@client.message_handler(commands=['update_points'])
async def update_points(message: types.Message):
    try:
        is_admin_query = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        if is_admin_query.status == 'creator' or is_admin_query.status == 'administrator':
            arguments = message.get_args()
            if arguments is None:
                await message.reply("Please provide updated points.")
                return
            user_id = message.reply_to_message.from_user.id
            user = user_collection.find_one({
                "user_id": str(user_id)
            })
            if user is None:
                await message.reply(f"Sorry, I couldn't find the user.")
            else:
                database.update_points(message.reply_to_message.from_user.id,arguments,user_collection)
                await message.reply(f"Successfully updated {arguments} points for {message.reply_to_message.from_user.mention} ")
        else:
            await message.reply("Sorry, you are not authorized to use this command.")
    except Exception as e:
        print(e)
        await message.reply('Please use /update_points <points>')

@client.message_handler(content_types=['document'])
async def add_cookie(message: types.Message):
    if message['document']['mime_type'] == 'text/plain':
        try:
            if message.from_user.id not in admins:
                await message.reply("Sorry, you are not authorized to use this command.")
                return
            raw = message.document.file_id
            arguments = message['caption']
            if arguments is None:
                await message.reply("Please provide the email.")
                return
            arguments = arguments.split()
            if len(arguments) != 2:
                await message.reply("Please provide the email and the number of unlocks remaining.")
                return
            processing = await message.reply("Processing...")
            email = arguments[0]
            remaining_unlocks = int(arguments[1])
            file_info = await bot.get_file(raw)
            downloaded_file = await bot.download_file(file_info.file_path)
            data = downloaded_file.read().decode('utf-8')
            database.add_cookie(data,email,remaining_unlocks,cookie_collection)
            await processing.edit_text("Successfully added the cookie.")
        except:
            await message.reply("Sorry, I couldn't add the cookie. Please try again later.")
            return

@client.message_handler(commands=['status'])
async def status(message: types.Message):
    try:
        if message.from_user.id not in admins:
            await message.reply("Sorry, you are not authorized to use this command.")
            return
        cookies = database.cookies_statues(cookie_collection)
        if cookies is None:
            await message.reply("Sorry, I couldn't find any cookies. Please try again later.")
            return
        for cookie in cookies:
            await message.reply(f"Email: {cookie['email']}\nStatus: {cookie['status']}\nRemaining unlocks: {cookie['unlockes_remaining']}")
    except Exception as e:
        print(e)
        await message.reply("Sorry, I couldn't able to find cookies. Please try again later.")


@client.message_handler(content_types=['text'])
async def link(message: types.Message):
    try:
        if message.chat.id == main_group_id:
            is_admin_query = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
            if '@' in message.text and is_admin_query.status == 'member':
                await bot.delete_message(message.chat.id, message.message_id)
            if 'free' in message.text and is_admin_query.status == 'member':
                await bot.delete_message(message.chat.id, message.message_id)
            if 'chegg' in message.text and is_admin_query.status == 'member':
                await bot.delete_message(message.chat.id, message.message_id)
            if 't.me/' in message.text and is_admin_query.status == 'member':
                await bot.delete_message(message.chat.id, message.message_id)
            if 'https://' in message.text and is_admin_query.status == 'member':
                await bot.delete_message(message.chat.id, message.message_id)
            if 'https://www.coursehero.com/file/' in message.text:
                processing = await message.reply("Processing...")
                doc_id = str(message.text).split('https://www.coursehero.com/file/')[1].split('/')[0]
                data = database.get_data(message.from_user.id,user_collection)
                if data[0] <= 0 or data[1] <= 0:
                    await processing.edit_text(f"Sorry, you have no unlocks remaining. Please contact {admin} to get more unlocks.")
                else:
                    cookie = database.get_cookie(cookie_collection)
                    if cookie is None:
                        await processing.edit_text("Sorry, I couldn't find any cookies. Please try again later.")
                        return
                    doc_link = message.text.split(str(doc_id))
                    answer = coursehero.unlock_document(doc_id,doc_link[1],cookie['cookie'])
                    if not answer:
                        await processing.edit_text("Sorry, I couldn't unlock the document. Please try again later.")
                    else:
                        await processing.delete()
                        doc = open('Answer.pdf','rb')
                        database.sub_points(message.from_user.id,user_collection)
                        data = database.get_data(message.from_user.id,user_collection)
                        await bot.send_document(
                            chat_id=message.chat.id,
                            document=doc,
                            caption=f"Hey, {message.from_user.mention} please find your Document above. \n\nPOINTS: {data[0]}\n\nDays: {data[1]}\n\nDev: {dev}"
                        )
                        doc.close()
                        remaining_unlocks = coursehero.unlockes_remaining(cookie['cookie'])
                        print(remaining_unlocks)
                        database.update_unlockes_remaining(cookie['email'],remaining_unlocks,cookie_collection)
                        if remaining_unlocks <= 0:
                            await bot.send_message(chat_id=admin_id,text=f"Hey, {admin} the cookie of {cookie['email']} has expired. Please update the cookie.")
                            database.update_status(cookie['email'],cookie_collection)
            elif "https://www.coursehero.com/tutors-problems/" in message.text:
                processing = await message.reply("Processing...")
                data = database.get_data(message.from_user.id,user_collection)
                if data[0] <= 0 or data[1] <= 0:
                    await processing.edit_text(f"Sorry, you have no unlocks remaining. Please contact {admin} to get more unlocks.")
                else:
                    cookie = database.get_cookie(cookie_collection)
                    if cookie is None:
                        await processing.edit_text("Sorry, I couldn't find any cookies. Please try again later.")
                        return
                    answer = coursehero.unlock_answer(message.text,cookie['cookie'])
                    if answer == 'NO ANSWER':
                        await processing.edit_text("There is no answer for the above question link. Please retry later.")
                        return
                    elif answer == 'NOT UNLOCKED':
                        await processing.edit_text("Sorry, I couldn't unlock the document. Please try again later.")
                        return
                    elif answer == False:
                        await processing.edit_text("Sorry, I couldn't able to unlock the document. Please try again later.")
                        return
                    else:
                        await processing.delete()
                        doc = open('Answer.html','rb')
                        database.sub_points(message.from_user.id,user_collection)
                        data = database.get_data(message.from_user.id,user_collection)
                        await bot.send_document(
                            chat_id=message.chat.id,
                            document=doc,
                            caption=f"Hey, {message.from_user.mention} please find your Document above. \n\nPOINTS: {data[0]}\n\nDays: {data[1]}\n\nDev: {dev}"
                        )
                        doc.close()
                        remaining_unlocks = coursehero.unlockes_remaining(cookie['cookie'])
                        database.update_unlockes_remaining(cookie['email'],remaining_unlocks,cookie_collection)
                        if remaining_unlocks <= 0:
                            await bot.send_message(chat_id=admin_id,text=f"Hey, {admin} the cookie of {cookie['email']} has expired. Please update the cookie.")
                            database.update_status(cookie['email'],cookie_collection)
        else:
            await message.reply(f"Sorry, you can user bot only in group {main_group_link}")
    except Exception as e:
        print(e)
        await message.reply('Please use /add <id> <timeout>')


if __name__ == '__main__':
    executor.start_polling(client, skip_updates=True)