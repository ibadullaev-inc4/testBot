from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Введите ваш токен, полученный от @BotFather
TOKEN = '6835434697:AAGqcQMGuziJbsfBu65sPoRDzcaJY0J3w-I'

# Определим inline-кнопки для меню
menu_keyboard = [
    [InlineKeyboardButton("Start", callback_data='start')],
    [InlineKeyboardButton("Help", callback_data='help')],
    [InlineKeyboardButton("Echo", callback_data='echo')]
]
inline_markup = InlineKeyboardMarkup(menu_keyboard)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Выберите команду:',
        reply_markup=inline_markup
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я твой бот. Чем могу помочь?')

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

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CallbackQueryHandler(button))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
