#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b> ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ᴘxᴢᴛᴇᴀᴍ</a>\nꜱᴜᴘᴘᴏʀᴛ : <a href='https://t.me/PXZsupport'>ᴘxᴢᴛᴇᴀᴍ ꜱᴜᴘᴘᴏʀᴛ</a>\nꜱᴜᴘᴘᴏʀᴛ ᴜᴘᴅᴀᴛᴇ : <a href='https://t.me/PXZsupport_official'>ᴘxᴢᴛᴇᴀᴍ ꜱᴜᴘᴘᴏʀᴛ ᴜᴘᴅᴀᴛᴇ</a>\nꜱᴛᴏʀᴇ : <a href='https://t.me/PXZstore'>ᴘxᴢꜱᴛᴏʀᴇ </a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('🛃 ᴅᴇᴠᴇʟᴏᴘᴇʀ 1', url='https://t.me/dammingyu'),
                    InlineKeyboardButton('🛃 ᴅᴇᴠᴇʟᴏᴘᴇʀ 2', url='https://t.me/PXZteam')],
                   [ InlineKeyboardButton('🛂 ꜱᴜᴘᴘᴏʀᴛ ', url='https://t.me/PXZsupport')],
                   [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")],
                
                ]
            )
        )
    elif data == "donate":
        await query.message.edit_text(
            text = f"DONATE - PXZFamily\n🪙 https://saweria.co/PXZsupport",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
            ])            
        )
    elif data == "premium":
        await query.message.edit_text(
            text = f"<b>List To Be Premium of PXZVip\n100 video 5k\n200 video 10k\n300 video 15k\n400 video 20k\n500 video 25k\n600 video 30k\n\nIF YOU WANT BUY VIP, PLEASE CONTACT</b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🤖 ᴄᴏɴᴛᴀᴄᴛ", url="https://t.me/pxzstore_official")],
                [
                InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
            ])            
        )
        elif data == "promotion":
        await query.message.edit_text(
            text = f"<b>YOU WANT PROMOTION VIDEO?, SURE WE CAN HELP IT\nSELL VIDEO? PUT PRICE PLEASE CONTACT</b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🤖 ᴄᴏɴᴛᴀᴄᴛ", url="https://t.me/pxzstore_official")],
                [
                InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
            ])            
                )
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
