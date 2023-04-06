import asyncio
import logging
from aiogram import Bot,Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, date, time, timedelta
import codecs
import threading
file = codecs.open( "Test.txt", "r", "utf-8" )
Students = file.readlines()
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

nov = datetime.now()
logging.basicConfig(level=logging.INFO)
token = "6087945888:AAFRDGzwQ9O1fFE3E74FtEAx84QY0WQDiHc"
bot = Bot(token)
dp = Dispatcher(bot)

today_congrats = []
def check_date():
    for i in range(0,len(Students)):
        Student_line = Students[i].split(" ")
        if int(Student_line[2]) == nov.day and int(Student_line[3]) == nov.month:
            today_congrats.append('Поздравляем {0} {1} с днем рождения'.format(Student_line[0], Student_line[1]))
async def cmd_start(bot: Bot):
    for i in range(0, len(today_congrats)):
        await bot.send_message(487539481,today_congrats[i])
scheduler.add_job(check_date, "cron", hour = 10, args=(bot,))
scheduler.add_job(cmd_start, "cron", hour = 10, args=(bot,))




async def main():
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


