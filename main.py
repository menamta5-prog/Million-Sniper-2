import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from google import genai

# قراءة المفاتيح من المتغيرات السرية
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# إعداد العميل لـ Gemini
client = genai.Client(api_key=GEMINI_API_KEY)

# أمر /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 أهلاً بك في بوت Million Sniper 2!\nالبوت متصل بـ Gemini وجاهز للرد على استفساراتك.")

# معالجة الرسائل وإرسالها لـ Gemini
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    try:
        # إرسال النص لـ Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_text,
        )
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {str(e)}")

def main():
    if not TELEGRAM_TOKEN or not GEMINI_API_KEY:
        print("خطأ: يرجى التأكد من إضافة TELEGRAM_TOKEN و GEMINI_API_KEY")
        return

    # إنشاء وتطبيق البوت
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 البوت يعمل الآن ويستمع للرسائل...")
    app.run_polling()

if __name__ == "__main__":
    main()
      
