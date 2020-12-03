# -*- coding: utf-8 -*-

import pandas as pd

course = pd.read_csv('p3_input.txt', header=None)

combinations = [[1, 1, 0], [3, 1, 0], [5, 1, 0], [7, 1, 0], [1, 2, 0]] # store different ways of traversing + number of trees encountered for each method in format [Right X, Down Y, Trees]

i, incr, inci, t, ans = 0, 0, 0, 0, 1 # initialise variables for the below for loop - 'ans' starting at 1 so that it can be multiplied by the number of trees for the answer

for element in combinations:
    incr = element[1] #number of rows to increment by
    inci = element[0] #number of elements to increment i by
    
    t, i = 0, 0 # reset t & i
    
    for index, row in course.iterrows(): # run through the series
        if index % incr == 0 & ~(index == 0):   # check if the row number is divisible by 'incr' and not 0 (first element is not counted for the challenge)
            if row.iloc[0][i] == '#': # check if the element at position i contains a 'tree' (#)
                t += 1              #increment t to count number of 'trees' encountered
            i = (i + inci) % 31     #increment i by number right required, then modulo 31 to 'loop' it back round to the start of the row
    element[2] = t #store number of trees enountered for each set of instructions (for error checking and check vs part 1 answer)
    
    ans *= t

print(ans)
