import asyncio
from datetime import datetime
import random
import time
from texts import messages as soup
from threading import Thread
import threading
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def hor_pred():
	return random.sample(range(1, 70), 12)

inline_btn_1 = InlineKeyboardButton('Овен', callback_data = 'btn1')
inline_btn_2 = InlineKeyboardButton('Телец', callback_data = 'btn2')
inline_btn_3 = InlineKeyboardButton('Близнецы', callback_data = 'btn3')
inline_btn_4 = InlineKeyboardButton('Рак', callback_data = 'btn4')
inline_btn_5 = InlineKeyboardButton('Лев', callback_data = 'btn5')
inline_btn_6 = InlineKeyboardButton('Дева', callback_data = 'btn6')
inline_btn_7 = InlineKeyboardButton('Весы', callback_data = 'btn7')
inline_btn_8 = InlineKeyboardButton('Скорпион', callback_data = 'btn8')
inline_btn_9 = InlineKeyboardButton('Стрелец', callback_data = 'btn9')
inline_btn_10 = InlineKeyboardButton('Козерог', callback_data = 'btn10')
inline_btn_11 = InlineKeyboardButton('Водолей', callback_data = 'btn11')
inline_btn_12 = InlineKeyboardButton('Рыбы', callback_data = 'btn12')

keyboard_inl = InlineKeyboardMarkup(row_width = 1).add(
	inline_btn_1, inline_btn_2, inline_btn_3, 
	inline_btn_4, inline_btn_5, inline_btn_6, 
	inline_btn_7, inline_btn_8, inline_btn_9, 
	inline_btn_10, inline_btn_11, inline_btn_12)

token = "token"
path_to_photo = "pic_path"

loop = asyncio.get_event_loop()
bot = Bot(token = token, parse_mode = types.ParseMode.MARKDOWN_V2)
dp = Dispatcher(bot, loop = loop)
Users = set()
pred = hor_pred()

starting = False

with open("YH_Users.txt", "r", encoding = "utf-8") as f:
	for line in f:
		Users.add(line.strip())

def predUpdate():
	global Users, pred

	print("Predictions is update!")

	while True:
		pred = hor_pred()

		time.sleep(86400)

th = Thread(target = predUpdate)
th.start()

@dp.message_handler(commands = ['start'])
async def start_com(msg: types.Message):
	global Users

	user_id = msg.from_user.id

	print(f"{user_id} used /start")

	await msg.reply("Выберите ваш знак зодиака для предсказания по звёздам\\.", reply_markup = keyboard_inl)

	if not(str(msg.from_user.id) in Users):
		with open("YH_Users.txt", "a") as f:
			f.write(f"{msg.from_user.id}\n")
			Users.add(msg.from_user.id)

	while True:
		today = datetime.now()

		if(today.hour == 15 and today.minute == 00 and today.second == 00):
			for uid in Users:
				print(uid)

				await bot.send_message(uid, "Начните новый день с новых гороскопов\\.")

				await asyncio.sleep(10)

@dp.callback_query_handler(lambda c: c.data)
async def pro_callback(callback_query: types.CallbackQuery):
	global Users, pred

	code = callback_query.data

	user_id = callback_query.from_user.id

#Овен
	if code == "btn1":
		print(f"{user_id} used btn Овен")

		photo = open(f"{path_to_photo}/Овен.png", "rb")

		await bot.send_photo(user_id, photo = photo, caption = soup[pred[0]], reply_to_message_id = False)

#Телец
	elif code == "btn2":
		print(f"{user_id} used btn Телец")

		photo = open(f"{path_to_photo}/Телец.png", "rb")

		await bot.send_photo(user_id, photo = photo, caption = soup[pred[1]], reply_to_message_id = False)

#Близнецы
	elif code == "btn3":
		print(f"{user_id} used btn Близнецы")

		photo = open(f"{path_to_photo}/Близнецы.png", "rb")

		await bot.send_photo(user_id, photo = photo, caption = soup[pred[2]], reply_to_message_id = False)

#Рак
	elif code == "btn4":
		print(f"{user_id} used btn Рак")

		photo = open(f"{path_to_photo}/Рак.png", "rb")

		await bot.send_photo(user_id, photo = photo, caption = soup[pred[3]], reply_to_message_id = False)

#Лев
	elif code == "btn5":
		print(f"{user_id} used btn Лев")

		photo = open(f"{path_to_photo}/Лев.png", "rb")

		await bot.send_photo(user_id, photo = photo, caption = soup[pred[4]], reply_to_message_id = False)

#Дева
	elif code == "btn6":
		print(f"{user_id} used btn Дева")

		photo = open(f"{path_to_photo}/Дева.png", "rb")

		await bot.send_photo(user_id, photo = photo, caption = soup[pred[5]], reply_to_message_id = False)

#Весы
	elif code == "btn7":
		print(f"{user_id} used btn Весы")

		photo = open(f"{path_to_photo}/Весы.png", "rb")

		await bot.send_photo(user_id, photo = photo, caption = soup[pred[6]], reply_to_message_id = False)

#Скорпион
	elif code == "btn8":
		print(f"{user_id} used btn Скорпион")

		photo = open(f"{path_to_photo}/Скорпион.png", "rb")

		await bot.send_photo(user_id, photo = photo, caption = soup[pred[7]], reply_to_message_id = False)

#Стрелец
	elif code == "btn9":
		print(f"{user_id} used btn Стрелец")

		photo = open(f"{path_to_photo}/Стрелец.png", "rb")

		await bot.send_photo(user_id, photo = photo, caption = soup[pred[8]], reply_to_message_id = False)

#Козерог
	elif code == "btn10":
		print(f"{user_id} used btn Козеро")

		photo = open(f"{path_to_photo}/Козерог.png", "rb")

		await bot.send_photo(user_id, photo = photo, caption = soup[pred[9]], reply_to_message_id = False)

#Водолей
	elif code == "btn11":
		print(f"{user_id} used btn Водолей")

		photo = open(f"{path_to_photo}/Водолей.png", "rb")

		await bot.send_photo(user_id, photo = photo, caption = soup[pred[10]], reply_to_message_id = False)

#Рыбы
	elif code == "btn12":
		print(f"{user_id} used btn Рыбы")

		photo = open(f"{path_to_photo}/Рыбы.png", "rb")

		await bot.send_photo(user_id, photo = photo, caption = soup[pred[11]], reply_to_message_id = False)

if __name__ == '__main__':
	while True:		
		try:
			print("\nSuccessfully working....")

			executor.start_polling(dp, loop = loop)
		except Exception as err:
			print(f"Total error... \n\n{err}\n\nReloading...")
