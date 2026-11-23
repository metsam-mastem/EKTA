# EKTA — راهنمای جامع ورودی‌ها و ورود دانش (Input Guide)

این سند دو مفهوم متفاوت را جدا می‌کند:

1. Search Input: چیزی که کاربر در کادر جست‌وجوی Workbench وارد می‌کند.
2. Knowledge Contribution / Ingestion: داده یا دانشی که قرار است به مخزن canonical افزوده شود.

جست‌وجو در Runtime 0.2 پیاده‌سازی شده است. در Workspace 0.4، Import Center می‌تواند فایل متنی Markdown/YAML/JSON را در staging محلی قرار دهد؛ این عملیات هنوز Knowledge Contribution به canonical محسوب نمی‌شود. انتشار نهایی همچنان از مسیر بازبینی و Git انجام می‌شود.

## 1. انواع ورودی جست‌وجو

### 1.1 متن آزاد
~~~text
runtime
workflow scheduler
embedded controller
~~~

چند واژه آزاد با منطق AND تطبیق داده می‌شوند.

### 1.2 عبارت دقیق
~~~text
"platform runtime"
'engineering knowledge'
~~~

ترتیب واژه‌ها حفظ می‌شود.

### 1.3 هشتگ
~~~text
#runtime
#scheduler
#software-engineering
~~~

هشتگ‌ها از نام، مستعار، شناسه، طبقه‌بندی، heading، مسیر و tagهای موجود استخراج می‌شوند. پوشش تابع متن ایندکس‌شده است.

### 1.4 فیلترهای ساختاری
~~~text
id:EKTA-CON-000001
territory:software-engineering
domain:software-engineering
layer:platform-runtime
type:concept
status:PROPOSED
kind:document
tag:runtime
~~~

مقدارهای چندواژه‌ای را در کوتیشن قرار دهید.

### 1.5 ورودی ترکیبی
~~~text
"workflow runtime" #scheduler territory:software-engineering status:PROPOSED
~~~

ترکیب متن آزاد، عبارت دقیق، هشتگ و فیلترها در یک Query مجاز است.

## 2. قواعد نرمال‌سازی و تطبیق

- حروف Unicode نرمال‌سازی می‌شوند.
- شکل‌های متداول عربی ي و ك به شکل فارسی ی و ک تبدیل می‌شوند.
- فاصله‌های متوالی یکسان‌سازی می‌شوند.
- واژه‌های آزاد به‌صورت AND تطبیق داده می‌شوند.
- فیلترهای ساختاری باید با مقدارهای قابل‌شناسایی در داده/Taxonomy منطبق باشند.
- جست‌وجو در داده‌های ایندکس‌شده انجام می‌شود، نه تمام فایل‌های رایانه.

## 3. چه محتوایی ایندکس می‌شود؟

در Runtime 0.2، شناسنامه‌های canonical در encyclopedia/concepts/ جداگانه بارگذاری می‌شوند. اسناد منتخب Markdown، YAML و JSON نیز در مسیرهای مشخص مانند موارد زیر ایندکس می‌شوند:

- docs/
- maps/
- references/
- research/
- taxonomy/
- schemas/
- templates/
- decision-lab/
- workflows/
- فایل‌های منتخب ریشه مانند README و CHANGELOG

دایرکتوری‌های مخفی، محیط مجازی، build و dist و مسیرهای تولیدی از ایندکس کنار گذاشته می‌شوند. پوشش دقیق تابع تنظیمات runtime/ekta_runtime/search.py است. PDF، DOCX، XLSX، تصاویر، صدا و ویدئو در این نسخه مستقیماً ایندکس نمی‌شوند.

## 4. Import Center و ورودی‌های مرحله‌بندی‌شده

از `/workspace` بخش «مرکز ورود» را باز کنید. پسوندهای مجاز .md، .markdown، .yaml، .yml و .json هستند؛ سقف هر فایل ۱ مگابایت است. فایل در `.ekta/workspace/imports/` ذخیره می‌شود. YAML/JSON با parser امن و Markdown دارای Front Matter از نظر ساختار اولیه بررسی می‌شود. این بررسی، اعتبار Schema یا صحت علمی را تأیید نمی‌کند.

ورودی‌های staging به دانشنامه اضافه یا ایندکس نمی‌شوند. برای انتشار، ابتدا محتوا را بازبینی کنید، شناسه و Schema و Taxonomy و منابع را بررسی کنید، سپس از گردش کار Git استفاده کنید.

## 5. ورودی‌های دانشی قابل ثبت دستی

موارد زیر انواع محتوایی هستند که می‌توانند در مخزن با رکورد مناسب ثبت شوند؛ این‌ها به معنی پشتیبانی از آپلود مستقیم در رابط نیستند:

| نوع محتوا | مقصد معمول | روش فعلی |
|---|---|---|
| مفهوم مهندسی | encyclopedia/concepts/ | Markdown با Front Matter |
| تکنیک/روش | کتابخانه دانش و قالب مربوط | رکورد ساخت‌یافته؛ وجود Schema را بررسی کنید |
| معماری | encyclopedia/ یا نقشه معماری | سند و ارجاع به مفاهیم |
| استاندارد/مشخصات | references/ | فراداده، نسخه، ناشر، URL و محدودیت مجوز |
| مقاله/پژوهش | research/ | اطلاعات کتابشناختی، روش، یافته و محدودیت |
| مخزن نرم‌افزاری | references/ | URL، نسخه/Commit، مجوز، وضعیت نگهداری و ارزیابی |
| تصمیم | decision-lab/ADR/ | ADR با گزینه‌ها، معیارها، شواهد و تصمیم |
| Playbook | execution-lab/ یا workflows/ | مراحل، ورودی/خروجی، ریسک و معیار پذیرش |
| آزمون/نتیجه | کنار رکورد یا مسیر آزمون | روش، محیط، داده، نتیجه و شواهد |

