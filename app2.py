import pandas as pd
import streamlit as st
import plotly.express as px
vehicles_df = pd.read_csv('vehicles_us.csv')

st.header('Share of Odometer Readings')

df = px.vehicles_df()
fig = px.histogram(df, x='odometer')
fig = fig.update_layout(width=800, height=400, margin=dict(l=50, r=50, t=50, b=50))

event = st.plotly_chart(fig, key="odometer", on_select="rerun")

event


fig = px.scatter(df, x='model_year', y='price', title='AVG Price per Model Year')

event2 = st.plotly_chart(fig, key="AVG Price", on_select="rerun")

event2

toggle = st.checkbox("Toggle Between Graphs")


if toggle('Show histogram'):
      st.plotly_chart(event)
else:
     st.plotly_chart(event2)
   