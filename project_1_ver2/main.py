def month_count(my_value):
    month = 0
    for i in range(len(my_value)):
        if my_value[i] in ['лет']:
            yr = int(my_value[i-1])
            month += yr*12
        if my_value[i] in ['месяцев']:
            mth = int(my_value[i-1])
            month += mth
            break
    return month
            


lst = ['Опыт','работы','16','лет','10','месяцев','Август,2010']

print(month_count(lst))