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
                    InlineKeyboardButton('🛃 ᴅᴇᴠᴇʟᴏᴘᴇʀ 2', url='https://t.me/HonorsTeam')],
                   [ InlineKeyboardButton('🛂 ꜱᴜᴘᴘᴏʀᴛ ', url='https://t.me/HRBsupport')],
                   [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
                ]
            )
        )

elif data == "media":
        await query.message.edit_text(
            text = f"<b>ᴍᴇɴᴜ ᴍᴇᴅɪᴀ\nꜰᴏʟʟᴏᴡ ᴜꜱ ꜱᴏᴄɪᴀʟ ᴍᴇᴅɪᴀ ᴏꜰꜰɪᴄɪᴀʟ",disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🌐 ᴡᴇʙꜱɪᴛᴇ', url='https://px-z.blogspot.com'),
                InlineKeyboardButton('📱 ɪɴꜱᴛᴀɢʀᴀᴍ', url='https://Instagram.com/pxz_official'),
                 InlineKeyboardButton('📲 ᴡʜᴀᴛꜱᴀᴘᴘ', url='https://whatsapp.com/channel/0029Vaj27FHLo4hWYvLaUM00')],
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
            ]
                )
        )

elif data == "shop":
        await query.message.edit_text(
            text = f"<b>ᴍᴇɴᴜ ꜱʜᴏᴘ\nʏᴏᴜ ᴡᴀɴᴛ ʙᴜʏ ᴠɪᴘ?, ᴄʟɪᴄᴋ ʙᴜᴛᴛᴏɴ ɪɴ ʙᴇʟᴏᴡ",disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [
                 InlineKeyboardButton('💰 ꜱᴛᴏʀᴇ ', url='https://t.me/HRBstore_official'),
                 InlineKeyboardButton('🚪 ɢʀᴏᴜᴘ ', url='https://t.me/+lasI21TGYKFmODk1')],
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
            ]
                )
        )


elif data == "menu":
        await query.message.edit_text(
            text = f"<b>ᴍᴇɴᴜ ꜰᴇᴀᴛᴜʀᴇᴅ",disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🛒 ᴘʀᴏᴍᴏᴛɪᴏɴ ", callback_data="shop"),
                 InlineKeyboardButton('💰 ꜱᴛᴏʀᴇ ', url='promotion')],
              [InlineKeyboardButton('🔐 ᴘʀᴇᴍɪᴜᴍ ᴠɪᴘ ', url='premium'),
              InlineKeyboardButton("⚖️ ᴅᴏɴᴀᴛᴇ ", callback_data="donate")],
                
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                 
            ]
                )
        )
    
    elif data == "donate":
        await query.message.edit_text(
            text = f"<b>DONATE - PXZFamily</b>\nJika kalian suka sama video yang kami bagikan secara gratis/bayaran, ingin berbagi (donasi) kepada PXZteam? Silahkan pilih via donasi\n If you like the videos we share for free/paid, want to share (donate) to PXZteam? Please choose via donation",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
              [  InlineKeyboardButton('🧾 ꜱᴀᴡᴇʀɪᴀ', url='https://saweria.co/PXZsupport'),
                InlineKeyboardButton('🧾 ᴘᴀʏᴘᴀʟ', url='https://paypal.me/PEXLAND')
          ],
                [InlineKeyboardButton('📤 ᴜᴘʟᴏᴀᴅᴇᴅ', url='https://t.me/HRBpay')],
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
                
            ])            
        )
    elif data == "premium":
        await query.message.edit_text(
            text = f"<b>List To Be Premium of PXZVip\n<blockquote>100 video 5k\n200 video 10k\n300 video 15k\n400 video 20k\n500 video 25k\n600 video 30k\n\nIF YOU WANT BUY VIP, PLEASE CONTACT</blockquote></b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🔓 ꜱᴀᴡᴇʀɪᴀ', url='https://saweria.co/PXZsupport'),
                InlineKeyboardButton('🔓 ᴘᴀʏᴘᴀʟ', url='https://paypal.me/PEXLAND')],
                [InlineKeyboardButton('🛂 ᴄᴏɴᴛᴀᴄᴛ', url='https://t.me/HonorsTeam')],
                [InlineKeyboardButton('📤 ᴜᴘʟᴏᴀᴅᴇᴅ', url='https://t.me/HRBpay')],
                [InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")]
            ])            
        )
    elif data == "promotion":
        await query.message.edit_text(
            text = f"<b>IF YOU WANT PROMOTION VIDEO/PHOTO/ETC CONTACT STORE TEAM👇</b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('🤖 ᴄᴏɴᴛᴀᴄᴛ', url='https://t.me/HonorsTeam'),
                InlineKeyboardButton('📤 ᴜᴘʟᴏᴀᴅᴇᴅ', url='https://t.me/HRBpromotion')],
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
