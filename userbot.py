from telethon import TelegramClient, events

# Telegram API ma'lumotlaringiz
api_id = 37543024
api_hash = "f2d08efbe13188958338cda784899b7d"

client = TelegramClient("userbot", api_id, api_hash)

AUTO_REPLY = "Salom! Hozir bandman. Tez orada javob beraman. 🙂"

# Bir odamga faqat bir marta javob berish uchun
replied_users = set()

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    if not event.is_private:   # Faqat shaxsiy chatlarda
        return

    sender = await event.get_sender()

    # O'zingizga javob bermaslik
    if sender.bot or sender.id == (await client.get_me()).id:
        return

    # Bir foydalanuvchiga faqat bir marta javob berish
    if sender.id in replied_users:
        return

    replied_users.add(sender.id)
    await event.reply(AUTO_REPLY)

client.start()
print("Userbot ishga tushdi.")
client.run_until_disconnected()
