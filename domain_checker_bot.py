import whois as pywhois
import validators
import datetime
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace with your bot token
BOT_TOKEN = "your_bot_token"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("👋 Send me a domain like `example.com` to check if it's legit.")

def check_domain(update: Update, context: CallbackContext):
    domain = update.message.text.strip()

    if not validators.domain(domain):
        update.message.reply_text("❌ That doesn't look like a valid domain. Try again.")
        return

    try:
        w = pywhois.whois(domain)
        created = w.creation_date
        registrar = w.registrar or "Unknown"

        if isinstance(created, list):
            created = created[0]

        if created:
            age_days = (datetime.datetime.now() - created).days
            age_status = "✅ Domain looks established." if age_days > 180 else "⚠️ Newly registered. Be cautious."
            response = f"""🔍 Domain: {domain}
- Registered: ✅
- Created on: {created.strftime('%Y-%m-%d')}
- Registrar: {registrar}
- Age: {age_days} days
- {age_status}"""
        else:
            response = f"""🔍 Domain: {domain}
- Registered: ❓ Unknown
- Could not retrieve creation date.
- Registrar: {registrar}"""

    except Exception as e:
        response = f"❌ Couldn't retrieve info for `{domain}`. It may not be registered or is invalid."

    update.message.reply_text(response)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, check_domain))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
