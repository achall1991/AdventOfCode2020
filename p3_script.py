# -*- coding: utf-8 -*-

import pandas as pd

course = pd.read_csv('p3_input.txt', header=None)

combinations = [[1, 1, 0], [3, 1, 0], [5, 1, 0], [7, 1, 0], [1, 2, 0]]

i, incr, inci, t, ans = 0, 0, 0, 0, 1

for element in combinations:
    incr = element[1]
    inci = element[0]
    
    t = 0
    i = 0
    
    for index, row in course.iterrows():
        if index % incr == 0 & ~(index == 0):
            if row.iloc[0][i] == '#':
                t += 1
            i = (i + inci) % 31                
    element[2] = t
    
    ans *= t

print(ans)