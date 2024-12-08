import logging
import asyncio
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

# Fungsi utama
def main():
    TOKEN = "7635188447:AAE-0gWseDjE5gHlLwgM8XKyz_w2rS8WZ0Y"  # Ganti dengan token bot Anda dari BotFather

    # Membuat aplikasi bot
    application = Application.builder().token(TOKEN).build()

    # Menambahkan handler untuk perintah /start
    application.add_handler(CommandHandler("start", start))

    # Menjalankan bot tanpa menggunakan asyncio.run
    try:
        asyncio.get_event_loop().run_until_complete(application.run_polling())
    except RuntimeError:
        # Jika event loop sudah berjalan, gunakan loop saat ini
        loop = asyncio.get_event_loop()
        loop.run_until_complete(application.run_polling())

if __name__ == "__main__":
    main()
