from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from collections import defaultdict
from urllib.request import *
from time import sleep, time
import itertools
import re
from lorem import text

# with open("sample.txt", "w") as f:
#     for i in range(2):
#         f.write(text())
import os


def counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0

    with open(fname, 'r') as f:
        # line by line
        for line in f:
            line = line.strip(os.linesep)
            wordslist = line.split()

            num_lines = num_lines + 1

            num_words = num_words + len(wordslist)
            num_charc = num_charc + \
                sum(1 for x in line if x not in (os.linesep, ' '))
            num_spaces = num_charc + \
                sum(1 for x in line if x in (os.linesep, ' '))

    print("Number of words in text file: ", num_words)
    print("Number of lines in text file: ", num_lines)
    print("Number of characters in text file: ", num_charc)
    print("Number of spaces in text file: ", num_spaces)

# counter('sample.txt')


def map_words(filename):
    data = []
    with open(filename, "r") as file:
        data = file.read()
    text = re.sub('[^a-z\ \']+', " ", data)
    words = list(text.split())
    return words
# print(map_words("sample.txt")[:5])


def wordcount(*args, **kwargs):
    d = defaultdict(list)
    for arg in args:
        if type(arg) == str:
            print("ddd")
            d['str'].append(arg)
        elif type(arg) == list:
            print("ffff")
            d['list'] += arg
    d = {**d, **kwargs}
    print(dict(d))

# wordcount("3", [1,2],x=4,y="d")


def f(x):
    '''run time'''
    sleep(1)
    return x*x


L = list(range(8))

# if __name__ == '__main__':

#     begin = time()
#     with ProcessPoolExecutor() as pool:

#         result = sum(pool.map(f, L))
#     end = time()

#     print(f"result = {result} and time = {end-begin}")
#     begin = time()
#     with ThreadPoolExecutor() as pool:

#         results = sum(pool.map(f, L))
#     end = time()
#     print(results,end-begin)


base_url = "http://www.thelatinlibrary.com/"
home_content = urlopen(base_url)
soup = BeautifulSoup(home_content, "lxml")
author_page_links = soup.find_all("a")
author_pages = [ap["href"] for i, ap in enumerate(author_page_links) if i < 49]
print(author_pages )

