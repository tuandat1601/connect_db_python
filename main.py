# import json
# from sys import intern
# person = '{"name": "dat", "age": 21}'
# person_dict = json.loads(person)
# strg = json.dumps(person_dict,indent=5)
# with open("ex.json",'w+',encoding='utf-8') as f:
#     json.dump(person_dict,f,ensure_ascii=False,indent=4)


# class Networkerror(RuntimeError):
#     def _init_(self, arg):
#         self.args = arg


# try:
#     raise Networkerror("Bad hostname")
# except Networkerror as e:
#     print(e.args)

from tkinter import N


class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x
a= fibonacci_numbers(6)

def square(nums):
    for num in nums:
        yield num**2

# print(sum(square(fibonacci_numbers(10))))
animals = {'cat', 'dog', 'fish', 'otter',4}
for idx, animal in enumerate(animals):
    if animal == 4:
        animal =8
    print('#%d: %s' % (idx + 1, animal))
