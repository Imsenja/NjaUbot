from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/c298f860e4c5e47a33e09.jpg",
                caption="🐊 **Senja Userbot Has Been Actived**!!\n━━━━━━━━━━━━━\n⌬ **Userbot Version** - 8.0@Senja-Userbot\n━━━━━━━━━━━━━\n⌬ **Powered By:** @Itsmesenjaaah ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/Itsmesenjah"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
