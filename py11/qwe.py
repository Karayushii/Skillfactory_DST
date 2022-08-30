
import pandas as pd

def get_experience(arg):
    """
    Напишите функцию get_experience(arg), аргументом которой является строка столбца с опытом работы. 
    Функция должна возвращать опыт работы в месяцах. Не забудьте привести результат к целому числу.
    """
    aarg = arg.split()[2:]
    if len(aarg) == 4 :
        return int(aarg[0])*12+int(aarg[2])
    elif aarg[1]=='лет' or aarg[1]=='года':
        return int(aarg[0])*12
    else:
        return int(aarg[0]) 
if __name__ == '__main__':
    experience_col = pd.Series([
        'Опыт работы 8 лет 3 месяца',
        'Опыт работы 3 года 5 месяцев',
        'Опыт работы 1 год 9 месяцев',
        'Опыт работы 3 месяца',
        'Опыт работы 6 лет'
        ])
    experience_month = experience_col.apply(get_experience)
    print(experience_month)