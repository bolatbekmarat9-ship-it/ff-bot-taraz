import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 🔥 Я бот ff_addlike_kz\n\n"
        "Напиши /like чтобы получить лайки"
    )

async def like(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Заявка на лайки принята! ✅ Скоро будет готово.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("like", like))

print("Bot started...")
app.run_polling()
