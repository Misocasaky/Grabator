from telegram.ext import Application, CommandHandler, MessageHandler, filters
from brain import respond_to_user

TOKEN = "7923579457:AAG4Ab24GEQvkySL4NyHVPDqf4KEtTQleaU"  # توكن Grabator

async def handle_message(update, context):
    user_text = update.message.text
    reply = respond_to_user(user_text)
    await update.message.reply_text(reply)

async def start(update, context):
    await update.message.reply_text("🤖 مرحباً! أنا Grabator، مساعدك الذكي!")

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🚀 Grabator يعمل الآن...")
    app.run_polling()
