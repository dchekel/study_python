class WithSlots:
    """
    __slots__ позволяет снизить объём памяти, потребляемой экземплярами класса, ограничивая количество атрибутов ими поддерживаемых.
    В __slots__ могут быть перечислены атрибуты для значений которых требуется зарезервировать место
    В качестве значения __slots__ может быть указана строка, объект поддерживающий итерирование, или последовательность
    строк с именами атрибутов, использующихся экземплярами.
    """
    # __slots__ = ['static_attr1', 'static_attr2', 'static_attr3']  # или так
    # __slots__ = 'static_attr'  # или так
    __slots__ = 'static_attr1', 'static_attr2', 'static_attr3'  # или так


# a = Ordinary()
b = WithSlots()

# a.__dict__  # {}
try:
    print(b.__dict__)  # AttributeError
except AttributeError:
    print('ошибка атрибута __dict__')

try:
    # a.__weakref__  # None
    print(b.__weakref__)  # AttributeError
except AttributeError:
    print('ошибка атрибута __weakref__')

print(b.__doc__)
# a.static_attr = 1
b.static_attr1 = 1
print('b.static_attr1=', b.static_attr1)

b.static_attr2 = 2
print('b.static_attr2=', b.static_attr2)

b.static_attr3 = 3
print('b.static_attr3=', b.static_attr3)

try:
    # a.dynamic_attr = 2
    b.dynamic_attr = 2  # AttributeError
except AttributeError:
    print('ошибка атрибута dynamic_attr')
