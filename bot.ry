import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 🔥 Я бот ff_addlike_kz\n"
        "Напиши /like чтобы получить лайк"
    )

async def like(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Заявка на лайк принята! ✅")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("like", like))
    print("Bot started...")
    app.run_polling()
