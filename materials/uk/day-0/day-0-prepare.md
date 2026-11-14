# День 0. Підготовка до курсу (≈60-90 хв, до Дня 1)

> Статус: ЧЕРНЕТКА. Команди встановлення (`winget`, `xcode-select`, `brew`, `nvm`, `apt`) ще не перевірені на чистих машинах (див. `mentor/uk/day-0-checklist.md`). Мова: [English](../../en/day-0/day-0-prepare.md).

**Мета:** прийти на День 1 з робочим середовищем. Результат: скріншот перевірки ментору.

## 0. Що потрібно мати
- Комп'ютер Windows 10/11, macOS або Linux, ≈5 ГБ вільного місця, інтернет.
- Права встановлювати програми (якщо їх немає, напишіть ментору **заздалегідь**).
- Акаунти: GitHub (обов'язково), Cursor (безкоштовний план), Figma (обов'язково; якщо акаунта немає, ментор надасть посилання на макет і ви працюватимете з ним, див. День 3).
- Англійська на рівні читання інтерфейсів Cursor і Figma.

## 1. Встановіть інструменти (≈40 хв)
| Інструмент | Windows (PowerShell) | macOS (Термінал) |
|---|---|---|
| Git | `winget install --id Git.Git -e` | `xcode-select --install` |
| Node.js 22+ | `winget install OpenJS.NodeJS.LTS` | інсталятор з https://nodejs.org |
| Cursor | https://cursor.com | https://cursor.com |

Linux: див. [installation-guide](../setup/installation-guide.md). Після встановлення **закрийте й відкрийте термінал заново**.

Перевірка:
```bash
git --version
node -v
```
Очікується: Git 2.x, Node `v22` або новіше.

Налаштуйте Git (один раз; ім'я латиницею, як у вашому GitHub):
```bash
git config --global user.name "Ivan Petrenko"
git config --global user.email "you@example.com"
```

## 2. Автентифікація GitHub (≈15 хв)
Пароль для `git push` більше не приймається. Найпростіший шлях для новачка:
1. Встановіть **GitHub CLI**: Windows `winget install --id GitHub.cli -e`, macOS `brew install gh` (або https://cli.github.com).
2. Виконайте `gh auth login`, оберіть **GitHub.com → HTTPS → Login with a web browser** і підтвердіть код у браузері.
3. Перевірка: `gh auth status` показує «Logged in».

Запасний шлях: Git Credential Manager (входить у Git for Windows) відкриє вікно входу під час першого `git push`. Документація: https://docs.github.com/en/get-started/git-basics/set-up-git

## 3. Перевірка готовності
- [ ] `git --version` і `node -v` показують версії
- [ ] `gh auth status` показує вхід (або Credential Manager налаштований)
- [ ] Cursor запускається, ви ввійшли
- [ ] Є акаунт Figma або ви знаєте, що працюватимете з посиланням ментора
- [ ] Скріншот перших двох пунктів надіслано ментору

## 4. Якщо щось не вийшло
Не витрачайте більше 20 хв на одну проблему: напишіть ментору з текстом помилки та скріншотом. Типові проблеми Windows/macOS: [installation-guide](../setup/installation-guide.md). Запасні шляхи (ZIP без Git, Codespaces) там само.

Далі: [Глосарій](glossary.md).
