# -*- coding: utf-8 -*-

import pandas as pd

data = open('p4_input.txt', 'r').read()        #open input data as a string

passports = pd.DataFrame([x.split(';') for x in data.split('\n\n')]).replace(r'\n', ' ', regex=True)   #read input data as a pandas dataframe
passports = passports.rename(columns={0: 'input'})

definitions = ({'byr:':'Birth_Year',         #define category names to use as column titles
                'iyr:':'Issue_Year',
                'eyr:':'Expiration_Year',
                'hgt:':'Height',
                'hcl:':'Hair_Color',
                'ecl:':'Eye_Color',
                'pid:':'Passport_ID',
                'cid:':'Country_ID'
                })


regex_matches = ([  ['byr:', r'.*byr:(\d{4}).*'],         # regex patterns to populate/extract data with
                    ['iyr:', r'.*iyr:(\d{4}).*'],
                    ['eyr:', r'.*eyr:(\d{4}).*'],
                    ['hgt:', r'.*hgt:(\d+cm|\d+in).*'],
                    ['hcl:', r'.*hcl:(#[0-9a-f]{6}).*'],
                    ['ecl:', r'.*ecl:(amb|blu|brn|gry|grn|hzl|oth).*'],
                    ['pid:', r'.*pid:(\b\d{9}\b).*'],
                    ['cid:', r'.*cid:(\S+).*']
                ])

for element in regex_matches:
    passports[definitions[element[0]]] = passports['input'].str.extract(element[1]) #extract data based on regex in regex_matches and assign to a new column

cleaned = passports.dropna(subset=['Birth_Year', 'Issue_Year','Expiration_Year','Height','Hair_Color','Eye_Color','Passport_ID']) #create new dataframe without the missing data for these columns

numeric_cols = ['Birth_Year', 'Issue_Year', 'Expiration_Year'] # columns to convert to numeric values for validation/cleaning

cleaned[numeric_cols] = cleaned[numeric_cols].apply(pd.to_numeric, errors='coerce', axis=1) # convert the columns in the list 'numeric_cols' to numeric data types


# clean up remaining invalid data:

cleaned = cleaned[(cleaned['Birth_Year'] >= 1920) & (cleaned['Birth_Year'] <= 2002)]
cleaned = cleaned[(cleaned['Issue_Year'] >= 2010) & (cleaned['Issue_Year'] <= 2020)]
cleaned = cleaned[(cleaned['Expiration_Year'] >= 2020) & (cleaned['Expiration_Year'] <= 2030)]

cleaned['Height_in'] = cleaned['Height'][cleaned['Height'].str.contains('in')].str.replace('in', '').astype(int) # create separate column for height in inches as integers for validation
cleaned['Height_cm'] = cleaned['Height'][cleaned['Height'].str.contains('cm')].str.replace('cm', '').astype(int) # create separate column for height in centimetres as integers for validation

cleaned = cleaned[((cleaned['Height_in'] >= 59) & (cleaned['Height_in'] <= 76)) | ((cleaned['Height_cm'] >= 150) & (cleaned['Height_cm'] <= 193))]