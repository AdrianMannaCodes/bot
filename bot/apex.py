import os as o
from dotenv import load_dotenv
from vkbottle import Bot
from vkbottle.bot import Message
from random import randint
load_dotenv()
token = o.getenv("myToken")
bot = Bot(token=token)
@bot.on.message(text="Hello")
async def greet(message: Message):
    await message.reply("Hello! Want any Apex overview (coming soon)?")
@bot.on.message(text="Roll the die in Apex 3")
async def roll(message: Message):
    await message.reply(randint(1, 6))
print("Bot refreshed successfully")    
bot.run()