# mixture_dict = {'a': 15, 'b': 10.5, 'c': '15', 'd': 50, 'e': 15, 'f': '15'}
# ## count_numbers = 4

mixture_dict = {'key1': 24, 'key2': '1.4', 'key3': 14, 'key4': 16.24, 'key6': 124.2414, 'key7': 12.2}
## count_numbers = 5
count_numbers = 0
for elem in mixture_dict:
    if mixture_dict[elem] is int or mixture_dict[elem] is float:
        count_numbers+=1
    continue
print(count_numbers)