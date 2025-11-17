#!/usr/bin/env python3
"""
بات ساده اکو - Ruplika 3.1.2
"""

from ruplika import Bot, Button, ButtonTypeEnum

# ایجاد نمونه بات
bot = Bot("YOUR_BOT_TOKEN_HERE")

@bot.command_handler("start")
def start_handler(message):
    """هندلر دستور /start"""
    # ساخت دکمه‌های ساده
    buttons = [
        [("help", "📖 راهنما"), ("about", "ℹ️ درباره ما")],
        [("contact", "📞 تماس با ما")]
    ]
    
    welcome_text = """
🎉 به بات اکو خوش آمدید!

🔸 این یک بات نمونه است که پیام‌های شما را تکرار می‌کند.

📝 دستورات موجود:
/start - شروع کار
/help - راهنمایی
/about - درباره بات

✨ هر پیامی بفرستید، آن را تکرار می‌کنم!
    """
    
    bot.send_message_with_buttons(
        chat_id=message.chat_id,
        text=welcome_text,
        buttons=buttons
    )

@bot.command_handler("help")
def help_handler(message):
    """هندلر دستور /help"""
    help_text = """
📖 راهنمای بات اکو:

• هر پیام متنی که بفرستید، بات آن را برای شما بازمی‌گرداند.
• از دکمه‌های زیر می‌توانید استفاده کنید.
• برای شروع مجدد از /start استفاده کنید.

🛠 توسعه‌دهندگان:
این بات با کتابخانه ruplika نسخه ۳.۱.۲ ساخته شده است.
    """
    
    bot.send_message(
        chat_id=message.chat_id,
        text=help_text
    )

@bot.command_handler("about")
def about_handler(message):
    """هندلر دستور /about"""
    about_text = """
🤖 بات اکو

نسخه: ۱.۰.۰
کتابخانه: ruplika 3.1.2

🔸 این یک بات نمایشی است که قابلیت‌های کتابخانه ruplika را نشان می‌دهد.

📚 امکانات:
• پاسخ به دستورات
• ارسال دکمه‌های اینلاین
• پردازش پیام‌های متنی
• مدیریت خطا
    """
    
    bot.send_message(
        chat_id=message.chat_id,
        text=about_text
    )

@bot.inline_handler
def inline_button_handler(inline_message):
    """هندلر کلیک روی دکمه‌های اینلاین"""
    if inline_message.button_id == "help":
        help_handler_type(inline_message)
    elif inline_message.button_id == "about":
        about_handler_type(inline_message)
    elif inline_message.button_id == "contact":
        contact_handler(inline_message)

def help_handler_type(inline_message):
    """هندلر دکمه راهنما"""
    bot.send_message(
        chat_id=inline_message.chat_id,
        text="📖 برای راهنمایی از دستور /help استفاده کنید."
    )

def about_handler_type(inline_message):
    """هندلر دکمه درباره ما"""
    bot.send_message(
        chat_id=inline_message.chat_id,
        text="ℹ️ برای اطلاعات بیشتر از دستور /about استفاده کنید."
    )

def contact_handler(inline_message):
    """هندلر دکمه تماس"""
    contact_text = """
📞 اطلاعات تماس:

• ایمیل: support@example.com
• تلفن: ۰۲۱-۱۲۳۴۵۶۷۸
• آدرس: تهران، خیابان نمونه

🕒 ساعات کاری:
شنبه تا چهارشنبه: ۸:۰۰ تا ۱۷:۰۰
پنجشنبه: ۸:۰۰ تا ۱۴:۰۰
    """
    
    bot.send_message(
        chat_id=inline_message.chat_id,
        text=contact_text
    )

@bot.message_handler
def echo_handler(message):
    """هندلر اصلی برای پیام‌های متنی"""
    if message.text and not message.text.startswith('/'):
        # تکرار پیام کاربر
        response = f"📨 شما گفتید: {message.text}"
        bot.send_message(
            chat_id=message.chat_id,
            text=response
        )

@bot.update_handler
def log_updates(update_data):
    """هندلر برای لاگ کردن تمام آپدیت‌ها"""
    print(f"📥 آپدیت دریافتی: {update_data.get('type')}")

if __name__ == "__main__":
    try:
        # دریافت اطلاعات بات
        bot_info = bot.get_bot_info()
        print(f"🤖 بات @{bot_info.username} راه‌اندازی شد!")
        print(f"📝 نام بات: {bot_info.bot_title}")
        print(f"🔸 توضیحات: {bot_info.description}")
        
        # اجرای بات
        bot.run_polling(interval=1)
        
    except KeyboardInterrupt:
        print("\n⏹ بات متوقف شد")
    except Exception as e:
        print(f"❌ خطا در اجرای بات: {e}")