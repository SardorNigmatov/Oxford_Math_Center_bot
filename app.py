from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, BotCommand, KeyboardButton, ChatAction, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import dotenv_values
config = dotenv_values(".env")
TOKEN = config.get(('TOKEN'))
ADMIN_ID = config.get('ADMIN_ID')
def start_command(update,context):
    commands = [
        BotCommand(command='start',description='botni ish tushirish'),
        BotCommand(command='help',description='tilni o\'zgartirish'),
        BotCommand(command='info',description='ma\'lumot olish'),
    ]

    buttons = [
        [KeyboardButton(text="O'zbekcha"),KeyboardButton(text='Русский')]
    ]

    context.bot.set_my_commands(commands=commands)
    update.message.reply_text(text=f"Xush kelibsiz! {update.message.from_user.first_name}",reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True))

def info_command(update,context):
    buttons = [
        [InlineKeyboardButton(text='"OXFORD math center" NTM',url='https://t.me/Oxford_math_center1')],
        [InlineKeyboardButton(text='Yangiyo\'l matematiklari',url='https://t.me/yangiyol_matematiklari')]
    ]
    update.message.reply_photo(
        photo=open('photos/logo.jpg','br'),
        caption="Bu \"Oxford Math center\" o'quv markazining shaxsiy boti.\nBundan foydalanib siz kurslarimiz haqida ma'lumot olishingiz."
                "\n\nЭто персональный бот учебного центра Оксфордского математического центра.Используя это, вы получите информацию о наших курсах.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def menu_handler(update,context):
        if context.user_data['lang'] == 'O\'zbekcha':
            buttons = [
                [KeyboardButton(text="Yangiyo\'l filiali(Lamonosov maktabi yonida)"),KeyboardButton(text="Gulbahor filiali")],
            ]
            update.message.reply_text(
                text='Filialni tanlang:',
                reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True)
            )
        else:
            buttons = [
                [KeyboardButton(text="Янгиюльский филиал (рядом со школой Ламоносова)"),
                 KeyboardButton(text="Филиал Гульбахар")],
            ]
            update.message.reply_text(
                text='Выбрать филиал',
                reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
            )



# Yangiyo'l
def courses_yangiul_handler(update,context):
    if context.user_data['lang'] == 'O\'zbekcha':
        buttons = [
            [KeyboardButton(text='Yangiyo\'ldagi manzilimiz'),KeyboardButton(text='Yangiyo\'ldagi kurslarimiz')],
            [KeyboardButton(text='Ortga')]
        ]
        update.message.reply_text(
            text='Tanlang:',reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True)
        )
    else:
        buttons = [
            [KeyboardButton(text='Наш адрес на Янгиюле'), KeyboardButton(text='Наши курсы в Янгиюле')],
            [KeyboardButton(text="Назад")]
        ]
        update.message.reply_text(
            text='Выбрать:', reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
        )


def yangiyul_filial_handler(update,context):
    if context.user_data['lang'] == 'O\'zbekcha':
        buttons = [
            [KeyboardButton(text='Matematika'),KeyboardButton(text='Ingliz tili')],
            [KeyboardButton(text='Fizika'),KeyboardButton(text='IELTS(Ingliz tili)')],
            [KeyboardButton(text='IT(Kompyuter savodxonligi)'),KeyboardButton(text='Rus tili')],
            [KeyboardButton(text='Bosh sahifa'),]

        ]
        update.message.reply_text(text='Kurslarimiz:',reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True))
    else:
        buttons = [
            [KeyboardButton(text='Mатематика'), KeyboardButton(text='Английский язык')],
            [KeyboardButton(text='Физика'), KeyboardButton(text='IELTS(английский язык)')],
            [KeyboardButton(text='IT(Kомпьютерная грамотность)'), KeyboardButton(text='Русский язык')],
            [KeyboardButton(text='Главная страница'), ]

        ]
        update.message.reply_text(text='Наши курсы:', reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True,one_time_keyboard=True))


#Gulbahor


