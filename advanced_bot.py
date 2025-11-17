#!/usr/bin/env python3
"""
بات پیشرفته - نمایش قابلیت‌های Ruplika 3.1.2
"""

from ruplika import Bot, Button, ButtonTypeEnum, ButtonSelectionItem, ButtonSelectionTypeEnum

bot = Bot("YOUR_BOT_TOKEN_HERE")

def create_main_menu():
    """ایجاد منوی اصلی با انواع دکمه"""
    # دکمه‌های ساده
    profile_btn = bot.create_simple_button("profile", "👤 پروفایل")
    settings_btn = bot.create_simple_button("settings", "⚙️ تنظیمات")
    
    # دکمه انتخاب محصولات
    products_items = [
        bot.create_selection_item("📱 گوشی موبایل"),
        bot.create_selection_item("💻 لپ‌تاپ"),
        bot.create_selection_item("🎧 هدفون"),
        bot.create_selection_item("⌚ ساعت هوشمند"),
    ]
    
    products_btn = bot.create_selection_button(
        button_id="products",
        text="🛍 محصولات",
        selection_id="products_list",
        items=products_items,
        title="انتخاب محصول",
        columns_count="2"
    )
    
    # دکمه‌های سرویس
    support_btn = bot.create_simple_button("support", "🎫 پشتیبانی")
    location_btn = Button(
        id="location",
        type=ButtonTypeEnum.LOCATION,
        button_text="📍 موقعیت ما"
    )
    
    return bot.create_keypad([
        [profile_btn, settings_btn],
        [products_btn],
        [support_btn, location_btn]
    ])

@bot.command_handler("start")
def start_command(message):
    """دستور شروع بات پیشرفته"""
    keypad = create_main_menu()
    
    welcome_text = """
🚀 به بات پیشرفته خوش آمدید!

این بات قابلیت‌های زیر را ارائه می‌دهد:
• منوی تعاملی با دکمه‌های مختلف
• لیست‌های انتخاب
• دریافت موقعیت مکانی
• پشتیبانی آنلاین

لطفا یک گزینه را انتخاب کنید:
    """
    
    bot.send_message(
        chat_id=message.chat_id,
        text=welcome_text,
        inline_keypad=keypad
    )

@bot.inline_handler
def handle_inline_clicks(inline_message):
    """مدیریت کلیک روی دکمه‌ها"""
    button_id = inline_message.button_id
    
    if button_id == "profile":
        show_profile(inline_message.chat_id)
    
    elif button_id == "settings":
        show_settings(inline_message.chat_id)
    
    elif button_id == "support":
        show_support(inline_message.chat_id)
    
    elif button_id == "location":
        send_location(inline_message.chat_id)
    
    elif button_id == "products":
        # این برای دکمه انتخاب، پاسخ در هندلر جداگانه مدیریت می‌شود
        pass

def show_profile(chat_id):
    """نمایش پروفایل کاربر"""
    profile_text = """
👤 پروفایل کاربر

• نام: کاربر نمونه
• عضویت: ۳۰ روز پیش
• امتیاز: ⭐⭐⭐⭐☆ (۴.۲)
• وضعیت: فعال

🎯 آمار فعالیت:
• پیام‌های ارسالی: ۱۲۷
• دستورات استفاده شده: ۲۳
• مدت استفاده: ۱۵ ساعت
    """
    
    bot.send_message(chat_id, profile_text)

def show_settings(chat_id):
    """نمایش تنظیمات"""
    settings_text = """
⚙️ تنظیمات بات

🔔 اعلان‌ها:
✓ دریافت نوتیفیکیشن
✓ اعلان پیام‌های جدید
✗ اعلان به روزرسانی‌ها

🌐 زبان:
• فارسی (پیشفرض)

🔒 حریم خصوصی:
• نمایش اطلاعات محدود
• عدم ذخیره پیام‌ها

برای تغییر تنظیمات با پشتیبانی تماس بگیرید.
    """
    
    bot.send_message(chat_id, settings_text)

def show_support(chat_id):
    """نمایش اطلاعات پشتیبانی"""
    support_text = """
🎫 پشتیبانی آنلاین

📞 تماس تلفنی:
۰۲۱-۱۲۳۴۵۶۷۸

📧 ایمیل:
support@company.com

🕒 ساعات کاری:
شنبه تا چهارشنبه: ۸:۰۰-۱۷:۰۰
پنجشنبه: ۸:۰۰-۱۴:۰۰

💬 پیام فوری:
برای پاسخ سریع‌تر، پیام خود را مستقیما ارسال کنید.
    """
    
    # ایجاد دکمه‌های پشتیبانی
    buttons = [
        [("call", "📞 تماس"), ("email", "📧 ایمیل")],
        [("back", "🔙 بازگشت")]
    ]
    
    bot.send_message_with_buttons(
        chat_id=chat_id,
        text=support_text,
        buttons=buttons
    )

def send_location(chat_id):
    """ارسال موقعیت مکانی"""
    # موقعیت نمونه (تهران)
    bot.send_location(
        chat_id=chat_id,
        latitude="35.715298",
        longitude="51.404343",
        text="📍 موقعیت دفتر مرکزی ما در تهران"
    )

@bot.message_handler
def handle_messages(message):
    """مدیریت پیام‌های متنی"""
    if message.text and not message.text.startswith('/'):
        # پاسخ به پیام‌های متنی
        response = f"""
📩 پیام شما دریافت شد:

"{message.text}"

✅ این پیام توسط تیم پشتیبانی بررسی خواهد شد.

برای بازگشت به منوی اصلی از /start استفاده کنید.
        """
        
        bot.send_message(
            chat_id=message.chat_id,
            text=response
        )

if __name__ == "__main__":
    print("🚀 بات پیشرفته در حال راه‌اندازی...")
    
    try:
        bot_info = bot.get_bot_info()
        print(f"✅ بات @{bot_info.username} آماده است!")
        print("🔸 از Ctrl+C برای توقف استفاده کنید")
        
        bot.run_polling(interval=1)
        
    except KeyboardInterrupt:
        print("\n⏹ بات متوقف شد")
    except Exception as e:
        print(f"❌ خطا: {e}")