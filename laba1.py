# #1 Напишите скрипт,который преобразует введенное с клавиатуры вещественное число в денежный формат.
# Например, число 12,5 должно быть преобразовано к виду «12 руб. 50 коп.».
# В случае ввода отрицательного числа выдайте сообщение «Некорректный формат!» путем обработки исключения в коде.

# # def number_convert(number):
# #     if number <= 0:
# #         print("Число меньше нуля!")
# #     else:
# #         print(int(number), 'руб.', round((number - int(number)) * 100), 'коп.')
# #
# #
# # number = float(input('Введите стоимость'))
# # number_convert(number)



#2  Написать скрипт, который выводит на экран «True»,
# если элементы программно задаваемого списка представляют собой возрастающую последовательность,
# иначе – «False».
# def bla_bla(arr):
#     for i in range(0,len(arr)-1):
#         if arr[i] >= arr[i+1]:
#             return False
#     return True
#
# array_1 = [1, 2, 3, 4, 5, 6, 7, 8]
# array_2 = [1, 2, 3, 4, 5, 3, 2, 1]
# print(bla_bla(array_1))
# print(bla_bla(array_2))



#3 Напишите скрипт, который позволяет ввести с клавиатуры номер дебетовой карты (16 цифр)
# и выводит номер в скрытом виде: первые и последние 4 цифры отображены нормально,
# а между ними – символы «*» (например, 5123 **** **** 1212).
# x = input()
# cnt = True
# while cnt:
#     if len(x) == 16:
#         print(x[:4], " **** **** ", x[-4:])
#          cnt = False
#




# 4  Напишите скрипт, который разделяет введенный с клавиатуры текст на слова и выводит сначала те слова,
# длина которых превосходит 7 символов, затем слова размером от 4 до 7 символов, затем – все остальные.
# x = input().split()
# array_1 = [i for i in x if len(i) > 7]
# array_2 = [i for i in x if 4 < len(i) <= 7]
# array_3 = [i for i in x if len(i) < 4]
# print(array_1, " Все символы больше 7")
# print(array_2, "Символы больше 4 и меньше 7")
# print(array_3, "Все остальные символы меньше 4")


# 5Напишите скрипт, который позволяет ввести с клавиатуры текст предложения и сформировать новую строку на основе
# исходной, в которой все слова, начинающиеся с большой буквы, приведены к верхнему регистру.
# Слова могут разделяться запятыми или пробелами. Например, если пользователь введет
# строку «город Донецк, река Кальмиус», результирующая строка должна выглядеть так: «город ДОНЕЦК, река КАЛЬМИУС».
# str = "город Донецк Река Кальмиус хорошая погода".split()
# [print(x.upper()) for x in list(str) if x[0].isupper()]
# [print(x) for x in list(str) if not x[0].isupper()]





# 6 Напишите программу, позволяющую ввести с клавиатуры текст предложения и вывести на консоль все символы,
# которые входят в этот текст ровно по одному разу.
# s = input("Введите предложение ")
# print(set(s))
# x = set(s)
# for i in range(len(s)):
#     kol = s.count(s[i])
#     if kol == 1:
#         print(s[i])





# 7  Напишите скрипт, который обрабатывает список строк-адресов следующим образом: сначала определяет,
# начинается ли каждая строка в списке с префикса «www». Если условие выполняется, то скрипт должен вставить
# в начало этой строки префикс «http://», а затем проверить, что строка заканчивается на «.com».
# Если у строки другое окончание, то скрипт должен вставить в конец подстроку «.com».
# В итоге скрипт должен вывести на консоль новый список с измененными адресами. Используйте генераторы списков.
# def replace(list_):
#
#     def change(address):
#         if address.startswith('www.'):
#             address = 'http://' + address
#         if not address.endswith('.com'):
#             address += '.com'
#         return address
#
#     return list(map(lambda x: change(x), list_))
#
# print(replace([]))




