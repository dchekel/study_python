'''
свойство представляет собой тип объ­ екта, присвоенного имени атрибута класса. Для создания свойства необходимо вы­
звать встроенную функцию property и передать ей три метода доступа (обработчики операций получения, установки и
удаления), а также необязательную строку докумен­ тации для свойства. Если любой из аргументов опущен или для него
передается None, то связанная с ним операция не поддерживается.
Встроенная функция property позволяет ассоциировать методы с операциями извлечения и установки для специфического
атрибута класса.
class Data:
    """
    https://all-python.ru/osnovy/klassy.html#abstraktnye-metody
    С помощью специального механизма свойств класса можно внести корректировки в работу с оператором точки, присвоив ему
     собственные функции. В следующем примере представлен класс с приватным полем x, для которого написаны
     getter и setter. С помощью присвоения полю x специального значения функции property, получающей в качестве
     аргументов имена методов, можно настроить работу оператора точки согласно своим нуждам.
    """
    def __init__(self, x):
        self.__set_x(x)

    def __get_x(self):  # при вызове оператора точка, например в "data.x" , вызывается этот метод
        print("Get X")
        return self.__x

    def __set_x(self, x):  # при установке значения "data.x = 20"  вызывается этот метод
        self.__x = x
        print("Set X")

    def __del_x(self):
        self.__x = 'No more'
        print("del X")

    x = property(__get_x, __set_x, __del_x, 'Это свойство x.')
    # (получение, установка, удаление, строка документации) либо использовать @


data = Data(10)
data.x

print('print(data.x)', data.x, data.x)

data.x = 20
data.x = 25
print('\nprint(data.x)', data.x)

del data.x
print(dir(data))
print(dir(Data))
'''


class Mine:

    def __init__(self):
        self._x = None

    x = property()

    @x.getter
    def x(self):
        """Это свойство x."""
        print("@x.getter")
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        print('@x.setter')

    @x.deleter
    def x(self):
        self._x = 'No more'
        print('@x.deleter')


print('\nm = Mine()')
m = Mine()

print('\nm.x = 100')
m.x = 100

print('\nprint(m.x)')
print(m.x)


