from InternetSpeedTwitter import InternetSpeedTwitterBot

PROMISED_DOWN = 50
PROMISED_UP = 50

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if float(bot.up) < PROMISED_UP or float(bot.down) < PROMISED_DOWN:
    msg = f'Hey Internet Provider, I am getting {bot.down}down/{bot.up}up, when I am paying for {PROMISED_DOWN}down/{PROMISED_UP}up.'
    bot.tweet_at_provider(msg)
