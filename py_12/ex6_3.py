# import pandas as pd
# import os

# def concat_users_files(path):
#     my_files = os.listdir(path)
#     my_files.sort(key = lambda x: x)
#     my_df = pd.DataFrame()
#     for i in my_files:
#         my_df = pd.concat([my_df,pd.read_csv(path +'\\'+ i)])
#         my_df = my_df.sort_values(by = 'user_id',ignore_index=1)
        
    

#     print(my_files)
  
#     return my_df
    


# if __name__ == '__main__':
#     data = concat_users_files('.\zd_6_3')
#     print(data)
    


# import pandas as pd
# import os

# def concat_users_files(path):
#     my_files = os.listdir(path)
#     my_df = pd.DataFrame()
#     for i in my_files:
#         my_df = pd.concat([my_df,pd.read_csv(path + i)])
#         my_df = my_df.sort(columns ='user_id')
#     return my_df.reset_index(drop=True)
    


# if __name__ == '__main__':
#     data = concat_users_files('./Root/users/')
#     print(data)


import pandas as pd
import os

def concat_users_files(path):
    my_files = os.listdir(path)
    my_files.sort()
    my_df = pd.DataFrame()
    
    for i in my_files:
        add_df = pd.read_csv(path+'\\'+i)
        my_df = pd.concat([my_df,add_df],axis = 0)
        
    
    return my_df
    


if __name__ == '__main__':
    data = concat_users_files('.\\zd_6_3')
    print(data)
