from instabot import Bot

# your credentials
name = "Your username"
password = "Your password"


# create object of Bot
bot = Bot()

# login
b.login(username=name, password=password)

# get user info
user_id = bot.get_user_id_from_username("mengelmoestuintjes")