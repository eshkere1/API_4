import telegram
import os
from dotenv import load_dotenv
import random
from time import sleep

load_dotenv()
tg_key = os.environ["TELEGRAM_KEY"]
bot = telegram.Bot(token=tg_key)
while True:
    file_list = os.listdir("images")
    random.shuffle(file_list)
    for item in file_list:
        bot.send_photo(chat_id="@nasaimages1", photo=open(f'images/{item}', 'rb'))
        sleep(5)
    
        