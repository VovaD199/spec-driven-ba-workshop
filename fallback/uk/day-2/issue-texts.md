# Тексти для issue (запасний приклад, день 2)

> ЗАПАСНИЙ ПРИКЛАД. Якщо GitHub MCP або чат недоступні, ці тексти можна **прочитати, виправити й вставити вручну** на github.com. Опора: `contact-form-feature.md` у цій же папці. Додайте власні правки (див. `fallback/uk/README.md`). **Оригінальний текст issue не перезаписуйте**: усе інше додавайте окремими коментарями..

## 1. Створення issue

**Заголовок:** `Contact form — update validation and notifications`

**Тіло:**

```text
We want to tighten up the contact form. Phone number should be mandatory.
We should also let visitors attach a document (CV or portfolio) when they write to us.
Notifications need to reflect the new field.
```

## 2. Коментар «Business context»

```text
Business context (simulation, to be confirmed with the real stakeholder):
- Goal: call back about performance rights; emails get lost.
- Success metric: share of requests answered within 2 working days, now ~50%, target 90%.
- NFR-01 privacy: phone and CV are personal data; keep up to 6 months; access for two employees.
- NFR-02 files: PDF only, up to 5 MB.
- NFR-03 languages: error messages in the visitor's interface language.
```

## 3. Коментар «Rules table:»

Вставте таблицю з розділу 5 `contact-form-feature.md` (RULE-01…RULE-11, три стани). Скорочена версія:

| ID | Правило | Файл | Джерело істини | Шар | Є зараз → Має бути |
|---|---|---|---|---|---|
| RULE-01 | Ім'я | `validation.ts`, `validateContactData.ts`; `ContactForm.tsx` | константа / число в схемі | API і UI | 2–50 → без змін |
| RULE-02 | Email | `validateContactData.ts` (регулярний вираз); `ContactForm.tsx` (`.email()`) | **два різні правила** | API і UI | різні → ? (Q-09) |
| RULE-03 | Телефон | `validateContactData.ts`; `ContactForm.tsx` | регулярний вираз / схема | API і UI | необов'язковий → обов'язковий |
| RULE-04 | Повідомлення | `validation.ts`; `ContactForm.tsx`; `i18n/messages` | константа і число в схемі й текстах | API і UI | 10–1000 → без змін |
| RULE-05 | Згода з політикою | `ContactForm.tsx` | схема zod | **лише UI** | лише UI → ? (Q-08) |
| RULE-08 | Приймання запиту | `app/api/collaboration/route.ts` | жорстко закодований текст | API | демо-«успіх» → ? |

## 4. Коментар з аналізом впливу

| Зачеплена область | Тип зміни | Ризик | Рекомендована дія | Ідея регресійного тесту | Пов'язані RULE-ID |
|---|---|---|---|---|---|
| Форма (`ContactForm.tsx`) | змінена | середній | Зробити телефон обов'язковим, додати поле файлу | Порожній телефон не відправляється | RULE-03, RULE-06 |
| Валідація API (`validateContactData.ts`) | змінена | високий | Прибрати гілку необов'язкового телефону, узгодити з формою | Запит без телефону отримує 400 | RULE-03 |
| Маршрути (`collaboration`, `contact`) | змінені | середній | Прийняти файл, обрати, який маршрут лишається | Завеликий файл відхиляється | RULE-06, RULE-08 |
| Сервіс пошти (`emailService.ts`) | нова робота | високий | Зараз не викликається: треба підключити й додати вкладення | Лист містить телефон і посилання | RULE-07 |
| Сервіс завантаження (`upload.ts`) | змінений | високий | Зараз демо-заглушка; визначити сховище | Завантажений PDF відкривається | RULE-06 |
| Тести (`ContactForm.test.tsx`, `validateContactData.test.ts`) | змінені | середній | Оновити очікування | Усі тести проходять | RULE-03 |
| Переклади (`i18n/messages`) | змінені | низький | Тексти помилок телефону, файлу (uk і en) | Показується правильна мова | RULE-03, RULE-06 |
| Конфігурація | нова | середній | Ліміти розміру й типу файлу в константах | Межі беруться з однієї константи | RULE-06 |

## 5. Коментар «Acceptance criteria:»

Використайте розділ 6 із `contact-form-feature.md` (AC-01…AC-12, Given/When/Then, RULE-ID). Це **окремий коментар**, а не заміна тіла issue.

## 6. Коментар «Open questions for the stakeholder:»

Використайте розділ 8 із `contact-form-feature.md` (Q-01…Q-10 із власниками й датами).
