import requests
from googletrans import Translator
from telethon import events
from telethon.tl.types import User

from userbot import CMD_HELP, LOGS, bot
from userbot.events import register
from userbot.utils import edit_or_reply

translator = Translator()
LANGUAGE = "id"

aktifnya_chat_bot = []

url = "https://api-tede.herokuapp.com/api/chatbot?message={message}"


async def ngapain_rep(message):
    hayulo_link_apa = url.format(message=message)
    try:
        data = requests.get(hayulo_link_apa)
        if data.status_code == 200:
            return (data.json())["msg"]
        else:
            LOGS.info("ERROR: API chatbot sedang down, report ke @tedesupport.")
    except Exception:
        LOGS.info("ERROR: {str(e)}")


async def chat_bot_toggle(db, event):
    status = event.pattern_match.group(1).lower()
    chat_id = event.chat_id
    if status == "on":
        if chat_id not in db:
            db.append(chat_id)
            return await edit_or_reply(event, "ChatBot Diaktifkan!")
        await edit_or_reply(event, "ChatBot Sudah Diaktifkan.")
    elif status == "off":
        if chat_id in db:
            db.remove(chat_id)
            return await edit_or_reply(event, "ChatBot Dinonaktifkan!")
        await edit_or_reply(event, "ChatBot Sudah Dinonaktifkan.")
    else:
        await edit_or_reply(event, "**Usage:**\n.chatbot <on/off>")


@register(outgoing=True, pattern=r"^\.chatbot(?: |$)(.*)")
async def on_apa_off(event):
    await chat_bot_toggle(aktifnya_chat_bot, event)


@bot.on(events.NewMessage(incoming=True))
async def tede_chatbot(event):
    sender = await event.get_sender()
    if not isinstance(sender, User):
        return
    if event.chat_id not in aktifnya_chat_bot:
        return
    if event.text and event.is_reply:
        rep = await ngapain_rep(event.message.message)
        tr = translator.translate(rep, LANGUAGE)
        if tr:
            await event.reply(tr.text)


CMD_HELP.update(
    {
        "chatbot": "**Plugin : **`chatbot`\
      \n\n  •  **Syntax :** `.chatbot` <on/off>\
      \n  •  **Function :** buat chatbot\
      "
    }
)
