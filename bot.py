import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Logging untuk debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Fungsi untuk perintah /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Halo! Bot Anda sudah aktif. 🎉")

# Fungsi utama untuk menjalankan bot
async def main():
    TOKEN = "7635188447:AAE-0gWseDjE5gHlLwgM8XKyz_w2rS8WZ0Y"  # Ganti dengan token bot Anda dari BotFather

    # Membuat aplikasi bot
    application = Application.builder().token(TOKEN).build()

    # Menambahkan handler untuk perintah /start
    application.add_handler(CommandHandler("start", start))

    # Menjalankan bot
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
