from time import sleep
from platform import uname
from userbot import ALIVE_NAME, WEATHER_DEFCITY, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG GOBLOKK!!!**")
# Pantun


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Salam Dulu Biar Sopan...`")
    sleep(2)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Salam


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Kalo Orang Salam Itu Dijawab...`")
    sleep(2)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Menjawab Salam


@register(outgoing=True, pattern="^.kenalin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `Obam Gila`")
    sleep(2)
    await typew.edit("✅ `Obam Gila`")
    sleep(1)
    await typew.edit("☑️ `Rendi Stress`")
    sleep(2)
    await typew.edit("✅ `Rendi Stress`")
    sleep(1)
    await typew.edit("☑️ `Pulud Gajelas`")
    sleep(2)
    await typew.edit("✅ `Pulud Gajelas`")
    sleep(1)
    await typew.edit("☑️ `Shiro Wibu Sangean`")
    sleep(2)
    await typew.edit("✅ `Shiro Wibu Sangean`")
    sleep(1)
    await typew.edit("☑️ `Cary Autis`")
    sleep(2)
    await typew.edit("✅ `Cary Autis`")
    sleep(1)
    await typew.edit("`⚡ Cuma Rio Yang Paling Waras, Baik Hati, Dan Tidak Sombong.`")
# King Userbot Support


@register(outgoing=True, pattern="^.la(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `Obam Owner Sadis`")
    sleep(1)
    await typew.edit("✅ `Obam Owner Sadis`")
    sleep(2)
    await typew.edit("☑️ `Tika Gila`")
    sleep(1)
    await typew.edit("✅ `Bela Gila`")
    sleep(2)
    await typew.edit("☑️ `Ana Babi`")
    sleep(1)
    await typew.edit("✅ `Alip Babi`")
    sleep(2)
    await typew.edit("☑️ `Alip Ayah Pekerja Keras`")
    sleep(1)
    await typew.edit("✅ `Alip Ayah Pekerja Keras`")
    sleep(2)
    await typew.edit("☑️ `Aca Gaje`")
    sleep(1)
    await typew.edit("✅ `Aca Gaje`")
    sleep(2)
    await typew.edit("✨ `Cuma Rio Yang Paling Sopan, Baik Hati, Dan Tidak Sombong.`")
# Luar Angkasa


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Heh Kamu Gaboleh Begitu...`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")
# Istigfar


@register(outgoing=True, pattern="^.perkenalan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja`")
# Perkenalan


CMD_HELP.update(
    {
        "gabut": "**Modules** - `Gabut`\
        \n\n Cmd : `.l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `.perkenalan`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `.la`\
        \nUsage : Luar Angkasa\
        \n\n Cmd : `.g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `.kenalin`\
        \nUsage : Awokwok\
        \n\n Cmd : `.p`\
        \nUsage : Untuk Memberi Salam\
    "
    }
)
