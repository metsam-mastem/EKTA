# EKTA — راهنمای نصب و راه‌اندازی (User Installation)

هدف: نصب Runtime 0.2 و Operational Workspace 0.4 روی رایانه و بازکردن رابط محلی EKTA.  
پیش‌نیاز: USER_SETUP.md.

## 1. روش پیشنهادی: Git Clone

### 1.1 بررسی ابزارها

~~~bash
python --version
git --version
~~~

نسخه Python باید 3.11 یا جدیدتر باشد. در Windows ممکن است به‌جای python از py -3 استفاده کنید.

### 1.2 دریافت مخزن

~~~bash
git clone https://github.com/metsam-mastem/EKTA.git
cd EKTA
~~~

برای دریافت نسخه مشخص، پس از clone شاخه یا Tag موردنظر را checkout کنید. برای استفاده پایدار از main یا یک Release/Commit مشخص استفاده کنید؛ شاخه‌های کاری ممکن است ناپایدار باشند.

## 2. نصب و اجرا در Windows

PowerShell را باز کنید و وارد پوشه مخزن شوید:

~~~powershell
cd EKTA
powershell -ExecutionPolicy Bypass -File scripts/start.ps1
~~~

اسکریپت فعلی مسیر ریشه مخزن را پیدا می‌کند؛ در صورت نبود .venv محیط مجازی می‌سازد؛ پروژه و وابستگی‌های اصلی را با pip install -e . نصب می‌کند؛ سپس Uvicorn را روی 127.0.0.1:8000 اجرا می‌کند.

اگر Python Launcher در سیستم موجود نیست، Python 3.11+ را نصب و مطمئن شوید py -3 در PowerShell کار می‌کند.

## 3. نصب و اجرا در Linux

~~~bash
cd EKTA
sh scripts/start.sh
~~~

در صورت نیاز:

~~~bash
chmod +x scripts/start.sh
./scripts/start.sh
~~~

اسکریپت محیط مجازی .venv را ایجاد می‌کند، وابستگی‌ها را نصب و Uvicorn را اجرا می‌کند.

## 4. نصب و اجرا در macOS

~~~bash
cd EKTA
sh scripts/start.sh
~~~

اگر چند نسخه Python دارید، بررسی کنید python3 --version حداقل 3.11 باشد. اسکریپت از python3 استفاده می‌کند.

## 5. نصب دستی

### Linux / macOS

~~~bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
python -m uvicorn ekta_runtime.api:app --app-dir runtime --host 127.0.0.1 --port 8000
~~~

### Windows PowerShell

~~~powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m uvicorn ekta_runtime.api:app --app-dir runtime --host 127.0.0.1 --port 8000
~~~

برای توسعه و اجرای آزمون‌ها:

~~~bash
python -m pip install -e ".[dev]"
python -m unittest discover -s tests -v
~~~

## 6. بازکردن رابط

پس از مشاهده پیام شروع Uvicorn، مرورگر را باز کنید:

- رابط اصلی: http://127.0.0.1:8000/
- سلامت سرویس: http://127.0.0.1:8000/health
- میزکار عملیاتی: http://127.0.0.1:8000/workspace\n- مستندات تعاملی API: http://127.0.0.1:8000/docs
- قرارداد OpenAPI: http://127.0.0.1:8000/openapi.json

تا زمانی که ترمینال اجراکننده سرور باز است، سرویس فعال می‌ماند. برای توقف، در همان ترمینال Ctrl+C بزنید.

## 7. اجرای مخزن از مسیر دیگر

Runtime مسیر ریشه داده را از متغیر محیطی EKTA_ROOT می‌خواند. این متغیر باید به پوشه‌ای اشاره کند که ساختار canonical EKTA مانند taxonomy/ و encyclopedia/ در آن قرار دارد.

Linux/macOS:

~~~bash
export EKTA_ROOT="$HOME/work/EKTA"
python -m uvicorn ekta_runtime.api:app --app-dir "$HOME/work/EKTA/runtime" --host 127.0.0.1 --port 8000
~~~

PowerShell:

~~~powershell
$env:EKTA_ROOT = "C:\work\EKTA"
python -m uvicorn ekta_runtime.api:app --app-dir "C:\work\EKTA\runtime" --host 127.0.0.1 --port 8000
~~~

## 8. دریافت نسخه جدید

سرور را متوقف کنید. سپس:

~~~bash
git status
git pull --ff-only
~~~

اگر تغییرات محلی دارید، پیش از Pull آن‌ها را Commit یا به‌صورت امن ذخیره کنید. پس از تغییر وابستگی‌ها:

~~~bash
python -m pip install -e .
~~~

سپس سرویس را دوباره اجرا کنید. برای تغییرات ساختاری، CHANGELOG.md را بررسی کنید.

## 9. حذف نصب

1. سرور را با Ctrl+C متوقف کنید.
2. اگر می‌خواهید داده و مخزن را نگه دارید، فقط .venv را حذف کنید.
3. برای حذف کامل نسخه محلی، پوشه clone را حذف کنید؛ این کار روی مخزن GitHub اثر ندارد.
4. فایل‌های شخصی یا تغییرات Commit‌نشده را پیش از حذف پشتیبان‌گیری کنید.

Linux/macOS: rm -rf .venv  
Windows: Remove-Item -Recurse -Force .venv

## 10. امنیت شبکه

اسکریپت‌های فعلی به‌صورت پیش‌فرض روی 127.0.0.1 گوش می‌دهند؛ سرویس برای دسترسی محلی طراحی شده است. آن را بدون احراز هویت روی 0.0.0.0 یا اینترنت عمومی منتشر نکنید. API کاوشگر read-only است؛ API میزکار فقط در staging و draft محلی می‌نویسد. هیچ‌کدام برای استقرار عمومی یا چندکاربره سخت‌سازی نشده‌اند.

## 11. محدودیت نصب

در این نسخه نصب‌کننده MSI/EXE، Docker Compose رسمی، APK/Android app، بسته آفلاین وابستگی‌های Python یا نصب‌کننده یک‌کلیکی منتشر نشده است.

برای خطاها، TROUBLESHOOTING.md را ببینید.
