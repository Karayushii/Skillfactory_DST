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


def find_median(input_string):
    # Преобразую строку в список
    input_string = input_string.split(', ')
    if input_string:
        try:
            for i in range(len(input_string)):
                input_string[i]=float(input_string[i])
        except ValueError:
            return 'Некорректный ввод'
        
        for n in range(len(input_string)):
            for m in range(len(input_string)):
                if input_string[n]>input_string[m]:
                    input_string[n],input_string[m] = input_string[m],input_string[n]
        # return input_string

        if len(input_string)%2==0:
            l = int(len(input_string)/2)
            l = (input_string[l]+input_string[l-1])/2
            return 'Median: {}'.format(l)
        else:
            l = int((len(input_string)-1)/2)
            return 'Median: {}'.format(input_string[l])
            
    else:
        return 'Некорректный ввод'
# i = [1, 5, 2, 3, 6]
# n = int((len(i)-1)/2)
# print(i[n])
# j = [1, 5, 2, 3, 6, 7,8,9]
# print(j[len(j)])

# input_string = input('Введите последовательность чисел: ')
print(find_median(input_string='1, 5, 2, 3, 6'))
# Ввод:
# 1, 5, 2, 3, 6

# Вывод:
# Median: 3.0
# ```
# ```
print(find_median(input_string='100, 5, 2, 4, 3, 6'))
# Ввод:
# 100, 5, 2, 4, 3, 6

# Вывод:
# Median: 4.5
# ```
# ```
# Ввод:
print(find_median(input_string=''))

# Вывод:
# Некорректный ввод
# ```
# ```
# Ввод:
print(find_median(input_string='десять, 10, пять, 7, семь'))
# десять, 10, пять, 7, семь

# Вывод:
# Некорректный ввод
# ```
