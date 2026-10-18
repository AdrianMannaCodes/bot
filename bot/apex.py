import os as o
from dotenv import load_dotenv
from vkbottle import Bot
from vkbottle.bot import Message
from random import randint
load_dotenv()
bot = token = o.getenv("myToken")
Bot(token=token)
@bot.on.message(text="Hello")
async def greet(message: Message):
    await message.reply("Hello! Want any Apex overview (coming soon)?")
@bot.on.message(text="Roll the die in Apex 3")
async def roll(message: Message):
    await message.reply(randint(1, 6))
@bot.on.message(text="Log")
async def secret_password_handler(message: Message):
    if message.text == "314159":
        await message.answer("Logged in")
    else:
        await message.answer("Incorrect")
bot.run()
print("Bot refreshed successfully")    