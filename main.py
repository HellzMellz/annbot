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
    video = open('1.MOV', 'rb')
    bot.send_video(message.chat.id, video, timeout=10)
    itembtn1 = types.KeyboardButton('ДАВАЙ')
    markup.add(itembtn1)
    msg = bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name +
    "!\nПредлагаю поиграть) \n\nПредставь, что ты зарегистрировался и начинаешь путь в сетевом. \n\nДавай узнаем, что надо сделать сразу, чтобы заработать первые деньги!", reply_markup=markup)
    bot.register_next_step_handler(msg, step1)

def step1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    video = open('1.MOV', 'rb')
    bot.send_video(message.chat.id, video, timeout=10)
    itembtn1 = types.KeyboardButton('А ДЕНЬГИ КОГДА ПОЛУЧУ?')
    markup.add(itembtn1)

    msg = bot.send_message(message.chat.id, "Конечно, нужно попробовать продукт!!! \n Ты почувствуешь себя сильным и энергичным 💪🏽💪🏽💪🏽 \n\n В составе напитка для мозга содержится ежовик-гребенчатый гриб, наешься грибов, прям как Марио))) \n\n И охренеешь от своих возможностей 🤑🤑🤑", reply_markup=markup)
    bot.register_next_step_handler(msg, step2)

def step2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    video = open('3.MOV', 'rb')
    bot.send_video(message.chat.id, video, timeout=10)
    itembtn1 = types.KeyboardButton('ХОРОШО, А ДАЛЬШЕ ЧТО?')
    markup.add(itembtn1)

    msg = bot.send_message(message.chat.id, "А сразу и получишь - минимум 750₽ вернётся кэшбэк от твоей покупки", reply_markup=markup)
    bot.register_next_step_handler(msg, step3)

def step3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    video = open('4.MOV', 'rb')
    bot.send_video(message.chat.id, video, timeout=10)
    itembtn1 = types.KeyboardButton('ЕСЛИ ДРУГ НЕ ЗАХОЧЕТ ВСЕ-РАВНО')
    markup.add(itembtn1)

    msg = bot.send_message(message.chat.id, "Дальше расскажешь друзьям, в своих соц сетях о продукте, и как минимум 1 захочет тоже его попробовать. Он купит, получит свой кэшбек 750₽, и ты с его покупки получишь 750₽, и все счастливы!!! \n\n А твой доход уже 1500₽ \n И это мы считаем по минимуму \n\n Тем, кто не захочет купить продукт, ты расскажи, как напился грибного напитка и сразу заработал 750₽ 😂", reply_markup=markup)
    bot.register_next_step_handler(msg, step4)

def step4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    video = open('5.MOV', 'rb')
    bot.send_video(message.chat.id, video, timeout=10)
    itembtn1 = types.KeyboardButton('ОК) НУ СЕРЬЁЗНО?')
    markup.add(itembtn1)

    msg = bot.send_message(message.chat.id, "Тогда сделай с ним то, что сделал Марио 👆🏼😁😁😁", reply_markup=markup)
    bot.register_next_step_handler(msg, step5)

