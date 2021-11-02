"""
• Как создать класс без инструкции class  ?!  # https://habr.com/ru/post/145835/  Метаклассы
"""
# type(имя класса, кортеж родительских классов, словарь атрибутов)
D6 = type('D6', (), {})  # имя класса, кортеж родительских классов, словарь атрибутов

print(isinstance(D6, type))
print(type(D6))
print('\n')

print(isinstance(str, type))
print(type(str))
print('\n')

print(isinstance(object, type))
print(type(str))
print('\n')

print(issubclass(type, object))
print(isinstance(D6, object))
print(issubclass(D6, object))
print(issubclass(str, object))
print('\n')
