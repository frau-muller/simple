# -*- coding: utf-8 -*-
"""Ведра.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ajHfnqr0WIULoKvZ2Yegacg2gEiC0qPU
"""

L_3 = 0
L_5 = 0
count = 0
while L_5!=4:
  print('Заполняем пятилитровик!')
  while L_5!=5:
    L_5 = int(input())
    if L_5!=5:
      print('введи 5!')
    else:
      print('"Отлично!Пятилитровик набран"')
  count += 1
  print('Переливаем из пятилитровика в трехлитровик до края. ')
  L_5 = L_5 - 3
  L_3 = L_3 + 3
  count += 1
  print('В пятилитровике осталось ' + str(L_5))
  while L_3!=0:      
    t = int(input('Освобождаем трехлитровик.'))
    L_3 = L_3 - t
    if t!=3:
      print('Объем трехлитровика. ')
    else:
      print('"Отлично, трехлитровик пуст"')
  count += 1
  print('ОбЪем  оставшейся жидкости пятилитровика переливаем в трехлитровик')
  L_3 = L_5
  count += 1
  print('Наполняем пятилитровик полностью')
  while L_5!=5:
    L_5 = int(input())
    if L_5!=5:
      print('неверно,введи 5!')
    else:
      print('"Здорово!Пятилитровик набран"')
  count += 1
  while L_3!=3:
    a = int(input('Доливаем в трехлитровик из пятилитровика '))
    L_3 = L_3 + a
    if L_3 > 3:
      print('Перелив!')
    else:
      print('"Условие выполнено"')
  L_5=L_5-a
  count += 1
print('Есть 4 литра, за ' + str(count) + ' манипуляций.')

