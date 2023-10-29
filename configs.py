# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "23562768"))
	API_HASH = os.environ.get("1b40c01ae078463626e1b4e8fe78e3a5")
	BOT_TOKEN = os.environ.get("6678356956:AAErFaEqRqmP28kQV2jlBT6TtOBs40Vu4Zo")
	BOT_USERNAME = os.environ.get("Zero2filestorebot")
	DB_CHANNEL = int(os.environ.get("-1001984137290", "-1001583779155"))
	BOT_OWNER = int(os.environ.get("1078225192", "1339262764"))
	DATABASE_URL = os.environ.get("mongodb+srv://k7c7i:P4ATAn0S6f4smn4u@cluster0.bu2dbgw.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("-1001825264509", "-1001506710273")
	LOG_CHANNEL = os.environ.get("-1001878894820", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/Zero2filestorebot)

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @Ur_core_i9

👥 **Support Group:** [COMPRESSOR GROUP](https://t.me/compress480p)

📢 **Updates Channel:** [MAIN NETWORK](https://t.me/All_Senpai_network)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @Ur_core_i9

Developer is Super Noob. Just Learning from Official Docs. Please support the developer by joining main network to keep services alive

	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
