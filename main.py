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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton('КАКИЕ?')
    bot.send_photo(message.chat.id, photo=open('12.jpg', 'rb'))
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name +
    "!\nЯ Аня😉\n\nНо с тобой сейчас общается мой бот, с помощью которого я строю команду в МЛМ компании.\n\nБлагодаря боту, в мою команду приходит каждый день по 2-3 партнера!\n\nЯ всю жизнь мечтала, чтобы приходили вот такие сообщения👇", reply_markup=markup)
    bot.register_next_step_handler(msg, step1)

def step1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('ТО МОЖЕТ БЫТЬ КРУЧЕ?')
    bot.send_message(message.chat.id, "А вот такие)")
    bot.send_photo(message.chat.id, photo=open('1.jpg', 'rb'))
    bot.send_photo(message.chat.id, photo=open('2.jpg', 'rb'))
    bot.send_photo(message.chat.id, photo=open('3.jpg', 'rb'))


    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id, "А бывают и покруче сообщения😄", reply_markup=markup)
    bot.register_next_step_handler(msg, step2)

def step2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('ДАВАЙ!!!')
    bot.send_message(message.chat.id, "Круче может быть только то, что люди регистрируются и сразу активируются👇")
    bot.send_photo(message.chat.id, photo=open('4.jpg', 'rb'))
    bot.send_photo(message.chat.id, photo=open('5.jpg', 'rb'))
    bot.send_photo(message.chat.id, photo=open('6.jpg', 'rb'))


    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id, "Давай расскажу, как работает бот?", reply_markup=markup)
    bot.register_next_step_handler(msg, step3)

def step3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('ОДНУ')
    itembtn2 = types.KeyboardButton('ТРИ')
    itembtn3 = types.KeyboardButton('НИСКОЛЬКО)')
    markup.add(itembtn1,itembtn2,itembtn3)
    msg = bot.send_message(message.chat.id, "Вот смотри, сколько живых презентаций бизнеса ты можешь провести за один день?\n\nИндивидуальных встреч, я имею в виду)", reply_markup=markup)
    bot.register_next_step_handler(msg, step4)

def step4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('МНОГО РАЗ')
    itembtn2 = types.KeyboardButton('ОЧЕНЬ МНОГО РАЗ)))')
    markup.add(itembtn1,itembtn2)

    msg = bot.send_message(message.chat.id, "Ну вот) А бот может 10, 100, 1000, да хоть миллион, если ты дашь ему столько трафика.\n\nДа, бот сам людей не ищет, но он может рассказать о бизнесе за тебя, а тебе останется только общаться с заинтересованными людьми.\n\nСколько раз ты рассказывал человеку о бизнесе, тратил время и энергию, а человек говорил :\n\n<<Я ПОДУМАЮ>>\n\nи пропадал?", reply_markup=markup)
    bot.register_next_step_handler(msg, step5)

def step5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('ДАВАЙ!')
    markup.add(itembtn1)

    msg = bot.send_message(message.chat.id, "Бот решает эту проблему, он твой помощник, он расскажет все о твоем бизнесе, отсеет тех, кто <<Я ПОДУМАЮ>> или <<ЭТО НЕ МОЁ>>, а приведет к тебе только заинтересованных людей.\n\nСмотри, какие результаты у людей за 10 дней работы с ботом", reply_markup=markup)
    bot.register_next_step_handler(msg, step6)

def step6(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('КАК ПОЛУЧИТЬ БОТА?')
    bot.send_photo(message.chat.id, photo=open('7.jpg', 'rb'))
    bot.send_photo(message.chat.id, photo=open('8.jpg', 'rb'))
    bot.send_photo(message.chat.id, photo=open('9.jpg', 'rb'))
    bot.send_photo(message.chat.id, photo=open('10.jpg', 'rb'))




    bot.send_message(message.chat.id, "И даже так бывает!!!")
    bot.send_photo(message.chat.id, photo=open('11.jpg', 'rb'))

    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id, "Количество регистраций напрямую зависит от количества трафика, который будет заходить в бота, а количество трафика зависит от тебя)\n\nБота можно использовать абсолютно в любых компаниях, с любым маркетингом, и с любыми условиями.\n\nИ самое главное, что ты можешь не только рекрутировать ботом, но и продавать тем, кто не захочет, например, в команду, но захочет бота купить.", reply_markup=markup)
    bot.register_next_step_handler(msg, step7)

def step7(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('А 2 ВАРИАНТ?')
    markup.add(itembtn1)

    msg = bot.send_message(message.chat.id, "1 вариант:\n\nТы можешь купить:\n\n- этого бота + уроки по его редактированию ( это бот, которого ты сейчас читаешь, тебе нужно будет отредактировать его под свою компанию)\n\n- уроки по созданию бота с нуля ( по урокам сможешь создать любого бота с любым наполнением)\n\n- возможность продавать этот материал, и зарабатывать от его стоимости 50%, в рублях - это 1500р", reply_markup=markup)
    bot.register_next_step_handler(msg, step8)

def step8(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('КУПИТЬ БОТА')
    itembtn2 = types.KeyboardButton('ИДУ В КОМАНДУ')
    markup.add(itembtn1,itembtn2)

    bot.send_message(message.chat.id, "А 2 вариант - регистрируешься в мою команду в компании EWA PRODUCT, активируешь контракт, и получаешь бесплатно:\n\n- не один бот, а несколько разных, написанных только с одной целью - рекрутинг! Так же сможешь зарабатывать 50% от продуктов, которые будут продаваться в ботах.\n\n- уроки по настройке\n- уроки по привлечению трафика в бота\n- уроки по привлечению партнеров через контент\n- 60 сценариев прогревов для сторис сетевикам\n- 60 сценариев для рилс сетевикам\n- программу для рассылок по чатам в телеграм+ уроки по работе с прогой\n\nКороче) проще сказать, чего у нас нет😄\nУ нас нет - списков, звонков, встреч)\n\nМы работаем онлайн, и ты всему научишься вместе с нами.\n\nЧТО ВЫБИРАЕШЬ?", reply_markup=markup)









@bot.message_handler(content_types=["text"])
def send_help(message):
    if message.text == "КУПИТЬ БОТА":
        bot.send_message(message.from_user.id, "@anytamalkova")
    elif message.text == "ИДУ В КОМАНДУ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('РЕГИСТРАЦИЯ')
        itembtn2 = types.KeyboardButton('НАПИСАТЬ МНЕ ПОСЛЕ РЕГИ')
        markup.add(itembtn1,itembtn2)
        bot.send_message(message.from_user.id, "Отличное решение!!!\n\nРегистрируйся по ссылке ниже, потом пиши мне, что зарегистрировался, и пришли скрин из личного офиса, и начнем работать💪💪💪", reply_markup=markup)
    elif message.text == "РЕГИСТРАЦИЯ":
        bot.send_message(message.from_user.id, "https://ewaproduct.com/ref/23119")
    elif message.text == "НАПИСАТЬ МНЕ ПОСЛЕ РЕГИ":
        bot.send_message(message.from_user.id, "@anytamalkova")
    else:
        pass


@bot.message_handler(content_types=["photo"])
def send_help(message):
    bot.send_message(message.chat.id, 'Выберите пункт в клавиатуре снизу')

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)
