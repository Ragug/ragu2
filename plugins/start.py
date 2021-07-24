from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("telegram sticker", url="https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTc2ODU0NzI4Mzk4MjY5?utm_medium=copy_link")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://www.instagram.com/ragug19?r=nametag")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info and how to use"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
