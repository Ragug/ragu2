from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"How to use this bot ? /n ➡️ Just share youtube video link to the bot /n ➡️ Then bot analyse the video and it ask you to select size of the file to download /n ➡️ Then select the size of the file and then bot prepare to download /n ✨ To get TELEGRAM STICKER pack the link in on my INSTAGRAM Story Highlights /nClick the link here https://www.instagram.com/ragug19?r=nametag /nCurrently Only supports Youtube Single  (No playlist) Just Send Youtube Url"
    await message.reply_text(helptxt)
