# EKTA — پروتکل تحویل به توسعه‌دهنده و AI Agent

هدف: ادامه مستقل پروژه توسط انسان، تیم یا عامل هوش مصنوعی بدون اتکا به تاریخچه یک مکالمه خاص.

## 1. ترتیب مطالعه

1. README.md
2. docs/PROJECT_CHARTER.md
3. docs/GOVERNANCE.md و docs/CONTEXT_CONTINUITY.md
4. docs/PROJECT_OVERVIEW.md
5. docs/KNOWLEDGE_ARCHITECTURE.md
6. docs/KNOWLEDGE_OPERATING_WORKFLOW.md
7. docs/IMPLEMENTATION_PLAN.md و docs/ROADMAP.md
8. docs/RUNTIME_ARCHITECTURE.md
9. CHANGELOG.md
10. فایل‌های مرتبط در taxonomy/، schemas/، encyclopedia/، runtime/ و tests/

برای وظیفه کاربری، از docs/USER_DOCUMENTATION_INDEX.md شروع کنید.

## 2. پیش از هر تغییر

~~~bash
git status --short
git branch --show-current
git rev-parse HEAD
git log -5 --oneline
~~~

همچنین:
- شاخه اصلی و Commit جاری GitHub را بررسی کنید؛
- PRها، Issueها و GitHub Actions را بررسی کنید؛
- مطمئن شوید فایل یا قابلیت موردنظر قبلاً ایجاد نشده است؛
- ادعاهای مستندات را با کد فعلی تطبیق دهید.

## 3. قواعد غیرقابل مذاکره

- مخزن Git منبع حقیقت پروژه است؛ مکالمه منبع canonical نیست.
- EKTA مستقل است؛ با پروژه دیگری ادغام نشود مگر مجوز صریح ثبت‌شده وجود داشته باشد.
- طراحی، پیاده‌سازی، آزمون و اعتبارسنجی را جدا نگه دارید.
- قابلیت را از روی README یا Roadmap فرض نکنید؛ کد و آزمون را بخوانید.
- شناسه پایدار را تغییر ندهید و دوباره استفاده نکنید.
- رابطه نامعتبر یا unresolved را حدس نزنید.
- مجوز مخزن undecided است؛ مجوز متن‌باز را فرض نکنید.
- Secret، Token و داده محرمانه Commit نکنید.
- تغییرات کوچک، قابل بازبینی و آزمون‌پذیر انجام دهید.
- نتیجه آزمون را فقط وقتی PASS بنویسید که واقعاً اجرا شده باشد.

## 4. چرخه تغییر

1. تعریف مسئله و معیار پذیرش.
2. جست‌وجوی کد، اسناد، Issue و سابقه تغییر.
3. ثبت تصمیم معماری در ADR در صورت اثر گسترده.
4. ایجاد Branch محدود و نام‌گذاری روشن.
5. نوشتن آزمون یا validator متناسب.
6. پیاده‌سازی.
7. اجرای تست‌ها و validatorها.
8. بررسی diff و اثر جانبی.
9. به‌روزرسانی اسناد و Changelog.
10. ساخت Pull Request با شواهد و محدودیت‌ها.
11. بررسی CI و Review.
12. Merge طبق مجوز Maintainer.
13. به‌روزرسانی Context Continuity و وضعیت بعدی.

## 5. اعتبارسنجی پایه

از ریشه مخزن:

~~~bash
python -m pip install -e ".[dev]"
python tools/validate_docs.py
python -m unittest discover -s tests -v
python tools/validate_frontend.py
python tools/build_graph.py
~~~

اگر هر فرمان اجرا نشد، وضعیت آن NOT_RUN است؛ اگر شکست خورد FAIL؛ اگر وابستگی یا مجوز لازم موجود نبود BLOCKED.

## 6. گزارش تحویل مستقل

هر تحویل باید این موارد را ثبت کند:
- هدف و دامنه تغییر؛
- فایل‌های تغییرکرده؛
- Branch، Commit و PR؛
- آزمون‌ها و خروجی دقیق؛
- وضعیت CI؛
- محدودیت‌ها و موارد NOT_RUN؛
- ریسک‌ها و تصمیم‌های باز؛
- کوچک‌ترین گام بعدی.

## 7. شروع از وضعیت نامعلوم

اگر سندها با هم تعارض دارند، هیچ‌کدام را بی‌صدا جایگزین نکنید. منبع، Commit و تاریخ هر دو ادعا را ثبت و برای تصمیم Maintainer ارجاع دهید. مقدار ناشناخته را UNKNOWN نگه دارید.
