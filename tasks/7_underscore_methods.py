"""
_single_leading_underscore
Таким способом задаются частные переменные, функции, методы и классы в модуле. Все, что использует такой способ задания
имени, будет проигнорировано в from module import *.

single_trailing_underscore_
Такой метод задания имен используется для избежания конфликтов со встроенными именами или классами.

__double_leading_underscore
Двойное подчеркивание (__) используется для искажения имен атрибутов в классе. Если мы создадим метод с именем
«__method» в классе с именем «ClassName», то вызвать этот метод так: «ClassName.__method» — у нас уже не получится.
Любой идентификатор формы __spam(не менее двух ведущих подчеркиваний, не более одного подчеркивания в конце) текстуально
 заменяется на _classname__spam, где classname- текущее имя класса с удаленными ведущими подчеркиваниями. Это изменение
 выполняется без учета синтаксической позиции идентификатора, поэтому его можно использовать для определения частных
 экземпляров и переменных класса, методов, переменных, хранящихся в глобальных объектах, и даже переменных, хранящихся в
  экземплярах. закрытый для этого класса в экземплярах других классов.

__double_leading_and_trailing_underscore__
Такой способ именования используется для специальных переменных или функций, таких как __init__ или __len__.
"""

print(__doc__)