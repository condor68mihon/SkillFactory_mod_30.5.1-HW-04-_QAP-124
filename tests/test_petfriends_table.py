import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_have_different_names(auth_pets):
   '''Поверяем что на странице со списком моих питомцев, у всех питомцев разные имена'''
   driver = auth_pets
   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   pet_data = driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')

   # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
   # и разделяем по пробелу.Выбераем имена и добавляем их в список pets_name.
   pets_name = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      pets_name.append(split_data_pet[0])

   # Перебираем имена и если имя повторяется то прибавляем к счетчику r единицу.
   # Проверяем, если r == 0 то повторяющихся имен нет.
   r = 0
   for i in range(len(pets_name)):
      if pets_name.count(pets_name[i]) > 1:
         r += 1
   assert r == 0


def test_no_duplicate_pets(auth_pets):
   '''Поверяем что на странице со списком моих питомцев нет повторяющихся питомцев'''
   driver = auth_pets
   # Устанавливаем явное ожидание
   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   # Сохраняем в переменную pet_data элементы с данными о питомцах
   pet_data = driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')

   # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
   # и разделяем по пробелу.
   list_data = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      list_data.append(split_data_pet)

   # Склеиваем имя, возраст и породу, получившиеся склееные слова добавляем в строку
   # и между ними вставляем пробел
   line = ''
   for i in list_data:
      line += ''.join(i)
      line += ' '

   # Получаем список из строки line
   list_line = line.split(' ')

   # Превращаем список в множество
   set_list_line = set(list_line)

   # Из количества элементов списка вычитаем количество элементов множества
   result = len(list_line) - len(set_list_line)

   # Если количество элементов == 0 значит карточки с одинаковыми данными отсутствуют
   assert result == 0

def test_photo_availability(auth_pets):
   '''Поверяем что на странице со списком моих питомцев хотя бы у половины питомцев есть фото'''
   driver = auth_pets
   element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   # Сохраняем в переменную ststistic элементы статистики
   statistic = driver.find_elements(By.CSS_SELECTOR,".\\.col-sm-4.left")

   # Сохраняем в переменную images элементы с атрибутом img
   images = driver.find_elements(By.CSS_SELECTOR,'.table.table-hover img')

   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   # Находим половину от количества питомцев
   half = number // 2

   # Находим количество питомцев с фотографией
   number_а_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_а_photos += 1

   # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
   assert number_а_photos >= half