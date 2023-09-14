import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def test_show_pet_friends(auth_pets):
   '''Проверка карточек питомцев'''
   driver = auth_pets
   # Устанавливаем неявное ожидание
   driver.implicitly_wait(10)

   # Проверяем, что мы оказались на главной странице пользователя
   assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

def test_there_is_a_name_age_and_gender(auth_pets):
   '''Поверяем что на странице со списком моих питомцев, у всех питомцев есть имя, возраст и порода'''
   driver = auth_pets
   element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   pet_data = driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')

   # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
   # и разделяем по пробелу. Находим количество элементов в получившемся списке и сравниваем их
   # с ожидаемым результатом
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      result = len(split_data_pet)
      assert result == 3

def test_all_pets_are_present(auth_pets):
   '''Проверяем что на странице со списком моих питомцев присутствуют все питомцы'''
   driver = auth_pets
   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   # Сохраняем в переменную ststistic элементы статистики
   statistic = driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   # Сохраняем в переменную pets элементы карточек питомцев
   pets = driver.find_element(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   # Получаем количество карточек питомцев
   number_of_pets = len(pets)

   # Проверяем что количество питомцев из статистики совпадает с количеством карточек питомцев
   assert number == number_of_pets