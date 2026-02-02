# Автотесты для модуля авторизации Ростелеком ID

##  Описание проекта
Набор автотестов для тестирования функционала авторизации, регистрации и восстановления пароля в сервисе "Ростелеком ID".

**Что тестируется:**
- Авторизация по номеру телефона, email, логину, лицевому счету
- Авторизация по временному коду (SMS/email)
- Восстановление пароля
- Регистрация нового пользователя
- Валидация полей ввода

##  Технологический стек
| Инструмент | Назначение | Почему выбран |
|------------|------------|---------------|
| **Python 3.10+** | Язык программирования | Популярность, простота синтаксиса, богатая экосистема |
| **Pytest** | Фреймворк для тестирования | Гибкость, фикстуры, параметризация, плагины |
| **Selenium WebDriver** | Автоматизация браузера | Стандарт для UI-автотестов, поддержка всех браузеров |
| **Page Object Model** | Паттерн проектирования | Повышение читаемости, переиспользование кода |
| **WebDriver Manager** | Управление драйверами | Автоматическая загрузка драйверов, не нужно хранить в репо |
| **Pytest-HTML** | Генерация отчетов | Простота использования, встроенная в Pytest |

1. Настройка проекта
pytest>=7.0.0
playwright>=1.40.0
pytest-playwright>=0.4.0
selenium>=4.15.0
pytest-html>=4.0.0
allure-pytest>=2.13.0


import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def page(browser):
    # Создаем новый контекст для каждого теста
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        locale='ru-RU',
        timezone_id='Europe/Moscow'
    )
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def browser(playwright):
    # Запускаем браузер один раз для сессии
    browser = playwright.chromium.launch(
        headless=False,  # Для отладки установите False
        slow_mo=50  # Замедление для визуализации
    )
    yield browser
    browser.close()

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="test", help="Окружение: test/stage/prod")
    parser.addoption("--base-url", action="store", help="Базовый URL приложения")

def pytest_configure(config):
    config.addinivalue_line("markers", "high: Высокий приоритет теста")
    config.addinivalue_line("markers", "medium: Средний приоритет теста")
