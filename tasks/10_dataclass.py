"""
Эта функция является декоратором, который используется для добавления сгенерированных специальных методов к классам,
dataclass - это обычные классы, которые предназначены для хранения состояния, а не содержат много логики.
Каждый раз, когда вы создаете класс, который в основном состоит из атрибутов, вы создаете dataclass.
dataclasses модуль заботится о большом количестве шаблонов.

Это особенно полезно, когда ваш класс данных должен быть хешируемым;
потому что для этого нужен не только __hash__метод, но и __eq__метод. Если вы добавите собственный __repr__метод для
упрощения отладки, он может стать довольно большим.
https://stackoverflow.com/questions/47955263/what-are-data-classes-and-how-are-they-different-from-common-classes
"""
from dataclasses import dataclass


@dataclass
# @dataclass()
# @dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=False)
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


ii = InventoryItem(name='myname', unit_price=10.10, quantity_on_hand=5)
print(ii.name, ii.unit_price, ii.quantity_on_hand, ii.total_cost())
ii2 = InventoryItem(name='myname2', unit_price=11.11, quantity_on_hand=55)
print(ii2.name, ii2.unit_price, ii2.quantity_on_hand, ii2.total_cost())
# print(ii < ii2)
# order: Если это True (по умолчанию False), __lt__(), __le__(), __gt__(), и __ge__()методы будут генерироваться.
# Они по порядку сравнивают класс, как если бы он был кортежем его полей.
