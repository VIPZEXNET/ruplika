<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ruplika - کتابخانه پایتون برای روبیکا</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            color: white;
            padding: 60px 20px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 20px;
            margin-bottom: 40px;
            backdrop-filter: blur(10px);
        }

        .header h1 {
            font-size: 3.5rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }

        .header p {
            font-size: 1.4rem;
            opacity: 0.9;
            max-width: 600px;
            margin: 0 auto;
        }

        .badges {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 30px 0;
            flex-wrap: wrap;
        }

        .badge {
            background: rgba(255, 255, 255, 0.2);
            padding: 10px 20px;
            border-radius: 25px;
            font-size: 0.9rem;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        .content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }

        .card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
        }

        .card h2 {
            color: #4a5568;
            margin-bottom: 20px;
            font-size: 1.5rem;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }

        .card ul {
            list-style-type: none;
            padding-right: 20px;
        }

        .card li {
            margin-bottom: 12px;
            position: relative;
            padding-right: 25px;
        }

        .card li:before {
            content: "✓";
            position: absolute;
            right: 0;
            color: #48bb78;
            font-weight: bold;
        }

        .code-section {
            background: #2d3748;
            color: #e2e8f0;
            padding: 25px;
            border-radius: 10px;
            margin: 20px 0;
            font-family: 'Courier New', monospace;
            overflow-x: auto;
        }

        .code-section pre {
            margin: 0;
        }

        .code-comment {
            color: #a0aec0;
        }

        .code-keyword {
            color: #f56565;
        }

        .code-string {
            color: #68d391;
        }

        .code-function {
            color: #63b3ed;
        }

        .btn {
            display: inline-block;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            font-size: 1.1rem;
            margin: 10px 5px;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }

        .btn-secondary {
            background: linear-gradient(135deg, #ed8936, #dd6b20);
        }

        .installation {
            text-align: center;
            margin: 40px 0;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }

        .feature-item {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 15px;
        }

        .footer {
            text-align: center;
            color: white;
            padding: 40px 20px;
            margin-top: 60px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 20px;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2.5rem;
            }
            
            .content {
                grid-template-columns: 1fr;
            }
            
            .badges {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧩 Ruplika</h1>
            <p>کتابخانه کامل و قدرتمند پایتون برای ساخت ربات‌های روبیکا</p>
            
            <div class="badges">
                <div class="badge">نسخه ۳.۱.۲</div>
                <div class="badge">پایتون ۳.۶+</div>
                <div class="badge">لایسنس MIT</div>
                <div class="badge">API روبیکا</div>
            </div>
        </div>

        <div class="installation">
            <h2 style="color: white; margin-bottom: 20px;">📦 نصب کتابخانه</h2>
            <div class="code-section">
                <pre><code>pip install ruplika</code></pre>
            </div>
            <div style="margin-top: 20px;">
                <a href="#quick-start" class="btn">شروع سریع</a>
                <a href="#features" class="btn btn-secondary">امکانات</a>
            </div>
        </div>

        <div class="content">
            <div class="card">
                <h2>🚀 ویژگی‌های اصلی</h2>
                <ul>
                    <li>پشتیبانی کامل از API روبیکا</li>
                    <li>مدیریت پیشرفته پیام‌ها</li>
                    <li>انواع دکمه‌های اینلاین</li>
                    <li>سیستم هندلر ماژولار</li>
                    <li>پشتیبانی از پولینگ و وب‌هوک</li>
                    <li>آپلود و ارسال فایل</li>
                    <li>مستندات کامل</li>
                    <li>مدیریت خطاهای پیشرفته</li>
                </ul>
            </div>

            <div class="card">
                <h2>📚 امکانات فنی</h2>
                <ul>
                    <li>اتصال کامل به تمام متدهای API</li>
                    <li>مدل‌های داده جامع</li>
                    <li>انواع داده پیشرفته (Enum)</li>
                    <li>پشتیبانی از نظرسنجی</li>
                    <li>ارسال موقعیت مکانی</li>
                    <li>مدیریت مخاطبین</li>
                    <li>ویرایش و حذف پیام</li>
                    <li>فوروارد پیام</li>
                </ul>
            </div>
        </div>

        <div id="quick-start" class="card">
            <h2>⚡ شروع سریع</h2>
            <p style="margin-bottom: 20px; color: #4a5568;">یک بات ساده در کمتر از ۵ خط کد:</p>
            
            <div class="code-section">
                <pre><code><span class="code-keyword">from</span> <span class="code-function">ruplika</span> <span class="code-keyword">import</span> Bot

<span class="code-comment"># ایجاد نمونه بات</span>
bot = Bot(<span class="code-string">"YOUR_BOT_TOKEN"</span>)

<span class="code-comment"># هندلر دستور start</span>
@bot.command_handler(<span class="code-string">"start"</span>)
<span class="code-keyword">def</span> <span class="code-function">start_handler</span>(message):
    bot.send_message(
        message.chat_id, 
        <span class="code-string">"🎉 به بات خوش آمدید!"</span>
    )

<span class="code-comment"># اجرای بات</span>
bot.run_polling()</code></pre>
            </div>
        </div>

        <div class="card">
            <h2>🎯 مثال پیشرفته</h2>
            <p style="margin-bottom: 20px; color: #4a5568;">باتی با دکمه‌های اینلاین و مدیریت پیام:</p>
            
            <div class="code-section">
                <pre><code><span class="code-keyword">from</span> <span class="code-function">ruplika</span> <span class="code-keyword">import</span> Bot, Button

bot = Bot(<span class="code-string">"YOUR_BOT_TOKEN"</span>)

<span class="code-comment"># ساخت دکمه‌های اینلاین</span>
buttons = [
    [[(<span class="code-string">"btn1"</span>, <span class="code-string">"📞 تماس"</span>), (<span class="code-string">"btn2"</span>, <span class="code-string">"ℹ️ درباره ما"</span>)]],
    [[(<span class="code-string">"btn3"</span>, <span class="code-string">"🛍 محصولات"</span>)]]
]

@bot.command_handler(<span class="code-string">"start"</span>)
<span class="code-keyword">def</span> <span class="code-function">start_handler</span>(message):
    bot.send_message_with_buttons(
        message.chat_id,
        <span class="code-string">"لطفا یک گزینه انتخاب کنید:"</span>,
        buttons
    )

@bot.inline_handler
<span class="code-keyword">def</span> <span class="code-function">button_handler</span>(inline_message):
    <span class="code-keyword">if</span> inline_message.button_id == <span class="code-string">"btn1"</span>:
        bot.send_message(inline_message.chat_id, <span class="code-string">"📞 شماره تماس: ۰۲۱-۱۲۳۴۵۶۷۸"</span>)

bot.run_polling()</code></pre>
            </div>
        </div>

        <div id="features" class="features-grid">
            <div class="feature-item">
                <div class="feature-icon">🔧</div>
                <h3>نصب آسان</h3>
                <p>نصب با یک خط دستور</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon">⚡</div>
                <h3>کارایی بالا</h3>
                <p>پردازش سریع پیام‌ها</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon">🛡️</div>
                <h3>امنیت</h3>
                <p>مدیریت خطا و اعتبارسنجی</p>
            </div>
            <div class="feature-item">
                <div class="feature-icon">📖</div>
                <h3>مستندات</h3>
                <p>راهنمای کامل و مثال‌های متنوع</p>
            </div>
        </div>

        <div class="footer">
            <h3>📞 ارتباط با ما</h3>
            <p>برای سوالات و پیشنهادات می‌توانید با ما در ارتباط باشید</p>
            <div style="margin-top: 20px;">
                <a href="https://github.com/yourusername/ruplika" class="btn">GitHub</a>
                <a href="https://pypi.org/project/ruplika" class="btn btn-secondary">PyPI</a>
            </div>
            <p style="margin-top: 30px; opacity: 0.8;">© 2024 Ruplika - کتابخانه پایتون برای روبیکا</p>
        </div>
    </div>

    <script>
        // اسکرول نرم برای لینک‌ها
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // افکت برای کارت‌ها هنگام اسکرول
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // اعمال افکت روی تمام کارت‌ها
        document.querySelectorAll('.card, .feature-item').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });
    </script>
</body>
</html>
