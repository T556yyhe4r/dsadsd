from functools import wraps
from config.config import MUST_JOIN
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant


def must_join_channel(func):
    @wraps(func)
    async def sz_message(_, message):
        try:
            await message._client.get_chat_member(MUST_JOIN, message.from_user.id)
            if MUST_JOIN.isalpha():          
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await message._client.get_chat(MUST_JOIN)
                link = chat_info.invite_link
        except UserNotParticipant:
            return await message.reply(
                    f"๐ฝูุฌุจ ุงู ุชุดุชุฑู ูู ูููุงุฉ ุงูุจูููุชโฌ๏ธ\n\n[โยฆ ููููุงุฉ ุณูููุฑุณ๏ธ ุงูุงุบููุงููู](https://t.me/UUU_C_1)\nููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููู\n**๐คูููุงุฉ ุงููุจููุช โฌ๏ธ** @{MUST_JOIN} ยป\nููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููููู\n๐ฅยฆุญุชู ุชุชููู ูู ุงุณุชุฎุฏุงูู\nโ ุงุดุชุฑู ุซู ุงุถุบุท ยซ /play ูุงูุงุบููู ยป ูุฑู ุงุฎุฑูโ\n\n๐ยฆ By ||[โ ๐ฒ๐พ๐๐ณ๐๐ฐ [๐ฐ๐ป๐บ๐ฐ๐ฑ๐ด๐] ๐ฐ๐๐บ๐๐ผ๐บ](https://t.me/COUDRA_1)||",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ุงุถูุบุท ููุง ููุฃุดุชูุฑุงู ุจูููุงุฉ ุงูุจููุชโ", url=f"https://t.me/{MUST_JOIN}"),
                            ],
                            [
                                InlineKeyboardButton("โ ๐ฒ๐พ๐๐ณ๐๐ฐ [๐ฐ๐ป๐บ๐ฐ๐ฑ๐ด๐] ๐ฐ๐๐บ๐๐ผ๐บ", url=f"https://t.me/COUDRA_1"),
                            ] 
                         ] 
                      ) 
                   ) 
        return await func(_, message)    
    return sz_message
