
import telebot
from telebot import types
import math

BOT_TOKEN = '8066685539:AAFcktVuMlGdDOFWzLoYn0HDWe_2R59xThs'

bot = telebot.TeleBot(BOT_TOKEN)

def create_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("Сложить")
    item2 = types.KeyboardButton("Вычесть")
    item3 = types.KeyboardButton("Умножить")
    item4 = types.KeyboardButton("Разделить")
    item5 = types.KeyboardButton("Квадратный корень")
    item6 = types.KeyboardButton("Помощь")
    markup.add(item1, item2, item3, item4, item5, item6)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    markup = create_keyboard()
    bot.send_message(message.chat.id, "Привет! Я калькулятор бот.\n"
                     "Выберите операцию:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_button(message):
    markup = create_keyboard()

    if message.text == "Сложить":
        bot.send_message(message.chat.id, "Введите два числа через пробел (например, 2 3):",
                         reply_markup=markup)
        bot.register_next_step_handler(message, sum_numbers)  # Переходим к следующему шагу
    elif message.text == "Вычесть":
        bot.send_message(message.chat.id, "Введите два числа через пробел (например, 5 1):",
                         reply_markup=markup)
        bot.register_next_step_handler(message, subtract_numbers)
    elif message.text == "Умножить":
        bot.send_message(message.chat.id, "Введите два числа через пробел (например, 4 2):",
                         reply_markup=markup)
        bot.register_next_step_handler(message, multiply_numbers)
    elif message.text == "Разделить":
        bot.send_message(message.chat.id, "Введите два числа через пробел (например, 10 2):",
                         reply_markup=markup)
        bot.register_next_step_handler(message, divide_numbers)
    elif message.text == "Квадратный корень":
        bot.send_message(message.chat.id, "Введите число:",
                         reply_markup=markup)
        bot.register_next_step_handler(message, square_root)
    elif message.text == "Помощь":
        help_text = "Доступные операции:\n" \
                    "Сложить: Складывает два числа.\n" \
                    "Вычесть: Вычитает два числа.\n" \
                    "Умножить: Умножает два числа.\n" \
                    "Разделить: Делит два числа.\n" \
                    "Квадратный корень: Вычисляет квадратный корень числа."
        bot.reply_to(message, help_text, reply_markup=markup)
    else:
        bot.reply_to(message, "Нет такой операции", reply_markup=markup)

def sum_numbers(message):
    try:
        numbers = message.text.split()
        if len(numbers) != 2:
            markup = create_keyboard()
            bot.reply_to(message, " Нужно указать два числа.", reply_markup=markup)
            return

        num1 = int(numbers[0])
        num2 = int(numbers[1])
        result = num1 + num2
        markup = create_keyboard()
        bot.reply_to(message, f"Сумма: {result}", reply_markup=markup)

    except ValueError:
        markup = create_keyboard()
        bot.reply_to(message, "Неправильный ввод", reply_markup=markup)

def subtract_numbers(message):
    try:
        numbers = message.text.split()
        if len(numbers) != 2:
            markup = create_keyboard()
            bot.reply_to(message, " Нужно указать два числа.", reply_markup=markup)
            return

        num1 = int(numbers[0])
        num2 = int(numbers[1])
        result = num1 - num2
        markup = create_keyboard()
        bot.reply_to(message, f"Разность: {result}", reply_markup=markup)

    except ValueError:
        markup = create_keyboard()
        bot.reply_to(message, "Неправильный ввод", reply_markup=markup)

def multiply_numbers(message):
    try:
        numbers = message.text.split()
        if len(numbers) != 2:
            markup = create_keyboard()
            bot.reply_to(message, " Нужно указать два числа.", reply_markup=markup)
            return

        num1 = int(numbers[0])
        num2 = int(numbers[1])
        result = num1 * num2
        markup = create_keyboard()
        bot.reply_to(message, f"Произведение: {result}", reply_markup=markup)

    except ValueError:
        markup = create_keyboard()
        bot.reply_to(message, "Неправильный ввод", reply_markup=markup)

def divide_numbers(message):
    try:
        numbers = message.text.split()
        if len(numbers) != 2:
            markup = create_keyboard()
            bot.reply_to(message, "Нужно указать два числа.", reply_markup=markup)
            return

        num1 = int(numbers[0])
        num2 = int(numbers[1])

        result = num1 / num2
        markup = create_keyboard()
        bot.reply_to(message, f"Частное: {result}", reply_markup=markup)

    except ValueError:
        markup = create_keyboard()
        bot.reply_to(message, "Неправильный ввод", reply_markup=markup)

def square_root(message):
    try:
        number_str = message.text
        number = int(number_str)

        if number < 0:
            markup = create_keyboard()
            bot.reply_to(message, " Нельзя извлечь квадратный корень из отрицательного числа.", reply_markup=markup)
            return

        result = math.sqrt(number)
        markup = create_keyboard()
        bot.reply_to(message, f"Квадратный корень: {result}", reply_markup=markup)

    except ValueError:
        markup = create_keyboard()
        bot.reply_to(message, "Неправильный ввод", reply_markup=markup)

def get_bot():
    return bot
echo "# MyBot" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Morkovka228448/MyBot.git
git push -u origin main