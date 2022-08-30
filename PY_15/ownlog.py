class OwnLogger():
    def __init__(self) -> None:
        self.alarms = dict()
    def log(self,message,level):
        if level not in ['info','warning','error']:
            raise ValueError('Неверное значение')
        self.alarms[level]=message
        return self.alarms
    def show_last(self,level='all'):
        if level=='all':
            return self.alarms.popitem()[1]
        try:
            return self.alarms[level]
        except KeyError as e:
            return None
logger = OwnLogger()
logger.log("System started", "info")
print(logger.show_last("error"))
# => None
# Некоторые интерпретаторы Python могут не выводить None, тогда в этой проверке у вас будет пустая строка
logger.log("Connection instable", "warning")
logger.log("Connection lost", "error")

print(logger.show_last())
# => Connection lost
print(logger.show_last("info"))
# => System started