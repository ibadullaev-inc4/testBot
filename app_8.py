from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Replace with your bot token
TOKEN = '6835434697:AAGqcQMGuziJbsfBu65sPoRDzcaJY0J3w-I'

# Inline keyboard with a single "Menu" button, aligned to the left and colored blue
main_menu_markup = InlineKeyboardMarkup([
    [InlineKeyboardButton("Menu", callback_data='menu')],
], resize_keyboard=True)

# Inline keyboard for menu commands
inline_markup = InlineKeyboardMarkup([
    [InlineKeyboardButton("Start", callback_data='start')],
    [InlineKeyboardButton("Help", callback_data='help')],
    [InlineKeyboardButton("Echo", callback_data='echo')],
])

# Handler for /start command
def start(update: Update, context) -> None:
    update.message.reply_text(
        'Привет! Я твой бот. Чем могу помочь?',
        reply_markup=main_menu_markup
    )

# Handler for /menu command
def menu(update: Update, context) -> None:
    update.callback_query.message.reply_text(
        'Выберите команду:',
        reply_markup=inline_markup
    )

# Handler for /help command
def help_command(update: Update, context) -> None:
    update.message.reply_text('Напиши /start, чтобы начать.')

# Handler for /echo command
def echo(update: Update, context) -> None:
    update.message.reply_text(update.message.text)

# Handler for button presses
def button(update: Update, context) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'menu':
        menu(update, context)
    elif query.data == 'start':
        query.edit_message_text(text="Привет! Я твой бот. Чем могу помочь?")
    elif query.data == 'help':
        query.edit_message_text(text="Напиши /start, чтобы начать.")
    elif query.data == 'echo':
        query.edit_message_text(text="Эхо-команда выбрана. Напишите сообщение для эхо.")

# Main function to start the bot
def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("echo", echo))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
