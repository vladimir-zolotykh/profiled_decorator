#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
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
    def bar(self, x, y):
        print(x, y)


@Profiled
def add(x, y):
    return x + y


add(2, 3)
add(4, 5)
add.ncalls

s = Spam()
s.bar(2)
s.bar(3)
s.bar.ncalls
