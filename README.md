# SkillFactory_mod_30.5.1-HW-04-_QAP-124
Тесты (проверка карточек питомцев) c неявными ожиданиями всех элементов (фото, имя питомца, его возраст)

Задание 30.5.1.
В написанном тесте (проверка карточек питомцев) добавьте неявные ожидания всех элементов (фото, имя питомца, его возраст).
В написанном тесте (проверка таблицы питомцев) добавьте явные ожидания элементов страницы.

Чеклист для самопроверки:

 -В тестах используется настройка implicitly-wait веб-драйвера.
 
 -В тестах используются элементы класса WebDriverWait.

Требуется установить дополнительные модули:

-import time,
-import pytest,
-from selenium.webdriver.support import expected_conditions as EC,
-from selenium.webdriver.common.by import By,
-from selenium import webdriver,
-from selenium.webdriver.chrome.service import Service as ChromeService,
-from webdriver_manager.chrome import ChromeDriverManager,
-from selenium.webdriver.support.ui import WebDriverWait,
-from settings import valid_password, valid_email,


В файле settings.py находятся данные о email и pass.

Авторизация и переход на страницу "Мои питомцы" происходит при помощи setup фикстуры в conftest.py, если PyCharm при запуске тестов
не видит фикстуры, необходимо переместить файл conftest.py директорию с файлами тестов. 
