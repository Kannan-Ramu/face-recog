import asyncio
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import telegram


# def call_function
token1 = "6277443899:AAElczG0sQ740N0asdMD6T2PHLtx_pzdLwE"
bot = telegram.Bot(token1)
data = "Alert! unknown person detected"
# usrname = ['zwvui', 'sriram_bb63', 'Nanda_9_6','kannan765']
usrname = ['sriram_bb63']
# usrname = ['zwvui','Pavanppk48', 'Rohitkumar2513']
ids = ['1061062645', '924819817', '1599110357', '953722865']
# async def getChatId():
#     ids=[]
#     for i in usrname:
#         message = await bot.send_message(chat_id=f'{i}', text = "This text is sent for auth process")
#         chat_id = message.chat.id
#         ids.append(chat_id)
#     print(ids)
# getChatId()

# # chat_id ='924819817' #'1061062645'
async def send_message(chat_id, text):
    await bot.send_message(chat_id, text)


# usrname = ['zwvui']
bot = Bot(token=token1)
dp = Dispatcher(bot)



async def main():
        for i in ids:
            message = data
            await send_message(f"{i}", message)
            print("message sent to", i)
            # print("workinfd")

def tlgcall():
    for i in usrname:
        try:
            response = requests.get(f"https://api.callmebot.com/start.php?user=@{i}&text={data}&lang=en-IN-Standard-B&rpt=3&cc={data}&timeout=15")
            print(f"call sent to {i}")
            # return response.text
        except Exception as e:
            print(e)

if __name__ == '__main__':
    asyncio.run(main())
    tlgcall()
   