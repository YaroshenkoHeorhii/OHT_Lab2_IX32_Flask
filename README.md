# Lab2-IX32 — Flask Hello World

Навчальний Flask-вебзастосунок для лабораторної роботи №2 з дисципліни
**«Основи хмарних технологій»** (Azure App Service / PaaS).

Автор: Ярошенко Г. Р., група ІХ-32.

## Файли

- `app.py` — Python/Flask застосунок з маршрутами `/` та `/health`.
- `requirements.txt` — залежності Python для Azure.
- `templates/index.html` — сторінка `Hello, World!`.

## Локальний запуск (за бажанням)

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Потім відкрийте `http://127.0.0.1:5000/`.

## Azure App Service

Створити **Linux Web App** з Python 3.11 і планом Free F1, тоді:

1. Завантажити файли **в корінь GitHub-репозиторію** (не вкладати папку `Lab2-IX32-Flask`).
2. У створеному Web App перейти до **Deployment Center**.
3. Вибрати **GitHub** і дозволити Azure доступ до власного репозиторію.
4. Вибрати гілку `main`, зберегти налаштування, перевірити GitHub Actions / Deployment logs.
5. Відкрити вебадресу App Service.

Для стандартної структури `app.py` + змінна `app` Azure автоматично
виявляє Flask і запускає Gunicorn. Самостійний workflow не додавайте —
Deployment Center створить його після підключення GitHub.

Після завершення лабораторної видаліть ресурсну групу, щоб не залишати
платні ресурси. Не додавайте в GitHub приватні SSH-ключі, токени чи паролі.
