"""
== для равенства значений  (имеют ли два объекта одинаковое значение)
is для ссылочного равенства (ссылаются ли на две ссылки на один и тот же объект)
"""

a = [1, 2, 3]
b = a
print(__doc__)
print('\n')
print('a=', a, 'id=', id(a))
print('b=', b, 'id=', id(b))
print('b is a', b is a)  # True
print('b == a', b == a)  # True
print('\n')

b = a[:]
print('теперь b - это срез списка a')
print('a=', a, 'id=', id(a))
print('b=', b, 'id=', id(b))
print('b is a', b is a)  # True
print('b == a', b == a)  # True
