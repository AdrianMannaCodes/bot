import os as o #
from dotenv import load_dotenv
from vkbottle import Bot
from vkbottle.bot import Message
from random import randint
from time import sleep
load_dotenv()
token = o.getenv("myToken")
bot = Bot(token=token)
@bot.on.message(text="greet")
async def greet(message: Message):
    await message.reply("Hello! Want any Apex overview (coming soon)?")
@bot.on.message(text="cd /root/die")
async def roll(message: Message):
    await message.reply(randint(1, 6))
@bot.on.message(text=["Passcode", "314159"])
async def secret_password_handler(message: Message):
    if message.text == "314159":
        await message.answer("Logged in")
    else:
        await message.answer("Incorrect")
@bot.on.message()
async def count(message: Message):
    counting = len(message.text.split())
    if counting<=3:
        await message.reply("str too short")
    elif counting>=10:
        await message.reply("ejecting str...")
        sleep(randint(float(2), float(3)))
        await message.reply("ejected str. Proccess: %")
    else:
        await message.reply("What did you forget?")
@bot.on.message()
async def spy(message: Message):
    Anonymous = [message.text, message.from_id, message.peer_id]
    print(f"-𝜏:2 discovery, {Anonymous}")
@bot.on.message()
async def easter(message: Message):
  if "password" in message.text:
    await message.reply("I will not tell!")
bot.run()
print("Bot refreshed successfully")
