# from instabot import Bot

# bot = Bot()
# bot.login",use_cookie=False)


# bot.follow("turk.elon.musk")

# bot.follow("elonmusk")
# bot.follow("beingsalmankhan")
# bot.like_user("beingsalmankhan", amount=3, randomize=True)
# from instabot import Bot

# # Remove old cookie files to prevent login issues
# import os
# if os.path.exists("config"):
#     import shutil
#     shutil.rmtree("config")

# # Initialize bot (no unsupported arguments)
# bot = Bot()

# # Login
# bot.login(",use_cookie=False)

# # Example actions
# # bot.upload_photo("photo.jpg", caption="Hello from Instabot!")
# bot.follow("beingsalmankhan")  

from instagrapi import Client

cl = Client()
cl.login()  # replace with your real password

username = "beingsalmankhan"

# Get user ID
user_id = cl.user_id_from_username(username)

# Follow the user
result = cl.user_follow(user_id)

print(result)  # True if successfully followed
