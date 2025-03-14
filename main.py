import asyncio
import random
import string
from playwright.async_api import async_playwright

async def main():
    # Получаем имя и фамилию от пользователя
    print("Введите имя:")
    first_name = input().strip()
    
    print("Введите фамилию:")
    last_name = input().strip()
    
    # Прокси данные
    proxy_http = {
        "server": "http://65.21.67.151:30413",
        "username": "u9XWcLanpKMC",
        "password": "U6N8DHaXb4"
    }
    
    proxy_socks5 = {
        "server": "socks5://65.21.67.151:31413",
        "username": "u9XWcLanpKMC",
        "password": "U6N8DHaXb4"
    }
    
    # Выберите один из прокси (http или socks5)
    active_proxy = proxy_http  # или proxy_socks5
    
    # Генерируем email на основе имени и фамилии + случайные символы
    random_suffix = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
    email_username = f"{first_name.lower()}.{last_name.lower()}.{random_suffix}"
    
    # Генерируем случайный пароль
    password = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()") for _ in range(12))
    
    # Генерируем случайный номер телефона
    phone_number = ''.join(random.choice(string.digits) for _ in range(9))
    
    # Случайная дата рождения (старше 18 лет)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    year = random.randint(1970, 2000)
    
    print(f"\nСгенерированные данные для регистрации:")
    print(f"Email: {email_username}@gmx.com")
    print(f"Имя: {first_name}")
    print(f"Фамилия: {last_name}")
    print(f"Страна: Romania")
    print(f"Пароль: {password}")
    print(f"Дата рождения: {month}/{day}/{year}")
    print(f"Телефон: {phone_number}")
    print("\nСохраните эти данные, они понадобятся для входа в аккаунт!")
    
    print("\nНачинаем процесс регистрации...")
    print("Пожалуйста, подождите, пока откроется браузер...")
    
    async with async_playwright() as p:
        # Настройки браузера для отладки
        browser = await p.chromium.launch(
            headless=False,  # Видимый браузер
            proxy=active_proxy,
            slow_mo=50  # Замедляем действия для наглядности
        )
        
        # Создаем контекст с таймаутом
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800}  # Увеличиваем размер окна
        )
        
        # Увеличиваем время ожидания для всех операций
        context.set_default_timeout(30000)  # 30 секунд
        
        # Создаем новую страницу
        page = await context.new_page()
        
        # Включаем журналирование консоли браузера для отладки
        page.on("console", lambda msg: print(f"Консоль браузера: {msg.text}"))
        
        try:
            print("Переходим на страницу регистрации...")
            # Переходим прямо на страницу регистрации GMX
            await page.goto("https://signup.gmx.com/#.1559516-header-signup1-1", wait_until="networkidle")
            
            # Ждем дополнительное время для полной загрузки страницы
            print("Ожидаем полной загрузки страницы...")
            await page.wait_for_timeout(3000)
            
            # Основной процесс регистрации
            print("\nЗаполняем форму регистрации...")
            
            # Попробуем найти поле ввода email несколькими способами
            email_field = None
            email_selectors = [
                '//*[@id="login"]',  # ID
                'input[name="login"]',  # CSS
                'input[type="text"]',  # Общий CSS
                '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[1]/onereg-alias/fieldset/onereg-progress-meter/div[3]/div/div[2]/div/pos-input[1]/input'  # Полный XPath
            ]
            
            for selector in email_selectors:
                try:
                    if selector.startswith('/'):
                        elem = await page.wait_for_selector(selector, state="visible", timeout=3000)
                    else:
                        elem = await page.wait_for_selector(selector, state="visible", timeout=3000)
                    
                    if elem:
                        email_field = elem
                        print(f"Найдено поле email, вводим: {email_username}")
                        break
                except Exception as e:
                    continue
            
            if email_field:
                # 1. Вводим имя пользователя для email
                await email_field.fill(email_username)
                await page.wait_for_timeout(500)
                
                # Находим кнопку "Check" и кликаем по ней, если она есть
                try:
                    check_button = await page.wait_for_selector('button:has-text("Check")', timeout=3000)
                    if check_button:
                        await check_button.click()
                        await page.wait_for_timeout(1000)
                        print("Проверка имени пользователя...")
                except Exception:
                    pass
                
                # 2. Пробуем найти и выбрать пол (Ms)
                try:
                    gender_selectors = [
                        'label:has-text("Ms")',
                        'input[value="FEMALE"]',
                        '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[2]/onereg-progress-meter/div[3]/onereg-personal-info/fieldset/div/div/onereg-radio-wrapper[1]/pos-input-radio/label'
                    ]
                    
                    for selector in gender_selectors:
                        try:
                            gender_elem = await page.wait_for_selector(selector, timeout=3000)
                            if gender_elem:
                                await gender_elem.click()
                                print("Выбран пол: Ms")
                                await page.wait_for_timeout(500)
                                break
                        except:
                            continue
                except Exception:
                    pass
                
                # 3. Вводим имя
                try:
                    first_name_selectors = ['#given-name', 'input[name="firstName"]']
                    for selector in first_name_selectors:
                        try:
                            first_name_field = await page.wait_for_selector(selector, timeout=3000)
                            if first_name_field:
                                await first_name_field.fill(first_name)
                                print(f"Введено имя: {first_name}")
                                await page.wait_for_timeout(500)
                                break
                        except:
                            continue
                except Exception:
                    pass
                
                # 4. Вводим фамилию
                try:
                    last_name_selectors = ['#family-name', 'input[name="lastName"]']
                    for selector in last_name_selectors:
                        try:
                            last_name_field = await page.wait_for_selector(selector, timeout=3000)
                            if last_name_field:
                                await last_name_field.fill(last_name)
                                print(f"Введена фамилия: {last_name}")
                                await page.wait_for_timeout(500)
                                break
                        except:
                            continue
                except Exception:
                    pass
                
                # 5. Пробуем выбрать страну (Румыния)
                try:
                    country_selectors = ['#country', 'select[name="country"]']
                    for selector in country_selectors:
                        try:
                            country_dropdown = await page.wait_for_selector(selector, timeout=3000)
                            if country_dropdown:
                                await country_dropdown.click()
                                await page.wait_for_timeout(500)
                                
                                # Пробуем выбрать по тексту
                                await page.select_option(selector, label="Romania")
                                print("Выбрана страна: Romania")
                                await page.wait_for_timeout(500)
                                break
                        except:
                            continue
                except Exception:
                    pass
                
                # 6. Вводим дату рождения
                try:
                    date_fields = [
                        ('#bday-month', str(month)),
                        ('#bday-day', str(day)),
                        ('#bday-year', str(year))
                    ]
                    
                    for selector, value in date_fields:
                        try:
                            field = await page.wait_for_selector(selector, timeout=3000)
                            if field:
                                await field.fill(value)
                                await page.wait_for_timeout(300)
                        except:
                            continue
                    print(f"Установлена дата рождения: {month}/{day}/{year}")
                except Exception:
                    pass
                
                # 7. Вводим пароль
                try:
                    pass_selectors = ['#password', 'input[name="password"]']
                    for selector in pass_selectors:
                        try:
                            password_field = await page.wait_for_selector(selector, timeout=3000)
                            if password_field:
                                await password_field.fill(password)
                                await page.wait_for_timeout(500)
                                break
                        except:
                            continue
                    print("Пароль установлен")
                except Exception:
                    pass
                
                # 8. Повторяем пароль
                try:
                    confirm_selectors = ['#confirm-password', 'input[name="passwordConfirmation"]']
                    for selector in confirm_selectors:
                        try:
                            confirm_password_field = await page.wait_for_selector(selector, timeout=3000)
                            if confirm_password_field:
                                await confirm_password_field.fill(password)
                                await page.wait_for_timeout(500)
                                break
                        except:
                            continue
                    print("Пароль подтвержден")
                except Exception:
                    pass
                
                # 9. Вводим номер телефона
                try:
                    phone_selectors = ['#mobilePhone', 'input[name="mobilePhone"]']
                    for selector in phone_selectors:
                        try:
                            phone_field = await page.wait_for_selector(selector, timeout=3000)
                            if phone_field:
                                await phone_field.fill(phone_number)
                                await page.wait_for_timeout(500)
                                break
                        except:
                            continue
                    print(f"Установлен телефон: {phone_number}")
                except Exception:
                    pass
                
                # Сообщение пользователю о необходимости решения капчи
                print("\n" + "=" * 50)
                print("ВНИМАНИЕ: ТРЕБУЕТСЯ РЕШЕНИЕ CAPTCHA!")
                print("=" * 50)
                print("Все поля формы заполнены автоматически.")
                print("Теперь вам нужно только решить капчу и нажать кнопку регистрации.")
                print("=" * 50)
                
                # Инструкции по reCAPTCHA
                print("\nДля завершения регистрации:")
                print("1. Установите галочку 'I'm not a robot' в блоке капчи")
                print("2. Если потребуется, решите визуальную капчу")
                print("3. Нажмите кнопку 'I agree. Create an email account now.'")
                
                # Делаем заключительный скриншот заполненной формы
                await page.screenshot(path="form_ready.png")
                print("Скриншот заполненной формы сохранен как form_ready.png")
            else:
                print("Не удалось найти основные элементы формы. Возможно, страница не загрузилась корректно.")
        
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            # Делаем скриншот при ошибке
            await page.screenshot(path="error_state.png")
            print("Скриншот ошибки сохранен как error_state.png")
        
        print("\nБраузер останется открытым, пока вы не нажмете Enter в этом терминале.")
        
        # Ждем, пока пользователь не решит закрыть браузер
        await asyncio.get_event_loop().run_in_executor(None, input)
        
        print("Закрываем браузер...")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
