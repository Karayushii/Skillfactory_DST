# class DepartmentReport():
#     def __init__(self,company) -> None:
#         self.revenues = []
#         self.company = company
        
#     def add_revenue(self,amount):   
#         self.revenues.append(amount)
#     def average_revenue(self):
#         average=sum(self.revenues)/len(self.revenues)
#         return f'Average department revenue for {self.company}: {round(average)}'
# report = DepartmentReport("Danon")
# report.add_revenue(1_000_000)
# report.add_revenue(400_000)

# print(report.average_revenue())

# class User():
#     def __init__(self,email,password,balance) -> None:
#         self.email = email
#         self.password=password
#         self.balance=balance
#     def login(self,email,password):
#         if (email is self.email) & (password is self.password):
#             print(True) 
#         else:
#             print (False)
#     def update_balance(self,amount):
#         self.balance+=amount

# user = User("gosha@roskino.org", "qwerty", 20_000)
# user.login("gosha@roskino.org", "qwerty123")
# # => False
# user.login("gosha@roskino.org", "qwerty")
# # => True
# user.update_balance(200)
# user.update_balance(-500)
# print(user.balance)
# # => 19700

# class DataBase():
#     def __init__(self) -> None:
#         pass
# db = DataBase()

# class Dog():
#     def bark():
#         return 'Bark!'
#     def give_paw():
#         return 'Paw'
    
# with open('PY_15/input.txt','w') as inp:
#     inp.write('1234234\n234234234234234\n234464623456\n4353452q3541345')
# # with open('PY_15/output.txt','w') as out:
# #      out.write('')
# with open('PY_15/input.txt','r') as inp:
#     with open('PY_15/output.txt','w') as out:
#         for n in inp:
#             out.write(n)

# real_num = open('PY_15/real_num.txt','w')
# real_num.write('1\n-3423523\n1.34566\n544400\n-2441.4334\n-234524567547\n')
# real_num.close()
# list_num = open('PY_15/real_num.txt','r')
# n = list_num.readlines()
# list_num.close()
# print(n)
# new_n = list()
# for i in n:
#     new_n.append(float(i[:-1]))
# print(new_n)
# n_min = new_n[0]
# for i in new_n:
#     if i<n_min:
#         n_min = i
# print(n_min)
# n_max= new_n[0]
# for i in new_n:
#     if i > n_max:
#         n_max=i
# print(n_max)
# print(n_min+n_max)
# with open('PY_15/output_num.txt','w') as ntxt:
#     ntxt.write(f'{n_min  + n_max}')

# with open('PY_15\students.txt','r',-1,'UTF-8') as f:
#     print(f)
#     stud_list = list()
#     for i in f:
#         i=i.replace('\n','')
#         stud_list.append(i)
# print(stud_list)
# my_dict=dict()
# for j in stud_list:
#     my_dict[j[:-1]]=j[-1]
# print(my_dict)
# for l in my_dict:
#     if int(my_dict[l])<3:
#         print(l)
        


# from asyncore import write


# with open('PY_15\students.txt','r',-1,'UTF-8') as f:
#     list_1=list()
#     for i in f:
#         i = i.replace('\n','')
#         list_1.append(i)
# print(list_1)
# list_1.reverse()
# print(list_1)
# with open('PY_15\students.txt','w',-1,'UTF-8') as f:
#     for j in list_1:
#         f.write(f'{j}\n')
# try:
#     a = int(input())
# except ValueError as e:
#     print('не правильный тип')
# else:
#     print(f'lucky value{a}')
# finally:
#     print('prg exit')


class NonPositiveDigitException(ValueError):
        def __init__(self, *args: object) -> None:
            super().__init__(*args) 
            
class Square(NonPositiveDigitException):
    def __init__(self,side) -> None:
        if side<0:
            raise NonPositiveDigitException("Xbckj")

a = Square(-1)