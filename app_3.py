from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Введите ваш токен, полученный от @BotFather
TOKEN = '6835434697:AAGqcQMGuziJbsfBu65sPoRDzcaJY0J3w-I'

# Определим меню
menu_keyboard = [
    ['Option_1_1', 'Option_1_2', 'Option_1_3', 'Option_1_4', ],
    ['Option_2_1', 'Option_2_2', 'Option_2_3', 'Option_2_4', ],
    ['Option_3_1', 'Option_3_2', 'Option_3_3', 'Option_3_4', ],
    ['Option_4_1', 'Option_4_2', 'Option_4_3', 'Option_4_4', ],
    ['Option_5_1', 'Option_5_2', 'Option_5_3', 'Option_5_4', ],
    
]

reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True, one_time_keyboard=False)

async def start_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Привет! Выберите опцию:',
        reply_markup=reply_markup
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Обработчик всех текстовых сообщений для отображения меню
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start_menu))

    # Обработчик эхо-сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()

if __name__ == '__main__':
    main()
