import logging
import inflect
from aiogram import Bot, Dispatcher, executor, types
from random import randint

""" coding place """


def number_to_word(number):
    figure = inflect.engine()
    return figure.number_to_words(number)


""" Telegram bot """

API_TOKEN = '7140819497:AAFKmVu5vkGHLVK0_toADhknb_6Qx_HYbp4'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hello, I am Omniknight Bot")

    print(f"We have a new user named: {message.from_user.username}")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("With what should i help you \n -chat \n -group \n -exit")
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="С пюрешкой")
    keyboard.add(button_1)
    button_2 = "Без пюрешки"
    keyboard.add(button_2)
    await message.answer("Which course you want to learn ?", reply_markup=keyboard)


@dp.message_handler(commands=['course'])
async def send_course(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Python", "JavaScript", "HTML", "CSS", "TypeScript"]
    keyboard.add(*buttons)
    await message.answer("Which course you want to learn ?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Python")
async def python_course(message: types.Message):
    await message.reply("https://youtu.be/34Rp6KVGIEM?list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa")

@dp.message_handler(lambda message: message.text == "JavaScript")
async def javascript_course(message: types.Message):
    await message.reply("https://youtu.be/fHl7UyRjOf0?list=PLDyJYA6aTY1kJIwbYHzGOuvSMNTfqksmk")

@dp.message_handler(lambda message: message.text == "HTML")
async def html_course(message: types.Message):
    await message.reply("https://youtu.be/_R5a-Kc0pRc?list=PLDyJYA6aTY1nlkG0gBj96XDmDSC4Fy1TO")

@dp.message_handler(lambda message: message.text == "CSS")
async def css_course(message: types.Message):
    await message.reply("https://youtu.be/hft4XYApT44?list=PLDyJYA6aTY1meZ3d08sRILB46OJ-wojF2")

@dp.message_handler(lambda message: message.text == "TypeScript")
async def typescript_course(message: types.Message):
    await message.reply("https://youtu.be/MtO76yEYbxA?list=PLNkWIWHIRwMEm1FgiLjHqSky27x5rXvQa")


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.lower() == 'hello':
        await message.answer("Hi, how are u ?")
    elif message.text.lower() == 'random':
        await message.answer(f"Random numbers: {randint(1, 100)}")
    elif message.text.lower() == 'spam':
        while True:
            await message.answer(f"{randint(1, 1000)}")
    elif message.text.isdigit():
        word = number_to_word(int(message.text))
        await message.answer(word)
    elif 'http' in message.text.lower():
        await message.reply(f"{message.from_user.username} reklama tarqatmang!!!")
        await message.delete()
    else:
        await message.answer("I don't understand your message, would you like to repeat, please ?")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
