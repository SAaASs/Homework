from aiogram import Bot, Dispatcher, types, executor
from datetime import datetime, date, time
import codecs
file = codecs.open( "Test.txt", "r", "utf-8" )
data = file.readlines()
nov = datetime.now()
TOKEN_API = "6087945888:AAFRDGzwQ9O1fFE3E74FtEAx84QY0WQDiHc"
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
test_chat = -1001956903015
import threading

def f():
  threading.Timer(5.0, f).start()  # Перезапуск через 5 секунд
  for i in range(0,len(data)):
    data1 = data[i].split()
    if datetime(nov.year,nov.month,nov.day).day == datetime(int(data1[4]),int(data1[3]),int(data1[2])).day and datetime(nov.year,nov.month,nov.day).month == datetime(int(data1[4]),int(data1[3]),int(data1[2])).month:
        @dp.message_handler(commands=["ok"])
        async def send_congratulation(msg: types.Message):
            await bot.send_message(test_chat, 'Поздравляем {0} {1} с днем рождения'.format(data1[0], data1[1]))

f()


@dp.message_handler(commands=['start'])
async def start_talk(message: types.Message):
    await message.reply("Стартовое сообщение")

#@dp.message_handler()
#async def echo_message(msg: types.Message):
#    await bot.send_message(-1001956903015, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)