# 8  Напишите скрипт, генерирующий случайным образом число n в диапазоне от 1 до 10000.
# Скрипт должен создать массив из n целых чисел, также сгенерированных случайным образом,
# и дополнить массив нулями до размера, равного ближайшей сверху степени двойки.
# Например, если в массиве было n=100 элементов, то массив нужно дополнить 28 нулями,
# чтобы в итоге был массив из 28=128 элементов (ближайшая степень двойки к 100 – это число 128, к 35 – это 64 и т.д.).
# import random
# from math import ceil, log
#
# random_number = random.randint(1, 10000)
#
# ganarated_array = [random.randint(1, 10) for i in range(random_number)]
# print("Начальный массив: ", len(ganarated_array))
#
# [ganarated_array.append(0) for i in range(pow(2, ceil(log(random_number, 2))) - len(ganarated_array))]
# print("Исправленный массив: ", len(ganarated_array))
# print(ganarated_array)





# 9 Напишите программу, имитирующую работу банкомата. Выберите структуру данных для хранения купюр разного достоинства
# в заданном количестве. При вводе пользователем запрашиваемой суммы денег, скрипт должен вывести на консоль
# количество купюр подходящего достоинства. Если имеющихся денег не хватает, то необходимо напечатать
# сообщение «Операция не может быть выполнена!».
# Например, при сумме 5370 рублей на консоль должно быть выведено «5*1000 + 3*100 + 1*50 + 2*10».
# import random
# import sys
#
#
# class OutOfMoney(Exception):
#     pass
#
#
# def bankomat(banks, money):
#     _money = money
#     _banks = banks.copy()
#     pos_banks = [1000, 100, 50, 10]
#     kol = []
#     for i in pos_banks:
#         kol = money // i
#         if kol >= 1:
#             for k in range(kol, 0, -1):
#                 if banks[i] - k >= 0 and money - k * i >= 0:
#                     money -= k * i
#                     banks[i] -= k
#                     print(k, '*', i)
#     if money != 0:
#         print('-' * 20)
#         print('Банкомат временно не работает')
#         raise OutOfMoney
#     print("Купюры", _banks)
#     print("Нужно снять", _money)
#     print("Осталось купюр", banks)
#     print("-" * 20)
#     return banks
#
#
# # словарь, ассоциативный массив - друг другу соответствую
# bnk = {j: random.randint(1, 10) for j in [1000, 100, 50, 10]}
# print("Купюры в банкомате", bnk)
# for i in sys.stdin:
#     # ввод суммы
#     try:
#         sum = int(input("Введите нужную сумму для выдачи наличными "))
#         if sum < 10 or sum > 10000:
#             raise ValueError
#     except ValueError:
#         print("Введите сумму больше 0 и меньше 10000")
#         print("-" * 20)
#     # выдача денег
#     try:
#         bnk = bankomat(bnk, sum)
#     except OutOfMoney:
#         break








# 10  Напишите скрипт, позволяющий определить надежность вводимого пользователем пароля.
# Это задание является творческим: алгоритм определения надежности разработайте самостоятельно
import sys

# class OutData(Exception):
#     pass
#
#
# def prowerka(data):
#     count_digit = 0
#     count_lower = 0
#     count_upper = 0
#
#     for i in data:
#         if i.isdigit():
#             count_digit += 1  # Считаем сколько цифр в пароле
#         if i.islower():
#             count_lower += 1  # Считаем сколько символов нижнего регистра
#         if i.isupper():
#             count_upper += 1  # Считаем сколько в верхнем регистре
#     # Если длина пароля >6, есть цифра и есть одна заглавная и одна маленькая буква, то True
#     if len(data) > 8 and count_digit > 0 and count_lower > 0 and count_upper > 0:
#         return "Пароль надежный"
#     else:
#         raise OutData
#
#
# for i in sys.stdin:
#     try:
#         digit = input("Введите пароль ")
#         if len(digit) < 8:
#             raise ValueError
#     except ValueError:
#         print("Введите пароль, состоящий минимум из 8 символов")
#     try:
#         # digit="1q2wg%3eSD"
#         print(prowerka(digit))
#     except OutData:
#         print("Парoль не надежный")
#         break





