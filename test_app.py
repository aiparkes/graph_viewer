import pandas as pd
import streamlit as st
from PIL import Image

#setting favicon
favicon = Image.open('illustration_resources/favicon.jpg')
st.set_page_config(page_title='CII Tool Bulk Carrier Prototype', page_icon=favicon)

import numpy as np
from datetime import date
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from custom_components.layout import _max_width_
from rating_boundary_funcs import derive_boundaries, tidy_for_print
from illustration import plot_boundaries_and_K

_max_width_()

##hide menu and footer
hide_menu_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

##Sidebar : Vessel Information
sidebarTitleTop= '<p style="font-weight: 700; color:#146EA6; font-size: 24px;">Vessel Information</p>'
st.sidebar.markdown(sidebarTitleTop, unsafe_allow_html=True)

ship_name = st.sidebar.text_input('Vessel Name', 'Anonymous Oldendorff ')
imo_num = st.sidebar.text_input('IMO Number', '1234567')
vessel_type = st.sidebar.selectbox('Vessel Type',('Bulk Carrier',''))

##decorative line
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

##Sidebar : Input
sidebarTitleBottom= '<p style="font-weight: 700; color:#146EA6; font-size: 24px;">Input</p>'
st.sidebar.markdown(sidebarTitleBottom, unsafe_allow_html=True)

input_DWT = st.sidebar.number_input('Vessel Deadweight', value=260000)
input_AER = st.sidebar.number_input('AER (Average Emissions Ratio)', value=1.5)

##decorative line
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

perc_decr = st.sidebar.number_input('Percentage Decrease Post 2026', value=3.0, format="%.1f", step=0.1)

st.image('illustration_resources/oldendorff.png')

##title

cIIHeader= '<p style="font-weight: 100; color:#042E43; font-size: 24px; margin-botttom: 0; ">CII Tool '+vessel_type+' Prototype </p>'
st.write(cIIHeader, unsafe_allow_html=True)

shipNameandIMO= '<span style="font-weight: 700; color:#146EA6; font-size: 36px;">'+ship_name+'</span> <span style="font-weight: 100; color:#146EA6; font-size: 36px;">IMO '+imo_num+'</span>'
st.write(shipNameandIMO, unsafe_allow_html=True)

st.write('2020 AER Plot as of '+date.today().strftime('%A %d %B %Y'))

##derive rating boundaries and colours/ratings of input
reference_lines = derive_boundaries(perc_decr, input_DWT, input_AER, vessel_type)

#plot figures
fig = plot_boundaries_and_K(reference_lines)
st.plotly_chart(fig, use_container_width = True)

##print data from reference lines
col1, col2, col3, col4, col5, col6 = st.columns([0.1,0.5,0.05,0.15,0.06, 0.09])
reference_lines = tidy_for_print(reference_lines)
idx = pd.IndexSlice
df = reference_lines[['E','D','Reference line','B','A','Percentage Decrease']].transpose()
slice_E = idx['E',:]
slice_D = idx['D',:]
slice_R = idx['Reference line',:]
slice_B = idx['B',:]
slice_A = idx['A',:]

st.dataframe(df.style.set_properties(**{'color': '#D81900'}, subset=slice_E).set_properties(**{'color': '#E59B2C'}, subset=slice_D).set_properties(**{'color': '#146EA6'}, subset=slice_R).set_properties(**{'color': '#6EAF04'}, subset=slice_B).set_properties(**{'color':  '#2C7B07'}, subset=slice_A))


##white space for locating logo at bottom of table
st.write('Powered by ')
st.image('illustration_resources/arcsilea.png', width=200)
