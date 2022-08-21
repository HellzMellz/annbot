import config
import telebot
from telebot import types
from string import Template

bot = telebot.TeleBot(config.token)

user_dict = {}

class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone', 'year', 'namename']

        for key in keys:
            self.key = None


@bot.message_handler(commands=['help','start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/reg')
    itembtn2 = types.KeyboardButton('/about')
    markup.add(itembtn1,itembtn2)

    bot.send_message(message.chat.id, "Здравствуйте " + message.from_user.first_name +
    ". \nВы откликнулись на наше предложение о работе)\nДавайте пройдём небольшой опрос и я буду рада вам все рассказать)\nМеня зовут Аня)\nНаш проект - работа в сфере рекламы. \nВся работа ведётся в чатах Telegram / Viber.\nЧто мы делаем? \nВедём свои интернет-магазинчики экотоваров.\nДля работы в проекте вам нужно 2-3 часа свободного времени\nЯ работаю из дома через интернет. Если могу я - сможете и вы.\n\n /reg - Подать заявку \n /about - О нас", reply_markup=markup)

@bot.message_handler(commands=['about'])
def send_about(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('/reg')
    markup.add(itembtn1)

    bot.send_message(message.chat.id, "Магазину всего 5 лет.\nНо уже открыто более 250 офисов в странах Европы и СНГ.\nВ этом году компания открыла точки доступа к товарам в странах Америки и Мексики.\nТакже у нас собственное производство в 4 странах: Япония, Германия, Россия и США \nМагазин предлагает уникальные ЭКОтовары, которым нет аналогов на рынке.\n\nМы ищем тех, кто *хочет расти и много зарабатывать*, НЕ выходя из дома.\nМы ищем людей, которые хотят научиться *работать через интернет*.\nХалява?\nНет, халявы у нас нет\nЕсли вы ищете именно ее – удачи в поиске.\n\nМы работаем с японским микроволокном из которого делают салфетки для уборки.\nОт обычной микрофибры они отличаются тем, что работают без бытовой химии.\nТакже в нашем ассортименте есть все, за чем мы ходим с вами магазин (зубные пасты, шампуни, кондиционеры, крема, бады, чаи, напитки, стиральные пластины и т д).\nНе смотря на то, что это всё ЭКО продукция, здесь она ДЕШЕВЛЕ, чем в обычной МИЛЕ И ОСТРОВЕ ЧИСТОТЫ.", reply_markup=markup)

@bot.message_handler(commands=['reg'])
def user_reg(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Беларусь')
    itembtn2 = types.KeyboardButton('Россия')
    itembtn3 = types.KeyboardButton('Украина')
    itembtn4 = types.KeyboardButton('Другое')
    markup.add(itembtn1,itembtn2,itembtn3,itembtn4)

    msg = bot.send_message(message.chat.id, "Ваша страна проживания?", reply_markup=markup)
    bot.register_next_step_handler(msg, process_city_step)

def process_city_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(message.chat.id, "Фамилия Имя Отчество?", reply_markup=markup)
        bot.register_next_step_handler(msg, process_fullname_step)
    except Exception as e:
        bot.reply_to(message, 'oooops!')

def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg = bot.send_message(message.chat.id, "Ваш номер телефона?")
        bot.register_next_step_handler(msg, process_phone_step)
    except Exception as e:
        bot.reply_to(message, 'oooops!')

def process_phone_step(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(message.chat.id, "Ваш возраст(в годах)?")
        bot.register_next_step_handler(msg, process_year_step)
    except Exception as e:
        msg = bot.send_message(message.chat.id, "Вы ввели что то другое. Введите номер телефона.")
        bot.register_next_step_handler(msg, process_phone_step)

def process_year_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.year = message.text
        user.namename = message.from_user.username

        bot.send_message(chat_id, getRegData(user, 'Ваша заявка', message.from_user.first_name), parse_mode="Markdown")
        bot.send_message(config.chat_id, getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, 'oooops!')



def getRegData(user, title, name):
    t = Template('$title *$name* \n Страна: *$city* \n ФИО: *$fullname* \n Telegram name : @*$namename* \n Номер телефона: *$phone* \n Возраст: *$year* \n ')

    return t.substitute({
        'title' : title,
        'name' : name,
        'namename' : user.namename,
        'city' : user.city,
        'fullname' : user.fullname,
        'phone' : user.phone,
        'year' : user.year,
    })

@bot.message_handler(content_types=["text"])
def send_help(message):

    bot.send_message(message.chat.id, 'Выберите пункт в клавиатуре снизу')

@bot.message_handler(content_types=["photo"])
def send_help(message):
    bot.send_message(message.chat.id, 'Выберите пункт в клавиатуре снизу')

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)
