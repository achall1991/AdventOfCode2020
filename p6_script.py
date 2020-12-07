# -*- coding: utf-8 -*-

import pandas as pd
import re

data = open('p6_input.txt', 'r').read()        #open input data as a string

def unique_count(string_input):
    k=list()
    for char in string_input:
        if re.search(r'\S', char) and char not in k:        #if a chracter exists and is not already on the list, append the list with it
            k.append(char)
    return len(k)                                           #return the final length of the list

dataframe_part_1 = pd.DataFrame([x.split(';') for x in data.split('\n\n')])     #read the input data as a dataframe

answer_part_1 = dataframe_part_1[0].apply(unique_count).sum()                   #apply the function above and sum the total

series_for_part_2 = dataframe_part_1[0].str.split('\n')                         #create a series of lists for each group member's answers for part 2

def part2_count(list_input):
    list_working = list(filter(None, list_input))   #remove empty list items
    k = {}
    valid_chars = ''
    for element in list_working:
        for character in element:                   #checks if a character exists for the element being iterated over
            if character in k:                      #if the character exists, iterate the dictionary value for that character by 1
                k[character] += 1
            else:
                k[character] = 1
            if k[character] == len(list_working):   #checks if the total number of characters 'counted' in the dictionary is equal to the length of the list being input (i.e. the total number of people in the group)
                valid_chars += character            #append the list of characters contained in every list item
    return valid_chars
        
answers_2 = series_for_part_2.apply(part2_count)    

ans_part_2 = answers_2.str.count(r'\S').sum()            #count non-whitespace, new line etc characters for the answer

