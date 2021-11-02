"""
https://www.rupython.com/__init__-__new__-19998.html
__new__ – это первый шаг создания экземпляра. Он вызывается первым и отвечает за возврат нового
экземпляра вашего класса.
Однако __init__ ничего не возвращает ; он отвечает только за инициализацию экземпляра после его
создания. Это конструктор
"""


class A(object):
    some_property = 'some_value'

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls, *args, **kwargs)
        obj.some_property = cls.some_property
        print('__new__ from class A', obj, obj.some_property)
        return obj


class B(A):
    some_property = 2

    def __new__(cls, *args, **kwargs):
        obj = super(B, cls).__new__(cls)
        print('__new__ from class B', obj, obj.some_property)
        return obj


b = B()
print(b)

# __new__ from class A <__main__.B object at 0x7fc0c7a08040> 2
# __new__ from class B <__main__.B object at 0x7fc0c7a08040> 2
# <__main__.B object at 0x7fc0c7a08040>
