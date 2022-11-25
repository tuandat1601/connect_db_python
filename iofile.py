import mo
import csv
# import xlrd
# excel_book = xlrd.open_workbook('sample.xls)
# print(excel_book.nsheets)
# print(excel_book.sheet_names)
# ------------------ START READ CSV FILE---------------------
# with open("csv_example.csv") as f:
#     csv_reader = csv.reader(f, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(row)
#             print(f'Column names are :{", ".join(row)}')
#             line_count += 1
#         else:
#             print(
#                 f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')

#     print(f'Number of lines:  {line_count}')
# ----------------------END READ------------------

# import xml.etree.ElementTree as ET
# tree = ET.parse('xml_example.xml')
# root = tree.getroot()
# print('Root tag:', root.tag)
# print('Attribute:', root.attrib)
# for child in root:
#     print('field: ', child.text)


# with open('barack_obama.txt', 'r+', encoding='utf-8') as f:
#     leng = 0
#     words=0
#     for row in f:
#         if len(row)>1:
#             words+=len(row)
#             leng += 1
#     print(leng,words)
def main():
    print("Hello World!")


# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n

#     n += 1
#     print('This is printed second')
#     yield n

#     n += 1
#     print('This is printed at last')
#     yield n
# a=my_gen()
# print(next(a))

class InfIter:
    """Infinite iterator to return all odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


a = iter(InfIter())
print(a[4])
