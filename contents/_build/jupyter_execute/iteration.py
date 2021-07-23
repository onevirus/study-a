Iteration
=======

### iterable

An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects, and objects of any classes you define with an `__iter__()` method or with a `__getitem__()` method that implements Sequence semantics.

Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), …). When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself. The for statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. See also iterator, sequence, and generator.

### iterator

An object representing a stream of data. Repeated calls to the iterator’s `__next__()` method (or passing it to the built-in function next()) return successive items in the stream. When no more data are available a StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further calls to its `__next__()` method just raise StopIteration again. Iterators are required to have an `__iter__()` method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.


iterator = iter(iterable)

iterable is a container. stateless
iterator 는 상태가 바뀜

# iterable

a = [1, 2, 3, 4, 5, 6, 7]

# iterator

b = iter(a)
print(b.__next__())
print(next(b))
for i in b:
    print(i)

c = a.__iter__()
print(next(c))
print(c.__next__())
print(list(c))

# generator

def gen():
    for row in [1, 2, 3, 4, 5]:
        yield row
        
g = gen()
print(next(g))
print(next(g))
print(next(g))
print(list(g))

list(range(10, -10, -3))