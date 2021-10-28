import pandas as pd
import numpy as np


def rate_input(ref):
    ref['rating'] = None
    ref.at[ref[ref.input < ref.A].index, 'rating'] = 'A'
    ref.at[ref[(ref.input > ref.A)&(ref.input < ref.B)].index,  'rating'] = 'B'
    ref.at[ref[(ref.input > ref.B)&(ref.input < ref.D)].index,  'rating'] = 'C'
    ref.at[ref[(ref.input > ref.D)&(ref.input < ref.E)].index,  'rating'] = 'D'
    ref.at[ref[(ref.input > ref.E)].index,  'rating'] = 'E'
    return ref

def colour_input(ref):
    ref['colour'] = None
    ref.at[ref[ref.input < ref.A].index, 'colour'] = '#72AE59'
    ref.at[ref[(ref.input > ref.A)&(ref.input < ref.B)].index, 'colour'] = '#B0CB5C'
    ref.at[ref[(ref.input > ref.B)&(ref.input < ref.D)].index, 'colour'] = '#DCE47C'
    ref.at[ref[(ref.input > ref.D)&(ref.input < ref.E)].index, 'colour'] = '#F6CA96'
    ref.at[ref[(ref.input > ref.E)].index, 'colour'] = '#F4B2A9'
    return ref

def derive_rating_bounds(ref):
    #might vary with diff ship type/size??
    boundaries = {'A':0.86,'B':0.94,'D':1.06,'E':1.18}
    ref['A'] = ref['Reference line']*boundaries['A']
    ref['B'] = ref['Reference line']*boundaries['B']
    ref['D'] = ref['Reference line']*boundaries['D']
    ref['E'] = ref['Reference line']*boundaries['E']
    return ref

def derive_boundaries(perc_decr, input_DWT, input_AER, vessel_type):
    ##bulk carrier cruve specifics, import from resources when implement more ship types
    bulk_ref_line = lambda DWT : 4745*(DWT**-0.622)
    if input_DWT > 279000:
        input_DWT = 279000
    ##percentage decrease in AER for each year might need to vary the number of years later?
    yearly_decrease = {2021:2,2022:3,2023:5,2024:7,2025:9,2026:11,2027:11+perc_decr,2028:11+perc_decr*2,2029:11+perc_decr*3,2030:11+perc_decr*4}
    ##dataframe for main illustration
    ref = pd.DataFrame(columns=['A','B','Reference line','D','E'])
    ref['Percentage Decrease'] = yearly_decrease.values()
    ref['Reference line'] = [bulk_ref_line(input_DWT)*(1-perc/100) for perc in yearly_decrease.values()]
    ref = derive_rating_bounds(ref)
    ref['input'] = np.repeat(input_AER,len(ref.index))
    ref = rate_input(ref)
    ref = colour_input(ref)
    ##column for K-tool illustation
    ref['bar'] = np.repeat(1,len(ref.index))
    ##make index year from perc decrease
    ref['year'] = yearly_decrease.keys()
    ref = ref.set_index('year')
    return ref

def tidy_for_print(ref):
    ref = ref.round({'Percentage Decrease':0,'A':3,'B':3,'Reference line':3,'D':3,'E':3})
    ref['Percentage Decrease'] = ref['Percentage Decrease'].astype(str)
    ref['perc'] = '%'
    ref['Percentage Decrease'] = ref['Percentage Decrease']+ref.perc
    ref = ref.astype(str)
    return ref
