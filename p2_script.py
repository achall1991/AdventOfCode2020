# -*- coding: utf-8 -*-

import pandas as pd

pws = pd.read_csv('p2_input.txt', header=None) # import text file into a pandas dataframe pws

pws[['num', 'letter', 'password']] = pws[0].str.strip().str.split(expand=True) # split out the data from the imported text file into separate columns by whitespace
pws[['imin', 'imax']] = pws['num'].str.split('-', expand=True).astype('int64') # separate the minimum and maximum values into two new columns
pws['letter'] = pws['letter'].str.strip(':') # remove character : from the letter column

pws['lcount'] = pws.apply(lambda x: x['password'].count(x['letter']), axis=1) # create column of instances of 'letter' in 'password'

pws['count'] = ( pws['lcount'] >= pws['imin'] ) & ( pws['lcount'] <= pws['imax'] ) # create a new column of True/False if a password is valid

print('part 1: ' + str(pws['count'].sum())) # print answer

pws['let_1'] = pws.apply(lambda x: x['password'][x['imin']-1], axis=1) # extract the letter in 'password' indexed by the number 'imin'
pws['let_2'] = pws.apply(lambda x: x['password'][x['imax']-1], axis=1) # extract the letter in 'password' indexed by the number 'imax'

pws['count_2'] = ( pws['let_1'] == pws['letter'] ) ^ ( pws['let_2'] == pws['letter']) # true or false using XOR

print('part 2: ' + str(pws['count_2'].sum())) # print answer