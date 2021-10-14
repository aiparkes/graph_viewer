import pandas as pd
import streamlit as st
import numpy as np
from datetime import date
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from custom_components.layout import _max_width_
from rating_boundary_funcs import derive_boundaries, tidy_for_print
from illustration import plot_boundaries_and_K
_max_width_()

##title including interactive vessel name and IMO number user inputs
col1, col2, col3 = st.columns([0.8,0.15,0.05])
col2.image('illustration_resources/oldendorff.png', width=200)
##user input
ship_name = col2.text_input('Vessel Name', '')
imo_num = col2.text_input('IMO Number', '')
##title
col1.header(ship_name+' IMO '+imo_num+': CII Tool (Bulk Carrier Prototype)')
col1.write('2020 AER Plot as of '+date.today().strftime('%A %d %B %Y'))

##all other user input
col1, col2, col3 = st.columns([0.8,0.15,0.05])
vessel_type = col2.selectbox('Vessel Type',('Bulk Carrier',''))
input_DWT = col2.number_input('Vessel Deadweight', value=260000)
input_AER = col2.number_input('Input AER', value=1.5)
perc_decr = col2.number_input('Percentage Decrease Post 2026', value=3.0, format="%.1f", step=0.1)

##derive rating boundaries and colours/ratings of input
reference_lines = derive_boundaries(perc_decr, input_DWT, input_AER, vessel_type)

#plot figures
fig = plot_boundaries_and_K(reference_lines)
col1.plotly_chart(fig, use_container_width = True)

##print data from reference lines
col1, col2, col3, col4, col5, col6 = st.columns([0.1,0.5,0.05,0.15,0.06, 0.09])
reference_lines = tidy_for_print(reference_lines)
col2.dataframe(reference_lines[['Percentage Decrease','A','B','Reference line','D','E']].transpose())


##white space for locating logo at bottom of table
col3.text('')
col4.text('')
col5.text('')
col6.text('')
col3.text('')
col4.text('')
col5.text('')
col6.text('')
col3.text('')
col4.text('')
col5.text('')
col6.text('')
col3.text('')
col4.text('')
col5.text('')
col6.text('')
col3.text('')
col4.text('')
col5.text('')
col6.text('')
col3.text('')
col4.text('')
col5.text('')
col6.text('')
col3.text('')
col4.text('')
col5.text('')
col6.text('')
col3.text('')
col4.text('')
col5.text('')
col6.text('')
col3.text('')
col4.text('')
col5.text('')
col6.text('')
col3.text('')
col4.text('')
col5.text('')
col6.text('')
col3.text('')
col4.text('')
col5.text('')
col5.write('Powered by ')
col6.image('illustration_resources/arcsilea.png')