پیش از ساخت فایل، ساختار واقعی مخزن و Templateها را بررسی کنید. پوشه یا Schema خالی به معنی وجود قابلیت کامل آن نوع رکورد نیست.

## 6. ورودی منبع و شواهد

برای هر منبع خارجی، تا حد امکان ثبت کنید:
- عنوان؛
- نویسنده یا ناشر؛
- URL canonical؛
- نوع منبع؛
- تاریخ انتشار/به‌روزرسانی و تاریخ دسترسی؛
- نسخه، Tag یا Commit؛
- مجوز و محدودیت بازاستفاده؛
- ادعاهایی که منبع واقعاً پشتیبانی می‌کند؛
- محدودیت، سوگیری یا عدم قطعیت.

URL به‌تنهایی اثبات‌کننده درستی ادعا نیست. در منابع پویا، نسخه و Commit را ثبت کنید.

## 6. ورودی فایل‌ها: وضعیت فعلی

Runtime 0.2 از فایل‌های متنی منتخب Markdown، YAML و JSON در مسیرهای تعریف‌شده مخزن استفاده می‌کند. شناسنامه‌های مفهوم نیز از فایل‌های canonical بارگذاری می‌شوند.

در UI فعلی وجود ندارد:
- آپلود PDF/DOCX/XLSX؛
- OCR تصویر یا PDF اسکن‌شده؛
- استخراج جدول و نمودار؛
- ASR و استخراج صوت؛
- استخراج فریم ویدئو؛
- crawl خودکار URL یا GitHub؛
- ورود دسته‌ای ZIP؛
- تبدیل خودکار فایل به شناسنامه و رابطه.

این قابلیت‌ها می‌توانند در Roadmap مطرح شوند، اما تا زمان پیاده‌سازی و آزمون نباید به‌عنوان قابلیت نسخه جاری معرفی شوند.

## 7. روش فعلی افزودن مفهوم جدید

1. در Workbench نام، مستعار و موضوع را جست‌وجو کنید تا رکورد تکراری نسازید.
2. فایل‌های templates/ و schemas/ را بررسی کنید.
3. شناسه جدید و غیرتکراری طبق قرارداد مخزن تعیین کنید؛ شناسه موجود را بازاستفاده نکنید.
4. فایل Markdown شناسنامه را در encyclopedia/concepts/ بسازید.
5. نام canonical، aliases، status، revision، domains، layers، knowledge_types و سایر فیلدهای الزامی را پر کنید.
6. تعریف، هدف، نقش، سازوکار، اجزا، ورودی/خروجی، محدودیت‌ها و روش اعتبارسنجی را بنویسید.
7. منابع و روابط را با شناسه‌های پایدار و Predicate کنترل‌شده ثبت کنید.
8. ادعاهای بدون شاهد را با وضعیت و عدم قطعیت روشن علامت‌گذاری کنید.
9. validator و آزمون‌ها را اجرا کنید.
10. Branch و Pull Request بسازید و نتیجه CI را بررسی کنید.
11. پس از تأیید، Merge کنید؛ Runtime با راه‌اندازی مجدد محتوای جدید را از مخزن بارگذاری می‌کند.

گردش کار کامل در workflows/knowledge-intake.md و docs/KNOWLEDGE_OPERATING_WORKFLOW.md قرار دارد.

## 9. نمونه Work Item

~~~yaml
work_item:
  title: "Investigate a new engineering concept"
  question: "What is the concept and how does it differ from related concepts?"
  expected_output:
    - canonical_concept_record
    - source_register
    - typed_relationships
  scope:
    territories: []
    domains: []
    layers: []
  evidence_requirements:
    - primary_documentation
    - implementation_reference
  acceptance_criteria:
    - stable_id_assigned
    - duplicate_search_completed
    - claims_have_sources_or_uncertainty_labels
    - taxonomy_ids_validate
    - relationships_reviewed
  status: INBOX
~~~

این نمونه طرح مفهومی است و لزوماً Schema اجرایی مستقل برای Work Item در نسخه فعلی نیست.

## 10. خطاهای رایج

- استفاده از نام نمایشی به‌جای شناسه canonical؛
- فرض اینکه هشتگ الزاماً یک مفهوم علمی مستقل است؛
- واردکردن چند شرط متناقض؛
- فرض اینکه تمام فایل‌های مخزن یا دیسک ایندکس می‌شوند؛
- تلقی URL یا نتیجه جست‌وجو به‌عنوان شاهد کافی؛
- کپی متن استاندارد یا کد دارای مجوز محدود؛
- ساخت مفهوم تکراری بدون جست‌وجوی قبلی؛
- نوشتن روابط با نام مبهم به‌جای شناسه پایدار؛
- قرار دادن داده محرمانه در مخزن عمومی.

## 11. توسعه آینده ورودی‌ها

پیشنهادهای قابل بررسی:
1. Import Queue برای فایل‌ها و URLها؛
2. Preview و استخراج metadata پیش از ثبت؛
3. پشتیبانی کنترل‌شده PDF/Office؛
4. OCR و استخراج جدول؛
5. اتصال GitHub/GitLab و ثبت نسخه/Commit؛
6. تبدیل محتوا به Candidate Record با تأیید انسانی؛
7. تشخیص تکرار و تعارض؛
8. ثبت provenance برای هر بخش استخراج‌شده؛
9. پردازش دسته‌ای و گزارش خطا؛
10. اتصال اختیاری به موتورهای embedding و semantic search.

هر مورد نیازمند قرارداد ورودی، محدودیت امنیتی، مجوز، معیار کیفیت و آزمون مستقل است.
