# Создаю Множество 
class multiSet():
    """
    Реализую хешфункцию 
    создал класс multiSet
            

    Returns:
        методы : 
            add - добавление
            delite - удаление
            show - показывает всю хеш таблицу
            find - нахождение (возвращает True - если такое значение есть в наборе)
    """
    set_size = 10
    myset = [[] for i in range(set_size)]
    def __init__(self) -> None:
        pass
    
    def add(self, num):
        if not self.find(num):
            self.myset[num%10].append(num)
        return False
    
    def find(self, num):
        for i in self.myset[num%10]:
            if i == num:
                return True

        return False
    
    def delite(self, num):
        xlist = self.myset[num%10]
        for i in range(len(xlist)):
            if xlist[i] == num:
                xlist[i], xlist[len(xlist)-1] == xlist[len(xlist)-1], xlist[i]
                xlist.pop()
                return True
            return False
        
    def show(self):
        return self.myset
        
# Создание 
my_set = multiSet()

# Добавление в хеш-таблицу 10
my_set.add(10)

#  Поиск несуществубщего значение (возвращает False)
print(my_set.find(7))

# Добавление, поиск и удаление 7
my_set.add(7)
print(my_set.find(7))
print(my_set.delite(7))

# Показ хеш-таблицы
print(my_set.show())
# [[10], [], [], [], [], [], [], [], [], []]
        



