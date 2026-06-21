import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import requests

# আপনার টেলিগ্রাম বট টোকেন এখানে বসান
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Enter 10 digit number:")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    
    if len(user_input) == 10 and user_input.isdigit():
        msg = await update.message.reply_text(f"Search 🔍 {user_input}\n\nPlease wait...")
        
        # API Call
        api_url = f"https://anishexploits.com/api/api.php?key=KEY_DEBB0D78_DEMOKA&type=number&num={user_input}"
        
        try:
            response = requests.get(api_url).text
            await context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=msg.message_id, text=f"Result:\n\n{response}")
        except Exception as e:
            await context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=msg.message_id, text="Error fetching data!")
    else:
        await update.message.reply_text("Please enter a valid 10 digit number.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()
