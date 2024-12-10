from telegram import __version__ as tg_version
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7314304305:AAEYGb3qEbnNUAEp_Fd7XCZNMS8D7b7zTZQ"
GAME_URL = "https://danilreznickyi.github.io/clumsy-bird/"  # Link to your game

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = (
        "Welcome to Clumsy Bird 🎮\n\n"
        "Press the button below to launch the game directly in Telegram!"
    )
    # Check Telegram library version
    if tg_version < "20.0":
        await context.bot.send_message(chat_id=chat_id, text="Please update the library!")
        return

    keyboard = [
        [
            InlineKeyboardButton(
                text="Launch Clumsy Bird", web_app={"url": GAME_URL}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
