# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

data = pd.read_csv('p7_input.txt', header=None, sep='\n').rename(columns={0:'input_data'})

data['bag_type'] = data['input_data'].str.extract(r'(\S+ \S+) bags.*')
data['bags_held'] = data['input_data'].str.extract(r'contain (.*)')
data['bags_held'] = data['bags_held'].str.replace(r'(bags)|(bag)|(\.)', '')

bags = data['bags_held'].str.split(',', expand=True)
bags['parent_bag'] = data['bag_type']

bags = bags.apply(lambda x: x.str.strip() if x.dtype == "object" else x) #strip all extra whitespace from the dataframe

bags = bags.melt(id_vars=['parent_bag']).dropna()

bags['num_children'] = bags['value'].str.extract(r'([0-9])').fillna(0)
bags['value'] = bags['value'].str.extract(r'[0-9] (\w+ \w+)')

bags = bags.rename(columns={'value':'child_bag'}).dropna()

unique_bag_list = data['bag_type']


bag_series = bags['parent_bag'][bags['child_bag'].str.contains('shiny gold')]

i, c = 1,0

bag_mult = 1

while i > 0:
    c = len(bag_series)
    for bag in bag_series:
        bag_series = bag_series.append(bags['parent_bag'][bags['child_bag'] == bag]).drop_duplicates()
    if c == len(bag_series):
        i = 0

