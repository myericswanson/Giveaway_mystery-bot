from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8151298356:AAGFimTJRXZqfdaoYY3-Q_pC8tQ38Q1jU9k"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💵 Mystery Box 1", callback_data="cash"),
         InlineKeyboardButton("📱 Mystery Box 2", callback_data="iphone")],
        [InlineKeyboardButton("💻 Mystery Box 3", callback_data="laptop"),
         InlineKeyboardButton("🚗 Mystery Box 4", callback_data="car")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎁 Choose a mystery box to reveal your prize:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    choice = query.data
    if choice == "cash":
        text = "🎉 Congratulations! You found 💵 *$10,000 Cash!*"
    elif choice == "iphone":
        text = "🎉 Congratulations! You won a brand new 📱 *iPhone!*"
    elif choice == "laptop":
        text = "🎉 Congratulations! You got a powerful 💻 *Laptop!*"
    elif choice == "car":
        text = "🎉 Congratulations! You discovered a 🚗 *Car!*"
    else:
        text = "Oops! Something went wrong."
    await query.edit_message_text(text=text, parse_mode="Markdown")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot is running...")
    app.run_polling()
