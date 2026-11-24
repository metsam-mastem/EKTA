# VES — Visual Engineering Studio

**Universal Visual Engineering Workbench** — محیط مستقل و local-first برای مدل‌سازی، طراحی بصری، ترکیب، اعتبارسنجی و مستندسازی سیستم‌های فیزیکی و دیجیتال.

## تصمیم‌های تثبیت‌شده
- Scope: Universal
- Visual: Hybrid (مهندسی دقیق + بوردگیم + Canvas آزاد)
- Interaction: All (کارت، نمودار، گراف، فرم و Canvas)
- Platform: Cross-platform (Web، Windows، Android)
- Priority: معماری جامع با توسعه مرحله‌ای

## محتویات نسخه 0.1.0
- مدل دامنه مستقل از Renderer برای Project، Entity، Relationship، Board و Placement
- اعتبارسنجی قطعی و گزارش Finding با کد و شدت
- Import/Export JSON نسخه‌دار و حفظ شناسه‌ها در Round-trip
- نمونه اولیه مرورگری بدون وابستگی خارجی: کارت‌های قابل جابه‌جایی، Inspector، ذخیره محلی و خروجی JSON
- قراردادهای JSON Schema، تست واحد، معماری، UX، کتابخانه کارت‌ها، فهرست OSS و اسناد کاربری

## اجرای سریع
از مسیر projects/ves:
    
    python -m unittest discover -s tests -v

برای نمونه بصری، فایل web/index.html را در مرورگر مدرن باز کن. در صورت محدودیت مرورگر:
    
    python -m http.server 8000 --directory web

سپس http://127.0.0.1:8000 را باز کن.

## مرزهای نسخه 0.1
این نسخه یک vertical slice اولیه است؛ هنوز پشتیبانی کامل SysML v2، UML، BPMN، EDA/CAD، شبیه‌سازی، همکاری چندکاربره، Plugin Sandbox، بسته Windows/Android و QA خودکار مرورگر پیاده‌سازی نشده‌اند.

## نقشه اسناد
- docs/PRODUCT_SPEC.md — مشخصات محصول
- docs/ARCHITECTURE.md — معماری
- docs/DATA_MODEL.md — مدل داده
- docs/UX_SYSTEM.md — UX و تعامل
- docs/CARD_LIBRARY.md — کتابخانه کارت و بورد
- docs/MVP_PLAN.md — برنامه MVP و معیار پذیرش
- docs/OPEN_SOURCE_REGISTER.md — مخازن متن‌باز و استانداردها
- docs/EKTA_INTEGRATION.md — اتصال به EKTA
- docs/INSTALLATION.md و docs/USER_GUIDE.md — راهنمای اجرا و کاربری
- docs/GOVERNANCE.md و docs/STATUS.md — حاکمیت و وضعیت

VES در EKTA ثبت شده اما Runtime آن مستقل است. هیچ داده canonical در EKTA به‌صورت خودکار تغییر نمی‌کند.
