# def pure_intersection(input_string1,input_string2):
#     # Преобразую строки в списки  
#     input_string1 = input_string1.split(', ')
#     input_string2 = input_string2.split(', ')
#     # Создаю пустой список для пересечений
#     my_list = list()
#     # Преобразую строки в целые значения
#     # Если строка не может быть преоразована вывожу некорректный ввод
#     try:
#         input_string1=list(map(lambda x:int(x),input_string1))
#         input_string2=list(map(lambda x:int(x),input_string2))
#     except ValueError:
#         return 'Некорректный ввод'
#     # Прохожу по спискам, сравниваю значения. Если они одинаковые, заношу в мой список.      
#     for i in input_string1:
#         for j in input_string2:
#             if i == j:
#                 my_list.append(i)
#     # Если мой список не пустой, то вывожу его
#     if my_list:
#         return my_list
#     #Если пустой, то вывожу пустой список
#     else:
#         return []
    
# input_string1 = input('Введите 1-ую последовательность идентификаторов: ')
# input_string2 = input('Введите 2-ую последовательность идентификаторов: ')
# print(pure_intersection(input_string1,input_string2))


# Ввод:
# 108, 138, 42, 52, 14
# 109, 13, 52, 32, 42, 14, 109

# Вывод:
# [42, 52, 14]

# ```

# **Пример №2:**
# ```
# Ввод:
# 108, 138, 42, 52, 14
# 189, 202, 249, 24, 15, 3

# Вывод:
# []

# ```

# **Пример №3:**
# ```
# Ввод:
# 108, 138, 42, 52, четырнадцать
# 189, 202, 249, 24, 15, 3


# Вывод:
# Некорректный ввод



# def find_min_max(input_string):
#     # Меняю запятые на точки
#     input_string = input_string.replace(',','.')
#     # Преобразую строку в список
#     input_string = input_string.split(' ')
#     # Создаю пустой список в который буду складывать только числа в формате float
#     # Если преобразование в число невозможно пропускаю
#     input_string = list()
#     for i in range(len(input_string)):
#         try:
#             input_string.append(float(input_string[i]))  
#         except ValueError:
#             continue
#     # Ищу числа формата int и преобразовываю из float
#     for j in range(len(input_string)):
#         if input_string[j]==int(input_string[j]):
#             input_string[j]=int(input_string[j])
#     # Сортирую пузырьком
#     for n in range(len(input_string)):
#         for m in range(len(input_string)):
#             if input_string[n]>input_string[m]:
#                 input_string[n],input_string[m] = input_string[m],input_string[n]
#     # Возвращаю первое и последнее значения из списка
#     return 'Minimum: {1} \nMaximim: {0}'.format(input_string[0],input_string[-1])


# input_string = input('Введите последовательность чисел: ')
# print(find_min_max(input_string))


# def find_median(input_string):
#     # Преобразую строку в список
#     input_string = input_string.split(', ')
#     # Если список пустой, тогда некорректный ввод
#     if input_string:
#         # Проверяю список на нечисловые значения и паралельно перевожу строки в числа
#         try:
#             for i in range(len(input_string)):
#                 input_string[i]=float(input_string[i])
#         except ValueError:
#             return 'Некорректный ввод'
#         # Сортирую пузырьком
#         for n in range(len(input_string)):
#             for m in range(len(input_string)):
#                 if input_string[n]>input_string[m]:
#                     input_string[n],input_string[m] = input_string[m],input_string[n]
#         # Если в списке четное количество элементов, делю длину списка 
#         # пополам, получаю индекс среднего числа смещенного вправо. Затем вычитаю из индекса 1 и получаю
#         # среднее число смещенное влево. Нахожу среднее арифметическое этих чисел.
#         if len(input_string)%2==0:
#             l = int(len(input_string)/2)
#             l = (input_string[l]+input_string[l-1])/2
#             return 'Median: {}'.format(l)
#         else:
#         # Если в списке нечетное количество элементов. Нахожу количество элементов до среднего.
#             l = int((len(input_string)-1)/2)
#             return 'Median: {}'.format(input_string[l])
            
#     else:
#         return 'Некорректный ввод'
# # i = [1, 5, 2, 3, 6]
# # n = int((len(i)-1)/2)
# # print(i[n])
# # j = [1, 5, 2, 3, 6, 7,8,9]
# # print(j[len(j)])

