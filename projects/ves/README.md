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
- SQLite local persistence با تراکنش و کنترل optimistic concurrency
- فرم‌های typed و اعتبارسنجی فیلدهای اجباری، نوع، محدوده و enum
- رجیستری اولیه 14 نوع کارت، 12 نوع بورد، 10 حالت نمایش و 5 Deck آماده
- crosswalk ماشین‌خوان شناسه‌های EKTA با تست تطبیق رجیستری
- نمونه اولیه مرورگری: Board، Gallery جست‌وجوپذیر، Deck Library، Inspector، ذخیره محلی و خروجی JSON
- قراردادهای JSON Schema، تست واحد و اسناد مهندسی و کاربری

## اجرای سریع
از مسیر projects/ves ابتدا وابستگی تست را نصب کن:

    python -m pip install -e ".[dev]"

سپس:

    python -m unittest discover -s tests -v

برای نمونه بصری، فایل web/index.html را در مرورگر مدرن باز کن. در صورت محدودیت مرورگر:

    python -m http.server 8000 --directory web

سپس http://127.0.0.1:8000 را باز کن.

## نقشه اسناد
- docs/PRODUCT_SPEC.md — مشخصات محصول
- docs/ARCHITECTURE.md — معماری
- docs/DATA_MODEL.md — مدل داده
- docs/UX_SYSTEM.md — UX و تعامل
- docs/CARD_LIBRARY.md و docs/CATALOG.md — کارت، بورد، View و Deck
- docs/FORMS.md — فرم‌ساز و اعتبارسنجی
- docs/PERSISTENCE.md — ذخیره‌سازی محلی
- docs/TAXONOMY_CROSSWALK.md — اتصال taxonomy به EKTA
- docs/MVP_PLAN.md — برنامه MVP و معیار پذیرش
- docs/OPEN_SOURCE_REGISTER.md — مخازن متن‌باز و استانداردها
- docs/EKTA_INTEGRATION.md — اتصال به EKTA
- docs/ORCHESTRATION.md — گردش کار توسعه و گیت‌های تحویل
- docs/INSTALLATION.md و docs/USER_GUIDE.md — راهنمای اجرا و کاربری
- docs/GOVERNANCE.md و docs/STATUS.md — حاکمیت و وضعیت

VES در EKTA ثبت شده اما Runtime آن مستقل است. هیچ داده canonical در EKTA به‌صورت خودکار تغییر نمی‌کند.
