# -*- coding: utf-8 -*-
import pandas as pd

## --- Read and convert data into a DataFrame so it can be used ---
data = pd.read_csv('p7_input.txt', header=None, sep='\n').rename(columns={0:'input_data'})

data['bag_type'] = data['input_data'].str.extract(r'(\S+ \S+) bags.*') # regex to extract the 'parent' bag
data['bags_held'] = data['input_data'].str.extract(r'contain (.*)')
data['bags_held'] = data['bags_held'].str.replace(r'(bags)|(bag)|(\.)', '') # regex to extract child bags of each parent in a format to be used in a dataframe

bags = data['bags_held'].str.split(',', expand=True) # create a new dataframe with a column for each type of child bag
bags['parent_bag'] = data['bag_type'] # add the parent bag names for each set of children

bags = bags.apply(lambda x: x.str.strip() if x.dtype == "object" else x) #strip all extra whitespace from the dataframe
bags = bags.melt(id_vars=['parent_bag']).dropna() #convert the children into a single column so that they can be iterated on

bags['num_children'] = bags['value'].str.extract(r'([0-9])').fillna(0).astype(int) # extract the number of each child bag and convert to int
bags['value'] = bags['value'].str.extract(r'[0-9] (\w+ \w+)') #remove the number from the string containing the child bag as it is now in another column
bags = bags.rename(columns={'value':'child_bag'}).dropna() #rename the column and remove NaN values (i.e. remove bags with no children)


## --- process data in order to solve the problem ---
bag_series = bags['parent_bag'][bags['child_bag'].str.contains('shiny gold')] # create a series of bags that contain a shiny gold bag

i = 0

while i != len(bag_series): #runs until the size of bag_series stops changing (i.e. there are no more bags to be found)
    i = len(bag_series)
    for bag in bag_series:
        bag_series = bag_series.append(bags['parent_bag'][bags['child_bag'] == bag]).drop_duplicates() # append the list of bags with all children of bags already on the list

print(len(bag_series)) # answer for part 1


def recurs_search(bag_to_search):
    if bags['child_bag'][bags['parent_bag'].str.contains(bag_to_search)].empty: # check if no children exist
        return 1
    else:
        n = 0
        for bag in bags['child_bag'][bags['parent_bag'].str.contains(bag_to_search)]: # for each child bag of the parent bag
            i = bags['num_children'][(bags['parent_bag'].str.contains(bag_to_search)) & (bags['child_bag'].str.contains(bag))].sum() #number of children
            i *= recurs_search(bag) # function calls itself to recursively calculate the number of child bags for the bag being checked
            n += i
    return n + 1

print(recurs_search('shiny gold') - 1) # answer for part 2. returns 1 too high for reasons i have not been able to figure out
