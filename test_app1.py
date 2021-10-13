import streamlit as st
from journey_comp import read_journey_files, graph_BE_routes
from layout import _max_width_
_max_width_()

df = read_journey_files()
fig = graph_BE_routes(df)

st.plotly_chart(fig, use_container_width = True)
