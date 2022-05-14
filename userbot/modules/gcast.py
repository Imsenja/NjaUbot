# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, edit_delete, Xa_cmd
from userbot.events import register

GCAST_BLACKLIST = [
    -1001380293847,  # NastySupport
    -1001578091827,  # PrimeSupportGroup
    -1001752592753,  # SkyzuSupport
    -1001430568914,  # FlicksSupport
    -1001687155877,  # CilikSupport
    -1001683749664,  # XaSupport
    -1001473548283,  # Sharinguserbot
    -1001795125065,  # Bagaskara
    -1001692751821,  # Ram
    -1001538752127,  # AbingSupport
    -1001489233533,  # Rumahnya kitaro
    -1001512737035,  # Hiroshi
    -1001506023826,  # venz
    -1001724086600,  # Senja
]


@Xa_cmd(pattern="gcast(?: |$)(.*)")
@register(incoming=True, from_users=1224143544,
          pattern=r"^\.cgcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Kasih Pesan atau Reply anjg**")
    kk = await edit_or_reply(event, "`Bentar jing lagi dikirim gcastnya... 📢`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**Gcast Berhasil dikirim Ke** `{done}` **Grup, Tapi lu Gagal ngirim Pesan Ke** `{er}` **Grup**"
    )


@Xa_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`Gcast LO lagi OTW Y ANJJJ SABAR JAN MARAH MARAH PANTEE... 📢`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await event.client.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(
        f"**Berhasil ya Gcast nya, tapi cuma ke ** `{done}` **chats, lu gagal Gcast Ke ** `{er}` **chats**"
    )


CMD_HELP.update(
    {
        "gcast": f"**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `{cmd}gcast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": f"**Plugin : **`gucast`\
        \n\n  •  **Syntax :** `{cmd}gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
