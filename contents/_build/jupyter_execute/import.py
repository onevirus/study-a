Import
======

https://docs.python.org/3/tutorial/modules.html?highlight=package#modules

## string varialbe 로 import 하기

import importlib

mod = importlib.import_module("datetime")

print(mod.datetime.utcnow())
print(mod.__file__)
dir(mod)

import importlib

a = importlib.import_module("concurrent.futures.thread")
print(a.__file__)

b = importlib.import_module(".futures", "concurrent")
print(b.__file__)

c = importlib.import_module(".futures.thread", "concurrent")
print(c.__file__)

d = importlib.import_module(".ElementTree", "xml.etree")
print(d.__file__)