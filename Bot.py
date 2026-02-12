import json
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = "توکن_جدیدت_اینجا"
ADMIN_ID = 5972276401

logging.basicConfig(level=logging.INFO)

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.web_app_data:
        data = json.loads(update.message.web_app_data.data)

        if data["type"] == "wallet_connected":
            text = (
                f"🔗 اتصال کیف پول جدید\n\n"
                f"👤 User ID: {data['user_id']}\n"
                f"📥 Wallet:\n{data['wallet']}"
            )
            await context.bot.send_message(chat_id=ADMIN_ID, text=text)

        elif data["type"] == "withdraw_request":
            text = (
                f"💸 درخواست برداشت جدید\n\n"
                f"👤 User ID: {data['user_id']}\n"
                f"💰 Amount: {data['amount']} TON\n"
                f"📥 Wallet:\n{data['wallet']}"
            )
            await context.bot.send_message(chat_id=ADMIN_ID, text=text)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))

app.run_polling()