# 11  Напишите генератор frange как аналог range() с дробным шагом.
# def frange(start, end, step):
#     while start < end - step:
#         yield round(start, 5)
#         start += step
#
# for i in frange(1, 5, 0.1):
#     print(i, end=', ')


# 12  Напишите генератор get_frames(), который производит «оконную декомпозицию» сигнала:
# на основе входного списка генерирует
# набор списков – перекрывающихся отдельных фрагментов сигнала размера size со степенью перекрытия overlap.
# def get_frames(signal, size, overlap):
#     print('Step: ')
#     x = signal
#     step = size * overlap
#     print(step)
#     i = 0
#     while i < len(signal):
#         print(signal[i:i + size])  # ot 0 do stap, ot stap + size
#         i = i + int(step)
#
#
# size = 10  # razmer okna
# signal = [i for i in range(0, 1024)]  # razer signala
# overlap = 0.3  # stepen perekritia
# get_frames(signal, size, overlap)


# 13  Напишите собственную версию генератора enumerate под названием extra_enumerate
# def extra_enumerate(someArray, start):
#   enum ne enum
#     n = start
#     cum = 0
#     for elem in someArray:
#         yield n, elem  #vozvrashaet generator
#         n += 1
#         cum = cum + elem
#         print(n,'     ',elem,'     ',cum,'     ',cum*0.1)
# x  = [1,3,4,2]
# print ('id     num     sum      10%')
# for i in extra_enumerate(x,0):
#     print()



# 14 Напишите декоратор non_empty, который дополнительно проверяет списковый результат любой функции:
# если в нем содержатся пустые строки или значение None, то они удаляются.
#
# array =  ['chapter1', '', 'contents', '', 'line1']
# print([x for x in array if True == bool(x.strip())])




# 15  Напишите параметризированный декоратор pre_process, который осуществляет
# предварительную обработку (цифровую фильтрацию) списка по алгоритму:
# s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в коде (по умолчанию равен 0.97).
# def pre_process(a=0.97):
#     def wrapTheFunction(a_func):
#         print("До исполнения a_func()")
#         print(s)
#         i = 0
#         for i in range(len(s)):
#             s[i] = s[i] - a * s[i - 1]
#
#         print("После исполнения a_func()")
#         print(s)
#
#     return wrapTheFunction
#
#
# s = [3, 5, 2, 5, 8, 2, 5, 6, 7]
#
#
# @pre_process(a=0.93)
# def plot_signal(s):
#     for i in s:
#         print(i)





# 16 Напишите скрипт, который на основе списка из 16 названий футбольных команд случайным образом формирует 4 группы
# по 4 команды, а также выводит на консоль календарь всех игр (игры должны проходить по средам, раз в 2 недели,
# начиная с 14 сентября текущего года).
# Даты игр необходимо выводить в формате «14/09/2016, 22:45». Используйте модули random и itertools.
# import random
# import datetime
# from datetime import timedelta
#
# TeamList = ['Group 1','Group 2','Group 3','Group 4','Group 5','Group 6','Group 7',
#     'Group 8','Group 9','Group 10','Group 11','Group 12','Group 13','Group 14',
#     'Group 15','Group 16']
# random.shuffle(TeamList)
# print (TeamList)
# TeamList = [TeamList[d:d+4] for d in range(0, len(TeamList), 4)]
# print ('\nГруппы:')
# print ('Group A: ',TeamList[0])
# print ('Group B: ',TeamList[1])
# print ('Group C: ',TeamList[2])
# print ('Group D: ',TeamList[3])
# print ('\nДаты:')
#
# datestart=datetime.date(2016,9,14)
# print(datestart.strftime('%d/%m/%Y, %I:%M'))
# delta = timedelta(days=14)
# print(delta)
# while(datestart<datetime.date(2017,9,14)):
#     datestart=datestart+delta
#     print(datestart.strftime('%d/%m/%Y, %I:%M'))
