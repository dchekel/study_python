class Methods:
    def imeth(self, x):  # Нормальный метод экземпляра: передается self
        print([self, x])

    def smeth(x):  # Статический метод: экземпляр не передается
        print([х])

    def cmeth(cls, х):  # Метод класса: получает класс, а не экземпляр
        print([cls, х])

    smeth = staticmethod(smeth)  # Делает smeth статическим методов (или @ впереди)
    cmeth = classmethod(cmeth)  # Делает cmeth методом класса (или @ впереди)


obj = Methods()  # Нормальные методы экземпляров Допускает вызов через экземпляр или класс
print('obj. imeth(1):', obj. imeth(1))
print('Methods.imeth(obj, 2):', Methods.imeth(obj, 2))
