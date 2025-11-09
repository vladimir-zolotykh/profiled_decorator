#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> add(2, 3)
5
>>> add.__name__
'add'
>>> add(4, 5)
9
>>> add.ncalls
2
>>> s = Spam()
>>> s.bar(2)
<__main__.Spam object at 0x...> 2
>>> s.bar.__name__
'bar'
>>> s.bar.__doc__
'Prints self, x'
>>> s.bar(3)
<__main__.Spam object at 0x...> 3
>>> s.bar.ncalls
2
"""
from functools import wraps
from types import MethodType


class Profiled:
    def __init__(self, func):
        self.ncalls = 0
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if not instance:
            return self
        return MethodType(self, instance)


class Spam:
    @Profiled
    def bar(self, x):
        """Prints self, x"""
        print(self, x)


@Profiled
def add(x, y):
    return x + y


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
