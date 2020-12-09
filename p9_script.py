# -*- coding: utf-8 -*-

import itertools as it

data = list( map( int, open('p9_input.txt', 'r').readlines())) # open input data as a list of ints
preamble_size = 25 # size of the preamble needed


def number_check(num, list_in):
    for item in list(it.combinations(list_in, 2)):
        if num == sum(item):                            #check if two items added together out of all combinations equal the number being checked
            return True
    return False

for i, item in enumerate(data[preamble_size:], preamble_size):
    if number_check(item, data[(i-preamble_size):(i)]) == False:
        num_to_solve = item                             #save the number that was found as a variable for later
        print(item)                                             
        break

def weakness_check(number, list_in):
    for n in range(0,len(list_in)):
        n_min, n_max, total = max(list_in),min(list_in),0       #initialise variables with highest and lowest possible values. can use 'inf' and '-inf' as well. avoids having additional lines further down
        for item in list_in[n:]:
            n_min = min(n_min, item)                            #store lowest number so far
            n_max = max(n_max, item)                            #store highest number so far
            total += item                                       #increase the total, check if it equals num_to_solve
            if total == number:
                return n_min + n_max                            #return the sum of the highest and lowest numbers
    return 0

print(weakness_check(num_to_solve, data))                       #print solution