def courses_gulbahor_handler(update,context):
    if context.user_data['lang'] == 'O\'zbekcha':
        buttons = [
            [KeyboardButton(text='Gulbahordagi manzilimiz'),KeyboardButton(text='Gulbahordagi kurslarimiz')],
            [KeyboardButton(text="Ortga")]
        ]
        update.message.reply_text(
            text='Tanlang:',reply_markup=ReplyKeyboardMarkup(buttons,resize_keyboard=True,one_time_keyboard=True)
        )
    else:
        buttons = [
            [KeyboardButton(text='Наш адрес в Gulbahar'), KeyboardButton(text='Наши курсы в Gulbahar')],
            [KeyboardButton(text="Назад")]
        ]
        update.message.reply_text(
            text='Выбрать:', reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
        )




def message_hanler(update,context):
    message = update.message.text
    user_id = update.message.chat.id
    query = update.callback_query

    if message == "O'zbekcha":
        context.user_data['lang'] = "O'zbekcha"
        menu_handler(update,context)
    elif message == 'Yangiyo\'l filiali(Lamonosov maktabi yonida)':
        courses_yangiul_handler(update,context)
    elif message == 'Yangiyo\'ldagi manzilimiz':
        update.message.reply_text(text="Bizning mazilimiz:")
        context.bot.send_location(chat_id=user_id, latitude=41.12138, longitude=69.06092)
    elif message == 'Yangiyo\'ldagi kurslarimiz':
        yangiyul_filial_handler(update, context)
    elif message in ['Matematika','Ingliz tili','Fizika','IELTS(Ingliz tili)','IT(Kompyuter savodxonligi)','Rus tili']:
        update.message.reply_text(
           text="<b>Dars kunlari</b>:\n1.Dushanba, Chorshanba, Juma.\n2.Seshanba, Payshanba, Shanba.\n<b>Dars vaqtlari</b>:\n8:00 - 09:30, 09:30-11:00, 11:00-12:30,14:00-15:30,\n15:30-17:00, 17:00-18:30, 18:30-20:00.\n<b>Dars davomiyligi</b>: 1 soat 30 min", parse_mode='html'
        )
    elif message == 'Gulbahor filiali':
        courses_gulbahor_handler(update,context)
    elif message == 'Gulbahordagi manzilimiz':
        update.message.reply_text(text='Bizning manzilimiz')
        context.bot.send_location(chat_id=user_id,latitude=41.075347,longitude=69.023686)
    elif message == 'Gulbahordagi kurslarimiz':
        yangiyul_filial_handler(update,context)
    elif message == 'Bosh sahifa':
        menu_handler(update, context)
    ##################################################################################################################
    elif message == "Русский":
        context.user_data['lang'] = "Русский"
        menu_handler(update,context)
    elif message == 'Янгиюльский филиал (рядом со школой Ламоносова)':
        courses_yangiul_handler(update,context)
    elif message == 'Наш адрес на Янгиюле':
        update.message.reply_text(text="Наш мазил:")
        context.bot.send_location(chat_id=user_id, latitude=41.12138, longitude=69.06092)
    elif message == 'Наши курсы в Янгиюле':
        yangiyul_filial_handler(update, context)
    elif message in ['Mатематика','Английский язык','Физика','IELTS(английский язык)','IT(Kомпьютерная грамотность)','Русский язык']:
        update.message.reply_text(
           text="<b>Дни занятий</b>:\n1.Понедельник, Среда, Пятница.\n2.Вторник, Четверг, Суббота.\n<b>Время занятий</b>:\n8:00 - 09:30, 09:30-11:00, 11:00-12:30,14:00-15:30,\n15:30-17:00, 17:00-18:30, 18:30-20:00.\n<b>Продолжительность урока</b>: 1 час 30 минут", parse_mode='html'
        )
    elif message == 'Филиал Гульбахар':
        courses_gulbahor_handler(update,context)
    elif message == 'Наш адрес в Gulbahar':
        update.message.reply_text(text='Наш мазил')
        context.bot.send_location(chat_id=user_id,latitude=41.075347,longitude=69.023686)
    elif message == 'Наши курсы в Gulbahar':
        yangiyul_filial_handler(update,context)
    elif message == 'Главная страница':
        menu_handler(update, context)
    elif message in ['Ortga','Назад']:
        menu_handler(update, context)




def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    #commands
    dispatcher.add_handler(CommandHandler('start',start_command))
    dispatcher.add_handler(CommandHandler('info',info_command))
    dispatcher.add_handler(CommandHandler('help',start_command))

   #MessageHandler
    dispatcher.add_handler(MessageHandler(Filters.text,message_hanler))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()