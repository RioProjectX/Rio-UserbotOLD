from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.mmk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ASTAGAAAA MEMEKNYA ANAK INI!!!!**")


@register(outgoing=True, pattern='^.ek(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EH KONTOOOLL!!!**")


@register(outgoing=True, pattern='^.ya(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**YAUDAH IYAAA SAYANG...**")


@register(outgoing=True, pattern='^.asn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ASTAGFIRULLAH NGENTOOOT!!!**")


@register(outgoing=True, pattern='^.suci(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**LU LAMA-LAMA JADI KEK ANAK HARAM, KEKNYA HARUS GUA BAPTIS. SINI LU NGENTOT GUA BAPTIS BIAR SUCI JIWA LO YANG HARAM ITU!!!**")


@register(outgoing=True, pattern='^.wibu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**LARI CUK ADA WIBU!!!**πππ")


CMD_HELP.update({
    "salam3":
    "πΎπ€π’π’ππ£π: `.asn`\
\nβ³ : Hmmm.\
\n\nπΎπ€π’π’ππ£π: `.mmk`\
\nβ³ : Biasalah.\
\n\nπΎπ€π’π’ππ£π: `.suci`\
\nβ³ : Baptis.\
\n\nπΎπ€π’π’ππ£π: `.wibu`\
\nβ³ : Pake Bila Ketemu Wibu.\
\n\nπΎπ€π’π’ππ£π: `.ek`\
\nβ³ : Coba Aja Sendiri Kontol.\
\n\nπΎπ€π’π’ππ£π: `.ya`\
\nβ³ : Yasaja."
})
