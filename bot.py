import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Logging untuk debug
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Fungsi untuk perintah /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Halo! Bot Anda sudah aktif.')

def main():
    TOKEN = "YOUR_API_TOKEN"  # Masukkan API Token dari BotFather
    updater = Updater(TOKEN)

    # Daftar handler
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Jalankan bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
