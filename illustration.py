import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import streamlit as st

def plot_K_tool(fig, reference_lines):
    fig.add_trace(go.Bar(x=reference_lines.index,
                        y=reference_lines.bar,
                        text=reference_lines.rating,
                        textposition='auto',
                        marker_color=reference_lines.colour,
                        showlegend=False),
                    row=2,col=1)
    return fig

def plot_boundary_graph(fig, reference_lines):
    ##rating boundary colours
    colours = {'E':'red','D':'orange','Reference line':'black','B':'lightgreen','A':'darkgreen'}

    lines = reference_lines.append(  pd.Series({'A':reference_lines.A[2021],
                            'B':reference_lines.B[2021],
                            'Reference line':reference_lines['Reference line'][2021],
                            'D':reference_lines.D[2021],
                            'E':reference_lines.E[2021],
                            },name = 2020.5) )

    lines = lines.append( pd.Series({'A':reference_lines.A[2030],
                            'B':reference_lines.B[2030],
                            'Reference line':reference_lines['Reference line'][2030],
                            'D':reference_lines.D[2030],
                            'E':reference_lines.E[2030],
                            },name = 2030.5) )

    lines = lines.sort_index()
#green
    fig.add_trace(go.Scatter(x=lines.index,
                                y=np.repeat(np.round(min(reference_lines['A'])-0.05,1),len(lines)),
                                mode='lines',
                                line=dict(color='#43961B', width=0.05),
                                showlegend=False),
                    row=1,col=1)
#Fill & Line Styling for A
    fig.add_trace(go.Scatter(x=lines.index,
                            y=lines['A'],
                            mode='lines',
                            fill='tonexty', fillcolor='rgba(53, 146, 10, 0.5)',
                            line=dict(
                                color='#2C7B07', dash='solid', width= 2 ),
                            name='A'),
                row=1,col=1)

#Fill & Line Styling for B
    fig.add_trace(go.Scatter(x=lines.index,
                            y=lines['B'],
                            mode='lines',
                            fill='tonexty',fillcolor='rgba(125, 178, 13, 0.5)',
                            line=dict(
                                color='#6EAF04', dash='solid', width= 2 ),
                            name='B'),
                row=1,col=1)
    '''
    fig.add_trace(go.Scatter(x=reference_lines.index,
                            y=reference_lines['Reference line'],
                            line=dict(color='orange'),
                            fill='tonexty',
                            showlegend=False),
                row=1,col=1)
    '''
#Fill & Line Styling for D
    fig.add_trace(go.Scatter(x=lines.index,
                            y=lines['D'],
                            mode='lines',
                            fill='tonexty',fillcolor='rgba(207, 209, 83, 0.5)',
                            line=dict(
                                color='#E59B2C', dash='solid', width= 2 ),
                            name='C'),
                row=1,col=1)
#Fill & Line Styling for E
    fig.add_trace(go.Scatter(x=lines.index,
                            y=lines['E'],
                            mode='lines',
                            fill='tonexty',fillcolor='rgba(253, 194, 123, 0.5)',
                            line=dict(
                                color='#D81900', dash='solid', width= 2 ),
                            name='D'),
                row=1,col=1)
#Fill & Line Styling for E
    fig.add_trace(go.Scatter(x=lines.index,
                                y=np.repeat(np.round(max(reference_lines['E'])+0.05,1),len(lines)),
                                mode='lines',
                                fill='tonexty',fillcolor='rgba(253, 140, 124, 0.5)',
                                line=dict(
                                color='#D81900', dash='solid', width= 0.05 ),
                                name='E'),
                    row=1,col=1)
#black
    fig.add_trace(go.Scatter(x=lines.index,
                            y=lines['Reference line'],
                            mode='lines',
                            line=dict(color='#146EA6', dash='dot'),
                            name='Reference line'),
                row=1,col=1)
#Marker style for A
    fig.add_trace(go.Scatter(x=reference_lines.index,
                            y=reference_lines['A'],
                            mode='markers',
                            marker=dict(
                                color='#ffffff',
                                line = dict(
                                    color= '#2C7B07',
                                    width= 2
                                ),
                            ),
                            showlegend=False),
                row=1,col=1)
#Marker style for B
    fig.add_trace(go.Scatter(x=reference_lines.index,
                            y=reference_lines['B'],
                            mode='markers',
                            marker=dict(
                                color='#ffffff',
                                line = dict(
                                    color= '#6EAF04',
                                    width= 2
                                ),
                            ),
                            showlegend=False),
                row=1,col=1)

#Marker style for Reference
    fig.add_trace(go.Scatter(x=reference_lines.index,
                            y=reference_lines['Reference line'],
                            mode='markers',
                            marker=dict(
                                color='#ffffff',
                                line = dict(
                                    color= '#146EA6',
                                    width= 2
                                ),
                            ),
                            showlegend=False),
                row=1,col=1)
#Marker style for D
    fig.add_trace(go.Scatter(x=reference_lines.index,
                            y=reference_lines['D'],
                            mode='markers',
                            marker=dict(
                                color='#ffffff',
                                line = dict(
                                    color= '#E59B2C',
                                    width= 2
                                ),
                            ),
                            showlegend=False),
                row=1,col=1)
#Marker style for E
    fig.add_trace(go.Scatter(x=reference_lines.index,
                            y=reference_lines['E'],
                            mode='markers',
                            marker=dict(
                                color='#ffffff',
                                line = dict(
                                    color= '#D81900',
                                    width= 2
                                ),
                            ),
                            showlegend=False),
                row=1,col=1)


    return fig

def plot_user_input(fig, reference_lines):
    fig.add_trace(go.Scatter(x=reference_lines.index,
                            y=reference_lines.input,
                            mode='markers',
                            marker_symbol='triangle-up',
                            marker_size=12,
                            marker=dict(
                                color='#82C1E8',
                                line = dict(
                                    color= '#146EA6',
                                    width= 2
                                )
                            ),
                            name='AER'),
                row=1,col=1)
    return fig

def plot_layout(fig):
    fig['layout']['xaxis2']['title']=None
    fig['layout']['xaxis']['title']='Year'
    fig['layout']['yaxis2']['title']=None
    fig['layout']['yaxis']['title']='AER'
    fig['layout']['yaxis']['visible']=True
    fig['layout']['xaxis']['showticklabels']=True
    fig['layout']['yaxis2']['visible']=False
    fig['layout']['xaxis2']['visible']=False

    fig.update_layout(
    	showlegend = True,
    	width=1000,
    	height=400,
        hovermode=False,
        margin=dict(l=10, r=10, t=10, b=10)
    	)
    return fig

def plot_boundaries_and_K(reference_lines):
    fig = make_subplots(rows=2, cols=1, row_heights=[0.9,0.1], shared_xaxes=True)
    fig = plot_K_tool(fig, reference_lines)
    fig = plot_boundary_graph(fig, reference_lines)
    fig = plot_user_input(fig, reference_lines)
    fig = plot_layout(fig)
    return fig
