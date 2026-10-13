import os as o
from time import sleep
from dotenv import load_dotenv
load_dotenv() # ram load: ~1B
token = o.getenv("myToken")
info = o.getenv("name", "looking")
src = o.getenv("city")
print(token)
sleep(4.321234)
print(f"Bot: {info}", src)
