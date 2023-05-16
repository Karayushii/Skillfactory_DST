# from bs4 import BeautifulSoup
# import requests
# def wiki_header(url):
#     responce = requests.get(url)
#     html_cd = responce.text
#     url = BeautifulSoup(html_cd,'html.parser')
#     zagolovok = url.find('h1').text
#     return zagolovok


# print(wiki_header('https://en.wikipedia.org/wiki/Operating_system'))
# import requests # Импортируем модуль requests
token = 'fb65b290fb65b290fb65b2905bf871a3a2ffb65fb65b2909f071112df9ccfc750e192e1' # Указываем свой сервисный токен
# url = 'https://api.vk.com/method/groups.getMembers' # Указываем адрес обращения
# count = 1000
# offset = 0 
# user_ids = [] 
# max_count = 1000
# while offset < max_count: 
#     # Будем выгружать по count=5 пользователей, 
#     # начиная с того места, где закончили на предыдущей итерации (offset) 
#     print('Выгружаю {} пользователей с offset = {}'.format(count, offset))   
#     params = {'group_id': 'vk', 'v': 5.95, 'count': count, 'offset': offset, 'access_token': token} 
#     response = requests.get(url, params = params) 
#     data = response.json() 
#     user_ids += data['response']['items'] 
#     # Увеличиваем смещение на количество строк, которое мы уже выгрузили 
#     offset += count 
#     max_count = data['response']['count']
# print(user_ids) 

# import requests # Импортируем модуль requests
# import time # Импортируем модуль time
# token = 'fb65b290fb65b290fb65b2905bf871a3a2ffb65fb65b2909f071112df9ccfc750e192e1'
# url = 'https://api.vk.com/method/groups.getMembers' # Указываем адрес страницы, к которой делаем запрос
# count = 1000 
# offset = 0  
# user_ids = []  
# while offset < 5000: 
#     params = {'group_id': 'vk', 'v': 5.95, 'count': count, 'offset': offset, 'access_token': token} 
#     response = requests.get(url, params = params) 
#     data = response.json() 
#     user_ids += data['response']['items'] 
#     offset += count 
#     print('Ожидаю 0.5 секунды...') 
#     time.sleep(0.5) 
# print('Цикл завершен, offset =',offset) 

import schedule
def task(): 
    print('Hello! I am a task!') 
    return 