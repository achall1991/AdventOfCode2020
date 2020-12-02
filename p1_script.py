# -*- coding: utf-8 -*-

import pandas as pd

file = pd.read_csv('p1_input.txt', header=None)

for num in file[0]: #part 1 answer
    for num2 in file[0]:
        if num + num2 == 2020:
            print(num * num2)
            
            
for num in file[0]: #part 2 answer
    for num2 in file[0]:
        for num3 in file[0]:
            if num + num2 + num3 == 2020:
                print(num * num2 * num3)