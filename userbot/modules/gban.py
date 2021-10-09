from telethon.events import ChatAction
from userbot import ALIVE_NAME, CMD_HELP, bot
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.events import register
from telethon.tl.types import MessageEntityMentionName


async def get_full_user(event):
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Ini Tidak Mungkin Tanpa ID Pengguna`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("`Terjadi Kesalahan... Mohon Lapor Ke Grup` @riogroupsupport", str(err))
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj
# Ported For Kaisar-userbot by kenkanasw/KEN KAN


@bot.on(ChatAction)
async def handler(tele):
    if tele.user_joined or tele.user_added:
        try:
            from userbot.modules.sql_helper.gmute_sql import is_gmuted

            guser = await tele.get_user()
            gmuted = is_gmuted(guser.id)
        except BaseException:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await tele.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                tele.chat_id, guser.id, view_messages=False
                            )
                            await tele.reply(
                                f"**Master, Pengguna Gban Telah Bergabung** \n"
                                f"**Pengguna**: [{guser.id}](tg://user?id={guser.id})\n"
                                f"**Aksi**  : `Banned`"
                            )
                        except BaseException:
                            return


@register(outgoing=True, pattern="^.gban(?: |$)(.*)")
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`Mengaktifkan Perintah Global Banned!`")
    else:
        dark = await dc.edit("`Memproses Global Banned Pengguna Ini ヅ`")
    me = await userbot.client.get_me()
    await dark.edit(f"`Global Banned Akan Segera Aktif, Anda Akan Dibanned Secara Global ヅ`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit(f"`Terjadi Kesalahan ヅ`")
    if user:
        if user.id == 1890868167:
            return await dark.edit(
                f"`Anda Tidak Bisa Melakukan Global Banned Ke Rio, Dia Adalah Pembuat Saya ヅ`"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(f"`Global Banned Aktif ✅`")
            except BaseException:
                b += 1
    else:
        await dark.edit(f"`Mohon Balas Ke Pesan Kaisar`")
    try:
        if gmute(user.id) is False:
            return await dark.edit(f"**Kesalahan! Pengguna Ini Sudah Kena Perintah Global Banned Kaisar.**")
    except BaseException:
        pass
    return await dark.edit(
        f"┏━━━━━━༻❁༺━━━━━━┓\n 𝙍𝙄𝙊 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 \n┣━━━━━━༻❁༺━━━━━━┛\n┣ 💌 **𝙋𝙀𝙍𝙄𝙉𝙏𝘼𝙃 :**\n┣ ↪ `{ ALIVE_NAME}`\n┣━━━━━━━━━━━━━━━━━━\n┣ 👥 **𝙋𝙀𝙉𝙂𝙂𝙐𝙉𝘼 :** [{user.first_name}](tg://user?id={user.id})\n┣ 🏃 **𝘼𝙆𝙎𝙄 :** `𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙`\n┗━━━━━━༻❁༺━━━━━━┛")


@register(outgoing=True, pattern="^.ungban(?: |$)(.*)")
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɢʟᴏʙᴀʟ ʙᴀɴɴᴇᴅ ᴘᴇɴɢɢᴜɴᴀ ɪɴɪ ヅ`")
    else:
        dark = await dc.edit("`Membatalkan Perintah Global Banned ヅ`")
    me = await userbot.client.get_me()
    await dark.edit(f"`ᴍᴇᴍᴜʟᴀɪ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɢʟᴏʙᴀʟ ʙᴀɴɴᴇᴅ, ᴘᴇɴɢɢᴜɴᴀ ɪɴɪ ᴀᴋᴀɴ ᴅᴀᴘᴀᴛ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ɢʀᴜᴘ ᴀɴᴅᴀ `")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("`Terjadi Kesalahan ヅ`")
    if user:
        if user.id == 1353102497:
            return await dark.edit("**ᴋᴀᴍᴜ ᴛɪᴅᴀᴋ ʙɪꜱᴀ ᴛᴇʀᴋᴇɴᴀ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ, ᴋᴀʀɴᴀ ᴅɪᴀ ᴘᴇᴍʙᴜᴀᴛᴋᴜ **")
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit(f"`ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ɢʟᴏʙᴀʟ ʙᴀɴɴᴇᴅ... ᴍᴇᴍᴘʀᴏꜱᴇꜱ... `")
            except BaseException:
                b += 1
    else:
        await dark.edit("`Harap Balas Ke Pesan Pengguna ヅ`")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**Kesalahan! Pengguna Sedang Tidak Di Global Banned.**")
    except BaseException:
        pass
    return await dark.edit(
        f"┏━━━━━━༻❁༺━━━━━━┓\n  𝙍𝙄𝙊 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 \n┣━━━━━━༻❁༺━━━━━━┛\n┣ 💌 **𝙋𝙀𝙍𝙄𝙉𝙏𝘼𝙃 :**\n┣ ↪ `{ ALIVE_NAME}`\n┣━━━━━━━━━━━━━━━━━━\n┣ 👥 **𝙋𝙀𝙉𝙂𝙂𝙐𝙉𝘼 :** [{user.first_name}](tg://user?id={user.id})\n┣ 🏃 **𝘼𝙆𝙎𝙄 :** `𝙈𝙚𝙢𝙗𝙖𝙩𝙖𝙡𝙠𝙖𝙣 𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙`\n┗━━━━━━༻❁༺━━━━━━┛")



CMD_HELP.update({
    "gban": "\
**Modules:** __Global Banned__\n\n**Perintah:** `.gban`\
\n**Penjelasan:** Melakukan Banned Secara Global Ke Semua Grup Dimana Kaisar Sebagai Admin.\
\n\n**Perintah:** `.ungban`\
\n**Penjelasan:** Membatalkan Global Banned"})
