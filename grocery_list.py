#!/usr/bin/env python3

# Simple program that help to make a list of produkts to buy in grocery store.

import os

print('The List 1.0 by Theodor Rundome')

list = [] # Initiate of empty list.
while True:
    item = input('To buy: ')
    if item == '':
        break

    item = list.append(item)
    print(list)

os.system('clear')
print('To buy: ')

file = open('list', 'w')

for item in list:file.write(item + '\n')
file.close()
os.system('cat list')
print()
print('thx!')

