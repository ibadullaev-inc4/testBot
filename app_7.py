from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Введите ваш токен, полученный от @BotFather
TOKEN = '6835434697:AAGqcQMGuziJbsfBu65sPoRDzcaJY0J3w-I'

# Обычная клавиатура с одной кнопкой "Menu"
main_menu_keyboard = [['Menu']]
main_menu_markup = ReplyKeyboardMarkup(main_menu_keyboard, resize_keyboard=True)

# Inline-клавиатура для команд меню
menu_keyboard = [
    [InlineKeyboardButton("Start", callback_data='start')],
    [InlineKeyboardButton("Help", callback_data='help')],
    [InlineKeyboardButton("Echo", callback_data='echo')]
]
inline_markup = InlineKeyboardMarkup(menu_keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Привет! Я твой бот. Чем могу помочь?',
        reply_markup=main_menu_markup
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Выберите команду:',
        reply_markup=inline_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Напиши /start, чтобы начать.')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'start':
        await query.edit_message_text(text="Привет! Я твой бот. Чем могу помочь?")
    elif query.data == 'help':
        await query.edit_message_text(text="Напиши /start, чтобы начать.")
    elif query.data == 'echo':
        await query.edit_message_text(text="Эхо-команда выбрана. Напишите сообщение для эхо.")

async def handle_menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await menu(update, context)

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.Regex('^Menu$'), handle_menu_command))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
