# -*- coding: utf-8 -*-

#INSTRUCTIONS:
#    nop = do nothing, advance to next step (equivalent to jmp where n = 1)
#    acc = increase accumulator by n
#    jmp = jump forward or ahead by n steps

import pandas as pd

program_data = pd.read_csv('p8_input.txt', header=None, sep='\n')[0].str.split(' ', expand=True).rename(columns={0:'instruction', 1:'value'}) # read in the input data to a dataframe

program_data['value'] = program_data['value'].astype(int)   #convert the instruction values to integers for performing calculations
program_data['line_ran'] = False                            #add a column to track whether the line has been run once or not

substitution = {'nop':'jmp', 'jmp':'nop'}                   #dictionary for substituting nop with jmp for part 2

list_of_instructions = program_data[(program_data['instruction'] == 'nop') | (program_data['instruction'] == 'jmp')] # index of all occurences of jmp and nop for part 2


## for part 1, remove this for loop
for lineref in list_of_instructions.index:
    data = program_data.copy()                                                          #copy data into a fresh dataframe so that the original is not changed
    data.loc[lineref, 'instruction'] = substitution[data.loc[lineref, 'instruction']]   #substitute one instance of jmp for loc or vice versa before testing the program
    i, line, acc_value = False, 0, 0                  # reset variables
    while i == False:
        if data.loc[line, 'line_ran'] == False:       #'run' the program by iterating through the dataframe, adjusting index depending on the instruction given
            data.loc[line, 'line_ran'] = True
            if data.loc[line, 'instruction'] == 'jmp':
                line += data.loc[line, 'value']
            elif data.loc[line, 'instruction'] == 'nop':
                line += 1
            elif data.loc[line, 'instruction'] == 'acc':
                acc_value += data.loc[line, 'value']
                line += 1
            if line == 594:                 #if the program reaches line number 594 (i.e. the last line + 1) the program has run successfully
                i = True
        else:                               #exit the while loop if an instruction has been run twice (if 'line_ran' reads True)
            i = True
    if line == 594:                          #if the program has run successfully, the for loop can be exited
        break

print(acc_value)
