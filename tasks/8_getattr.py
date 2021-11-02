"""
object.__getattr__(self, name)
Позволяет определить поведение экземпляра пользовательского типа при попытке получения значения атрибута.
Вызывается в случае, когда значение атрибута не удалось получить обычным способом (не определён ни для экземпляра,
ни в иерархии типов данного экземпляра).
Метод не вызывается, если значение удалось получить обычным способом (см. выше). Это намеренное отличие от
object.__setattr__, обусловленное как соображениями производительности, так и тем, что иначе метод не имел бы доступа к
прочим атрибутам экземпляра.

__getattribute__(self, name)
вызывается при попытке доступа к атрибуту экземпляра класса.
Метод должен вернуть вычисленное значение для указанного атрибута, либо поднять исключение AttributeError.

getattr(obj, name[, default])
default : Значение по умолчанию, которое будет возвращено, если объект не располагает указанным атрибутом.
Если не задано, и атрибут отсутствует, возбуждается исключение AttributeError.
"""


class First(object):
    attr = 'my_attr'

    def __getattr__(self, name):
        return 'my_%s_val' % name


class Second:
    my_first_attr = 1

    def __getattribute__(self, name):
        if name == 'my_second_attr':
            return 'some attr'
        else:
            return object.__getattribute__(self, name)


f1 = First()
print('__getattr__')
print('f1.attr', f1.attr)  # my_attr
print('f1.attr1', f1.attr1)  # my_attr1_val
print('f1.attr2', f1.attr2)  # my_attr2_val
print('\n')
f2 = Second()
print('__getattribute__')
print('f2.my_first_attr', f2.my_first_attr)  # some attr
print('f2.my_second_attr', f2.my_second_attr)  # some attr
try:
    print('f2.my_third_attr', f2.my_third_attr)  #
except AttributeError:
    print('f2.my_third_attr not exist')  #

print('\n')
print('getattr(obj, name[, default])')
attr1 = getattr(f1, 'attr', 'attr not in obj')
attr_not = getattr(f1, 'attr_n', 'attr not in obj')
print(attr1)  # my_attr
print(attr_not)  # my_attr_n_val