# # input_string = input('Введите последовательность чисел: ')
# print(find_median(input_string='1, 5, 2, 3, 6'))
# # Ввод:
# # 1, 5, 2, 3, 6

# # Вывод:
# # Median: 3.0
# # ```
# # ```
# print(find_median(input_string='100, 5, 2, 4, 3, 6'))
# # Ввод:
# # 100, 5, 2, 4, 3, 6

# # Вывод:
# # Median: 4.5
# # ```
# # ```
# # Ввод:
# print(find_median(input_string=''))

# # Вывод:
# # Некорректный ввод
# # ```
# # ```
# # Ввод:
# print(find_median(input_string='десять, 10, пять, 7, семь'))
# # десять, 10, пять, 7, семь

# # Вывод:
# # Некорректный ввод
# # ```
# def transform_string_to_integer(input_string):
#     my_list = list()
#     my_sum = 0
#     input_string = input_string.split(' ')
#     # Ищу число в словаре по первым буквам. 
#     # Когда слово находится,добавляю в список и прерываю цикл(начинаю искать следующее значение/)
#     for i in range(len(input_string)):
#         for j in number_word_dict:
#             if input_string[i].startswith(j):
#                 my_list.append(number_word_dict[j])
#                 break
#                 # Если тысяча стоит в начале списка, тогда просто суммирую.
#     if my_list[0]==1000:
#             for n in range(len(my_list)):
#                 my_sum+=my_list[n]
                
#     else:   
#          for m in range(len(my_list)):
#                 # Если тысяча стоит не в начале списка, тогда сумму полученную до 1000 умножаю на 1000.
#                 if my_list[m]==1000:
#                      my_sum*=1000
#                      continue
#                 my_sum+=my_list[m]
        
#     return my_sum

# number_word_dict = {
#     "ты": 1000, "м": 1000000,
#     "сто": 100, "двес": 200, "трис": 300, "четырес": 400, "пятьс": 500, "шестьс": 600, "семьс": 700, "восемьс": 800, "девятьс": 900,
#     "одинн": 11, "двен": 12, "трин": 13, "четырн": 14, "пятн": 15, "шестн": 16, "семн": 17, "восемн": 18, "девятн": 19,
#     "двад": 20, "трид": 30, "сор": 40, "пятьд": 50, "шестьд": 60, "семьд": 70, "восемьд": 80, "девяно": 90,
#     "деc": 10, "н": 0, "о": 1, "дв": 2, "т": 3, "ч": 4, "п": 5, "ш": 6, "с": 7, "в": 8, "д": 9, }

# print(transform_string_to_integer('один'))
# print(transform_string_to_integer('двадцать'))
# print(transform_string_to_integer('двести сорок шесть'))
# print(transform_string_to_integer('семьсот восемьдесят три тысячи девятьсот девятнадцать'))
# print(transform_string_to_integer('девятьсот девяносто девять тысяч пятьсот шестьдесят три'))
# # 1. Минимальное число — ноль (0) включительно. Максимальное число — один миллион (1000000) включительно.

# 2. Гарантируется, что на вход подаются строки с описанием числа, проверять это не нужно.

# **Пример №1:**
# ```
# Ввод:
# один

# Вывод:
# 1
# ```

# **Пример №2:**
# ```
# Ввод:
# двадцать

# Вывод:
# 20
# ```

# **Пример №3:**
# ```
# Ввод:
# двести сорок шесть

# Вывод:
# 246
# ```

# **Пример №4:**

# ```
# Ввод:
# семьсот восемьдесят три тысячи девятьсот девятнадцать

# Вывод:
# 783919
import pandas as pd


def delete_columns(df, col=[]):
    
    return df.drop(col,axis=1,inplace=True)


customer_df = pd.DataFrame({
            'number': [0, 1, 2, 3, 4],
            'cust_id': [128, 1201, 9832, 4392, 7472],
            'cust_age': [13, 21, 19, 21, 60],
            'cust_sale': [0, 0, 0.2, 0.15, 0.3],
            'cust_year_birth': [2008, 2000, 2002, 2000, 1961],
            'cust_order': [1400, 14142, 900, 1240, 8430]
        })
# print(delete_columns(customer_df,[1,2]))