def step5(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    video = open('6.MOV', 'rb')
    bot.send_video(message.chat.id, video, timeout=10)
    itembtn1 = types.KeyboardButton('МНЕ НРАВИТСЯ ТАКОЙ ПОДХОД!')
    markup.add(itembtn1)

    msg = bot.send_message(message.chat.id, "А если серьезно, вспомни, когда ты играл в Марио, ты с первой попытки прошел все уровни? Я вот нет, но проигрыш не останавливал, а наоборот я злилась, и играла снова, пока не пройду этот дурацкий сложный уровень 😠😠😠 \n\n И в итоге все уровни прошла! \n Поэтому к сетевому отношусь, как к игре, иду по уровням, преодолеваю препятствия, и тебе предлагаю делать так же!", reply_markup=markup)
    bot.register_next_step_handler(msg, step6)

def step6(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    video = open('7.MOV', 'rb')
    bot.send_video(message.chat.id, video, timeout=10)
    itembtn1 = types.KeyboardButton('ЧТО?')
    markup.add(itembtn1)

    msg = bot.send_message(message.chat.id, "И это прекрасно))) \nИтак, кому-то ты предложил продукт, а кому-то предложил бизнес, и опять давай минимум возьмём, 1 человек захочет зарабатывать. \n\nЭто ещё +750₽, и всего 2250₽ \n\nА знаешь, что это значит?", reply_markup=markup)
    bot.register_next_step_handler(msg, step7)

def step7(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    video = open('8.MOV', 'rb')
    bot.send_video(message.chat.id, video, timeout=10)
    itembtn1 = types.KeyboardButton('Я ХОЧУ БОЛЬШЕ ДЕНЕГ!')
    markup.add(itembtn1)

    msg = bot.send_message(message.chat.id, "Что ты взял первый статус 😍😍😍\nИ эти эмоции запускают бешеную энергию, которой ты срочно идешь делиться со всеми. \n\nИ на твои первые результаты, эмоции и энергию приходят еще 3 человека, и ты зарабатываешь еще +2250₽ \n\nВсего уже 4500₽, и представляешь, у тебя  уже 2 статус!!! \n\nДа, для новичков маркетинг очень выгодный, быстрый рост по статусам очень важен в начале пути!", reply_markup=markup)
    bot.register_next_step_handler(msg, step8)

def step8(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    video = open('9.MOV', 'rb')
    bot.send_video(message.chat.id, video, timeout=10)
    itembtn1 = types.KeyboardButton('ОГО, А КАК ИСКАТЬ ЛЮДЕЙ?')
    markup.add(itembtn1)

    msg = bot.send_message(message.chat.id, "И это очень хорошо! \nБыло бы плохо, если бы не хотел) \n\nУ тебя в команде уже 5 человек, и все они пойдут по тому же пути, что и ты. \nУ них появятся свои партнеры, а ты с их покупок будешь зарабатывать, потому что это сетевой маркетинг) \n\nЗдесь все зарабатывают друг на друге в глубину до бесконечности, и кайфуют)))\n\nТаким образом, твой доход за месяц работы будет минимум 10 000₽", reply_markup=markup)
    bot.register_next_step_handler(msg, step9)

def step9(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('СМОТРЕТЬ МАРКЕТИНГ')
    markup.add(itembtn1)

    msg = bot.send_message(message.chat.id, "Пришло время знакомиться) \n\n Меня зовут Аня. Я занимаюсь сетевым бизнесом через интернет, и в моей команде ты получишь все необходимые инструменты для работы, а если конкретно, то: \n\n - у тебя будет такой же бот \n- другие боты (я постоянно делаю новые) \n- уроки по привлечению трафика в бота \n- уроки по работе через сторис, рилс, телеграмм канал \n- уроки по работе с программами для автоматизации\n\nПредлагаю посмотреть маркетинг план компании, чтобы понимать, откуда здесь деньги", reply_markup=markup)
    bot.register_next_step_handler(msg, step10)

def step10(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('РЕГИСТРАЦИЯ В ПЕРВУЮ ЛИНИЮ')
    itembtn2 = types.KeyboardButton('НАПИСАТЬ ПОСЛЕ РЕГИ')
    markup.add(itembtn1,itembtn2)
    bot.send_message(message.chat.id, "https://youtu.be/DycYU7A86D8")
    bot.send_message(message.chat.id, "Пока ты изучаешь маркетинг план, сразу предлагаю дальнейшее развитие событий: \n\n1. Регистрируешься в нашу команду \n2. Активируешь контракт \n3. Получишь доступ к обучению \n4. По видео урокам настраиваешь бота и начинаешь привлекать трафик \n5. Закрываешь статусы и получаешь деньги \n\nПосле регистрации обязательно напиши мне (кнопка ниже), я добавлю тебя в наши чаты и начнём бомбить!", reply_markup=markup)









@bot.message_handler(content_types=["text"])
def send_help(message):
    if message.text == "РЕГИСТРАЦИЯ В ПЕРВУЮ ЛИНИЮ":
        bot.send_message(message.from_user.id, "https://ewaproduct.com/ref/23119")
    elif message.text == "НАПИСАТЬ ПОСЛЕ РЕГИ":
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
