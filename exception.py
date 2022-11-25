

# def upper_text(func):
# 	def inner(*args):
# 		ms= func(*args)
# 		ms = ms.upper()
# 		return ms
# 	return inner
# def split_text(func):
# 	def inner(*args):
# 		ms = func(*args)
# 		ms=ms.split()
# 		print(ms)
# 	return inner
# @split_text
# @upper_text
# def messe(msg):
# 	return msg
# numbers = [1, 2, 3, 4, 5] # iterable
# def square(x):
#     return x ** 2
# numbers_squared = map(square, numbers)
# print(type(numbers_squared))
from contextlib import contextmanager


class Person:
    def __init__(self, fname: str = '', lname: str = '', age: int = 18):
        self.__fname = fname
        self.__lname = lname
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if age > 0:
            self.__age = age

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname: str):
        if fname.isalpha():
            self.__fname = fname

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def fname(self, lname: str):
        if lname.isalpha():
            self.__lname = lname

    @property
    def fullname(self):
        return f'{self.__fname}+{self.lname}'


dat = Person
dat.fname = 'dat'

dy = {'a': "vv", "b": "bb"}


def show_person_details(name: str, is_gangster: bool, is_hacker: bool, age: int):
    print('name: {}, gangster: {}, hacker: {}, age: {}'.format(
        name, is_gangster, is_hacker, age))


def func_with_loads_of_args(arg1, *, arg2=None, arg3=None, arg4=None, arg5='boom'):
    pass

def my_context():
    print('Entering to my context')
   
    print('Exiting my context')
    
def do_stuff():
    with my_context():
        print('Doing stuff')
        
    print('Doing some stuff outside my context')
        
def nat(*args):
    return sum(args)
print(nat(1,2,3,4))
