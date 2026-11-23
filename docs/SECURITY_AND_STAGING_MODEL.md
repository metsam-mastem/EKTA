# مدل امنیت و مرحله‌بندی Workspace

## Trust boundaries

| ناحیه | سطح اعتماد | رفتار |
|---|---|---|
| Git canonical tree | منبع حقیقت | فقط از مسیرهای حاکمیتی و بازبینی‌شده تغییر می‌کند |
| Import staging | ورودی تأییدنشده | فایل محدود، parse امن و ذخیره خارج از canonical |
| Draft staging | محتوای پیشنهادی | Markdown و فراداده در پوشه محلی مستقل |
| Backup archive | snapshot قابل انتقال | مسیرهای منتخب؛ بدون .git و محیط اجرایی |
| Restore staging | بسته بازیابی تأییدنشده | بررسی ZIP و نگهداری خام؛ بدون extract/overwrite |
| Documentation reader | محتوای متنی | فقط فایل Markdown زیر docs؛ بدون HTML rendering |

## Input constraints

- Import extensions: .md, .markdown, .yaml, .yml, .json.
- Import maximum: 1 MiB per file.
- Restore maximum: 20 MiB and 5,000 archive members.
- Restore blocks absolute paths, parent traversal, symlinks, and archives without EKTA root folder.
- Draft IDs accept uppercase letters, digits and hyphens, length 3–64.
- Drafts and staging files are local workspace data and must not be committed.

## Explicit non-goals

No direct canonical write, no Git commit/push, no automatic extraction, no arbitrary filesystem browser, no cloud upload, no authentication, and no multi-user collaboration.

## Release hardening still required

Before network exposure or multi-user use: authentication/authorization, CSRF strategy, rate limiting, request body limits at server/proxy, audit log, quotas/retention, malware scanning if binary import is ever added, and threat-model review.
