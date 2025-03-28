# 📧 GMX Авторегистратор

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Latest-green.svg?logo=playwright&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

*Автоматизация регистрации аккаунтов на GMX.com с использованием Playwright*

</div>

<p align="center">
  <img src="https://www.gmx.com/resources/ms2/cpv/images/cpv-logo-gmx.svg" alt="GMX Logo" width="200" />
</p>

## 📝 Описание

Этот скрипт автоматизирует процесс регистрации новых аккаунтов на GMX.com, предварительно заполняя все необходимые поля. Используя библиотеку Playwright для управления браузером, скрипт значительно упрощает и ускоряет процесс создания новых учетных записей.

## ✨ Функциональность

| Функция | Описание |
|---------|----------|
| 🤖 Автозаполнение | Автоматическое заполнение всех полей формы регистрации |
| 🔑 Генерация данных | Создание уникального email-адреса и надежного пароля |
| 🌐 Прокси | Использование HTTP и SOCKS5 прокси для обхода ограничений |
| 📸 Скриншоты | Создание скриншотов для отслеживания процесса регистрации |
| 👤 Персонализация | Использование пользовательских данных (имя, фамилия) |

## 🔧 Требования

- Python 3.7+
- Playwright для Python
- Стабильное интернет-соединение

## 📥 Установка

```bash
# Клонирование репозитория
git clone https://github.com/Wiranov/gmx-autoreg.git
cd gmx-autoreg

# Установка зависимостей
pip install -r requirements.txt

# Установка браузеров для Playwright
python -m playwright install
```

> 📋 **Файл requirements.txt:**
> ```
> playwright==1.30.0
> asyncio==3.4.3
> ```

## 🚀 Использование

```bash
python main.py
```

### Пошаговая инструкция:

1. Запустите скрипт командой `python main.py`
2. Введите своё имя и фамилию по запросу
3. Скрипт автоматически заполнит все поля формы
4. Решите капчу вручную
5. Подтвердите регистрацию, нажав кнопку
6. Сохраните выведенные в консоль данные аккаунта

## ⚙️ Настройка прокси

В скрипте предусмотрено два варианта прокси:

<details>
<summary>HTTP прокси</summary>

```python
proxy_http = {
    "server": "http://proxy_ip:port",
    "username": "ваш_логин",
    "password": "ваш_пароль"
}
```
</details>

<details>
<summary>SOCKS5 прокси</summary>

```python
proxy_socks5 = {
    "server": "socks5://proxy_ip:port",
    "username": "ваш_логин",
    "password": "ваш_пароль"
}
```
</details>

Для выбора нужного прокси измените значение переменной `active_proxy`.

## 📌 Важные примечания

- ⚠️ Скрипт не обходит капчу автоматически — решение капчи требует участия пользователя
- 🖱️ Браузер открывается в видимом режиме для контроля процесса
- ⏱️ Для завершения работы скрипта нажмите Enter в терминале после успешной регистрации

## 📊 Пример работы

```
Введите имя:
Иван
Введите фамилию:
Петров

Сгенерированные данные для регистрации:
Email: ivan.petrov.a7b3c@gmx.com
Имя: Иван
Фамилия: Петров
Страна: Romania
Пароль: H8jK!2pQ5#xL
Дата рождения: 5/12/1987
Телефон: 987654321

Сохраните эти данные, они понадобятся для входа в аккаунт!
```

## 📜 Лицензия

Распространяется под лицензией MIT. См. файл `LICENSE` для получения дополнительной информации.


<div align="center">
<p>⭐ Не забудьте поставить звездочку этому репозиторию, если он вам помог! ⭐</p>
</div>

