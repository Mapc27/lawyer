import telebot
from lawyer import settings


bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN, parse_mode=None)


@bot.message_handler()
def process_all_messages(message):
    bot.reply_to(message, "Я могу только отправлять уведомления")


def send_message(user, message_text: str):
    bot.send_message(user, message_text)


def start_bot():
    bot.infinity_polling()
