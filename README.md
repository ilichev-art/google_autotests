# 🧪 Singletone Framework

Лёгкий и расширяемый Python-фреймворк для UI-автотестов на базе Selenium с реализацией шаблона проектирования **Singleton** для управления WebDriver.

## 📌 Возможности

- ✅ Singleton WebDriver: предотвращает повторную инициализацию браузера
- ✅ Поддержка Pytest с глобальной фикстурой `setup_teardown`
- ✅ Структура Page Object (POM)
- ✅ Базовый `BasePage` с удобными методами:
  - Открытие URL
  - Поиск элементов
  - Ожидание видимости/кликабельности
  - Ввод текста
  - Проверка загрузки страницы

## 🛠️ Стек технологий

- Python 3.11+
- Selenium 4
- Pytest
- WebDriver Manager
- Allure (опционально для отчётов)
- Faker (опционально для генерации данных)

## 📁 Структура проекта

```
singletone_framework/
├── tests/                 # UI-тесты
│   └── test_google_search.py
├── entities/              # Страницы (Page Object)
│   ├── base_page.py
│   └── google_page.py
├── utils/
│   └── webdriversingleton.py
├── conftest.py            # Pytest фикстура с инициализацией/завершением браузера
├── config.py              # Настройки URL и пр.
└── requirements.txt
```

## 🚀 Быстрый старт

1. Клонируй репозиторий:

```bash

git clone https://github.com/ilichev-art/singletone_framework.git
cd singletone_framework
```

2. Установи зависимости:

```bash

pip install -r requirements.txt
```

3. Запусти тест:

```bash

pytest -v
```

4. (Опционально) с отчётом Allure:

```bash

pytest --alluredir=allure-results
allure serve allure-results
```


## 📬 Обратная связь

Проект в активной разработке. Предложения и pull request'ы приветствуются!

---

**Автор:** [ilichev-art](https://github.com/ilichev-art)
