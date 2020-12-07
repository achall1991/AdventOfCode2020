# -*- coding: utf-8 -*-

import pandas as pd
from statistics import mean
import math

data = pd.read_csv('p5_input.txt', header=None)

data['row'] = data[0].str.extract(r'(\S{7})')
data['column'] = data[0].str.extract(r'(\S{3}\b)')

def ref_calculate(column, calc_cols): 
    loc = [0, 127]                              # set the maximum possible pair of values when looking for a row
    if calc_cols == True:
        loc[1] = 7                              # if looking for a column, reduce the maximum possible value
    for element in column[:-1]:                 # run through each letter except for the last
        if element == 'B' or element == 'R':    # if each element is a B or an R (higher half), increase the minimum value by the mean of both potential values
            loc[0] = math.ceil(mean(loc))
        else:                                   # otherwise reduce the maximum value by the mean of both potential values
            loc[1] = math.floor(mean(loc))
    if column[-1] == 'B' or column[-1] == 'R':  # if the final value in the string is a B or an R, return the highest value, otherwise return the lowest
        return loc[1]
    else:
        return loc[0]

data['row_num'] = data['row'].apply(ref_calculate, calc_cols=False)
data['col_num'] = data['column'].apply(ref_calculate, calc_cols=True)

data['seat_id'] = ( data['row_num'] * 8 ) + data['col_num']  # answer is the maximum of this value

#find a seat ID where: ID does not exist but ID + 1 and ID -1 exists

for i in range(data['seat_id'].min(), data['seat_id'].max()):
    if ( i+1 in data['seat_id'].unique() ) and ( i-1 in data['seat_id'].unique() ) and ( i not in data['seat_id'].unique()):
        print(i)    #uses series.unique() to check if the number i does not exist along with i+1 and i-1 (adjacent seats) existing with it
