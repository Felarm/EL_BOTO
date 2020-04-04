import telebot
from text_to_speech import TextToSpeech

bot = telebot.TeleBot('')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text', 'audio', 'document'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    else:
        tts = TextToSpeech(text=message.text, lang='ru')
        ogg_file = tts.save()
        with open(ogg_file, 'rb') as f:
            bot.send_voice(message.chat.id, f)

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
