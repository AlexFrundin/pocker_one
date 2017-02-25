class Singletone:
    def __new__(cls):
        #проверка на экземпляры
        if not hasattr(cls, 'isinstance'):
            cls.isinstance=super().__new__(cls)
        return cls.isinstance
#статическая инициализация
class State:
    db ='connection'
