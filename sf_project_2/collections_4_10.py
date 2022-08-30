from collections import defaultdict, deque

my_dict = defaultdict(deque)
def task_manager(tasks):
    for i in range(len(tasks)):
        if tasks[i][2]:
            my_dict[tasks[i][1]].appendleft(tasks[i][0])
        else:
            my_dict[tasks[i][1]].append(tasks[i][0])
    return my_dict
 

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]
 
print(task_manager(tasks))
