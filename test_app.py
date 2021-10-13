import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from layout import _max_width_
_max_width_()


ref = pd.DataFrame(columns=['A','B','Reference line','D','E'])
yearly_decrease = {2021:2,2022:3,2023:5,2024:7,2025:9,2026:11,2027:14,2028:17,2029:20,2030:23}
bulk_ref_line = lambda DWT : 4745*(DWT**-0.622)
boundaries = {'A':0.86,'B':0.94,'D':1.06,'E':1.18}
colours = {'E':'red','D':'orange','Reference line':'black','B':'lightgreen','A':'darkgreen'}

col1, col2, col3 = st.columns([0.75,0.125,0.125])

vessel_type = col2.selectbox('Vessel Type',('Bulk Carrier',''))
input_AER = col2.number_input('Input AER', value=1.5)
input_DWT = col2.number_input('Input Deadweight', value=260000)

if input_DWT > 279000:
    input_DWT = 279000
ref['Reference line'] = [bulk_ref_line(input_DWT)*(1-perc/100) for perc in yearly_decrease.values()]
ref['A'] = ref['Reference line']*boundaries['A']
ref['B'] = ref['Reference line']*boundaries['B']
ref['D'] = ref['Reference line']*boundaries['D']
ref['E'] = ref['Reference line']*boundaries['E']
ref['input'] = np.repeat(input_AER,len(ref.index))
ref['year'] = yearly_decrease.keys()
ref['colour'] = None
ref['rating'] = None
ref.at[ref[ref.input < ref.A].index, 'colour'] = 'darkgreen'
ref.at[ref[(ref.input > ref.A)&(ref.input < ref.B)].index, 'colour'] = 'lightgreen'
ref.at[ref[(ref.input > ref.B)&(ref.input < ref.D)].index, 'colour'] = 'yellow'
ref.at[ref[(ref.input > ref.D)&(ref.input < ref.E)].index, 'colour'] = 'orange'
ref.at[ref[(ref.input > ref.E)].index, 'colour'] = 'red'
ref.at[ref[ref.input < ref.A].index, 'rating'] = 'A'
ref.at[ref[(ref.input > ref.A)&(ref.input < ref.B)].index,  'rating'] = 'B'
ref.at[ref[(ref.input > ref.B)&(ref.input < ref.D)].index,  'rating'] = 'C'
ref.at[ref[(ref.input > ref.D)&(ref.input < ref.E)].index,  'rating'] = 'D'
ref.at[ref[(ref.input > ref.E)].index,  'rating'] = 'E'
ref['bar'] = np.repeat(1,len(ref.index))
ref = ref.set_index('year')

fig = make_subplots(rows=2, cols=1, row_heights=[0.9,0.1], shared_xaxes=True)

fig.add_trace(go.Bar(x=ref.index,
                    y=ref.bar,
                    text=ref.rating,
                    textposition='auto',
                    marker_color=ref.colour,
                    showlegend=False),
                row=2,col=1)

for col in ['A','B','Reference line','D','E']:
    if col == 'Reference line':
        fig.add_trace(go.Scatter(x=ref.index,
                                y=ref[col],
                                line=dict(color=colours[col], dash='dash'),
                                name=col),
                    row=1,col=1)
    else:
        fig.add_trace(go.Scatter(x=ref.index,
                                y=ref[col],
                                line=dict(color=colours[col]),
                                name=col),
                    row=1,col=1)

fig.add_trace(go.Scatter(x=ref.index,
                        y=ref.input,
                        mode='markers',
                        marker_symbol='x',
                        marker_size=10,
                        marker=dict(color='purple'),
                        name='Input AER'),
            row=1,col=1)

fig['layout']['xaxis2']['title']=None
fig['layout']['xaxis']['title']='Year'
fig['layout']['yaxis2']['title']=None
fig['layout']['yaxis']['title']='AER'
fig['layout']['yaxis']['visible']=True
fig['layout']['xaxis']['showticklabels']=True
fig['layout']['yaxis2']['visible']=False
fig['layout']['xaxis2']['visible']=False

fig.update_layout(
	title_text = 'CII tool',
	showlegend = True,
	width=1100,
	height=500,
    hovermode="x unified"
	)

col1.plotly_chart(fig, use_container_width = True)


col11, col12 = st.columns([0.1,0.8])

col12.dataframe(ref[['A','B','Reference line','D','E']].transpose().style.format("{:.4}"))
