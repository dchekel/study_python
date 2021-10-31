print(list.__mro__)  # (list, object)


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class BC(B, C):
    """
    __mro__ Содержит кортеж с родительскими типами, выстроенными в порядке разрешения методов.
    """
    pass


print(BC.__mro__)  # (__main__.BC, __main__.B, __main__.C, __main__.A, object)
