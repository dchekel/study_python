class Methods:
    def imeth(self, x):  # Нормальный метод экземпляра: передается self
        print([self, x])

    def smeth(x):  # Статический метод: экземпляр не передается
        print([x])

    @staticmethod
    def smeth2(x):  #
        """
        Статический метод: экземпляр или класс не передается
        его определение неизменяемо через наследование
        это просто функция, называемая синтаксически как метод, но без доступа к объекту и его атрибутам
        """
        print('вызов staticmethod smeth2', x)

    def cmeth(cls, х):
        """
        Метод класса: получает класс, а не экземпляр,
        можно переопределить дочерними классами.
        имеет доступ ко всем атрибутам класса
        """
        print('вызов classmethod cmeth', [cls, х])

    @classmethod
    def cmeth2(cls, y):
        print('вызов classmethod cmeth2', [cls, y])

    smeth = staticmethod(smeth)  # Делает smeth статическим методов (или @ впереди)
    cmeth = classmethod(cmeth)  # Делает cmeth методом класса (или @ впереди)


obj = Methods()  # Нормальные методы экземпляров Допускает вызов через экземпляр или класс
print('obj. imeth(1):', obj. imeth(1))
print('Methods.imeth(obj, 2):', Methods.imeth(obj, 2))

Methods.cmeth('method22')

obj.cmeth2('method2')

Methods.smeth('method smeth')
obj.smeth2('method smeth2')
