# import datetime
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.datetime.now()
#         result = func(*args, **kwargs)
#         end = datetime.datetime.now()
#         print(end - start, '-vaqt ketdi')
#         return result
#     return wrapper
#
#
# @timer
# def add_two_numbers(a, b):
#     sum = a + b
#     return sum
#
#
# @timer
# def daraja(a, b):
#     daraja = a ** b
#     return daraja
#
#
# print(add_two_numbers(1, 2))
# print(daraja(1, 2))

# multy decorator
# def decor1(func):
#     def wrapper(*args, **kwargs):
#         x = func(*args, **kwargs)
#         return x*x
#     return wrapper
#
# def decor2(func):
#     def wrapper(*args, **kwargs):
#         x = func(*args, **kwargs)
#         return x*2
#     return wrapper
#
# @decor2
# @decor1
# def num():
#     return 10
#
# @decor1
# @decor2
# def num2():
#     return 10
#
# print(num()) #
# print(num2())
#
# class Logger:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("Logger called")
#         result = self.func(*args, **kwargs)
#         print(f"Logged result: {result}")
#         return result
#
#
# # @Logger
# def divide(a, b):
#     try:
#         d = a / b
#     except ZeroDivisionError:
#         print("Division by zero")
#         d=None
#     except Exception as e:
#         print(e)
#         d = None
#     return d
#
#
# print(divide(2, 0))

# for i in [1,2,3,4,5]:
#     print(i)
# a = iter([1, 2, 3, 4, 5])
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
#
# class MyIterator:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start == self.end:
#             raise StopIteration
#         else:
#             self.start += 1
#             return self.start - 1
#
#
# my_iterator = MyIterator(2, 10)
# for i in my_iterator: # 1.iter._next_ = 2, 2-iter._next_=3
#     print(i)

def yrange(n):
    i = 0
    while i < n:
        yield i # 1- toxtadi
        i += 1 # i = 1

# iter_ = yrange(100)
# print(iter_)
# def xrange(n):
#     return range(n)
# print(list(xrange(5)))

for i in yrange(10):
    print(i)

def yrange(n):
    pass

print(yrange(5))
print(yrange(5))
print(yrange(5))

print(yrange(5))