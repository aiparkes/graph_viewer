import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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
    for col in ['A','B','Reference line','D','E']:
        if col == 'Reference line':
            fig.add_trace(go.Scatter(x=reference_lines.index,
                                    y=reference_lines[col],
                                    line=dict(color=colours[col], dash='dash'),
                                    name=col),
                        row=1,col=1)
        else:
            fig.add_trace(go.Scatter(x=reference_lines.index,
                                    y=reference_lines[col],
                                    line=dict(color=colours[col]),
                                    name=col),
                        row=1,col=1)
    return fig

def plot_user_input(fig, reference_lines):
    fig.add_trace(go.Scatter(x=reference_lines.index,
                            y=reference_lines.input,
                            mode='markers',
                            marker_symbol='x',
                            marker_size=10,
                            marker=dict(color='purple'),
                            name='Input AER'),
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
    	width=1100,
    	height=400,
        hovermode="x unified",
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
