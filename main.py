import telebot
import compliments
import apiKey

bot = telebot.TeleBot(apiKey.apiKey())

@bot.message_handler(commands=['start'])
def main(message):
    compliment = compliments.compliment()
    bot.send_message(message.chat.id, 'Напиши мне что угодно, когда нужна поддержка')

@bot.message_handler()
def info(message):
    compliment = compliments.compliment()
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет! {compliment}')
    else:
        bot.send_message(message.chat.id, compliment)

bot.polling(none_stop=True)