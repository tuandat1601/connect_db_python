# Boolean operators
# The difference between Annie’s age (25) and Ellie’s (21)
import math
print(27-24)
# The total of $14.99, $27.95, and $19.83
print(14.99 + 27.95 + 19.83)
# The area of a rectangle of length 20 and width 15
print(20*15)
# 2 to the 10th power
print(2**10)
# The minimum of 3, 1, 8, -2, 5, -3, and 0
print(min(min(3, 1, 8, -2, 5, -3, 0)))
print(3 == 4-2)
# The value of 17//5 is 3
print(17//5 == 3)
# The value of 17%5 is 3
print(17 % 5 == 3)
# 284 is even
print(284 % 2 == 0)

# 284 is even and 284 is divisible by 3
print(284 % 2 == 0 and 284 % 2 == 0)
# 284 is even or 284 is divisible by 3
print(284 % 2 == 0 or 284 % 2 == 0)

# String operators
s1 = 'good'
s2 = 'bad'
s3 = 'silly'
# 'll' appears in s3
print('ll' in s3)
# the blank space does not appear in s1
print(' ' not in s1)


# the concatenation of s1, s2,
# and s3
print(sum(s1, s2, s3))
# the blank space appears in the
# concatenation of s1, s2, and
# s3
print(' ' in s1 + s2 + s3)
# the concatenation of 10 copies
# of s3
print(10*s3)
# the total number of characters
# in the concatenation of s1, s2,
# and s3
print(len(s1+s2+s3))

# Lists methods
# You found another retailer selling the
# boots for $160.00; add this price to list
# lst
lst = [159.99, 160.00, 205.95, 128.83, 175.49]
# Compute the number of retailers
# selling the boots for $160.00
lst.append(160.00)
lst.count(160.00)
# Find the minimum price in lst
print(min(lst))
# Using c), find the index of the
# minimum price in list lst
lst.index(128.83)
# Using c) remove the minimum price
# from list lst
lst.remove(128.83)
# Sort list lst in increasing order
lst.sort()
# Standard Library module math
# a)
print(math.sqrt(3**2+4**2))
# b)
print(math.sqrt(3**2+4**2) == 5)
# c
print(math.pi * 10 ** 2)
# d
print(c=(2*5**2 < 7**2))
