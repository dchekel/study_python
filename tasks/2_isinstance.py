"""
Возвращает флаг, указывающий на то, является ли указанный объект экземпляром указанного класса (классов)
, либо наследующегося от него класса.
isinstance(obj, classinfo) -> bool
"""
print(__doc__)
print('isinstance(10, int)->', isinstance(10, int))  # True
print('isinstance("some value", str)->', isinstance('some value', str))  # True
print('isinstance(10.3, float)->', isinstance(10.3, float))  # True
print('\n')
print('isinstance(10, object)->', isinstance(10, object))  # True
print('isinstance("some value", object)->', isinstance('some value', object))  # True
print('isinstance(10.3, object)->', isinstance(10.3, object))  # True
print('\n')
print('isinstance("100", (float, int, str))->', isinstance(10.3, (float, int, str)))  # True
