import telebot


bot=telebot.TeleBot('790777539:AAE64sE4Z_PMx13ccogiCBCc0dwhNmqSSlk')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['fine'])
def send_welcome(message):
    bot.reply_to(message,"i am also fine")
    
@bot.message_handler(commands=['where are you from','help'])
def send_welcome(message):
    bot.reply_to(message,"i am from kerala")

@bot.message_handler(commands=['cool','help'])
def send_welcome(message):
    bot.reply_to(message,":)")
    
@bot.message_handler(commands=['how old are you ','help'])
def send_welcome(message):
    bot.reply_to(message,"my age is divisible by 2 and 6")
    
@bot.message_handler(commands=['i guess your age is 18 ','help'])
def send_welcome(message):
    bot.reply_to(message,"you are brillant .yes:))")

@bot.message_handler(commands=['my age is 20','help'])
def send_welcome(message):
    bot.reply_to(message,"nice)")

@bot.message_handler(commands=['bye talk to you later','help'])
def send_welcome(message):
    bot.reply_to(message,"bye.nice talking to you")


bot.polling()
