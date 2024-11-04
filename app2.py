import pandas as pd
import streamlit as st
import plotly.express as px
vehicles_df = pd.read_csv('vehicles_us.csv')

st.header('Share of Odometer Readings')

fig = px.histogram(vehicles_df, x='odometer')
fig = fig.update_layout(width=800, height=400, margin=dict(l=50, r=50, t=50, b=50))

event = st.plotly_chart(fig, key="odometer", on_select="rerun")


avg_price_per_year = vehicles_df.groupby('model_year')['price'].mean()
avg_price_per_year = avg_price_per_year.reset_index()
avg_price_per_year['model_year'] = avg_price_per_year['model_year'].astype(str)



fig = px.scatter(avg_price_per_year, x='model_year', y='price', title='AVG Price per Model Year')

event2 = st.plotly_chart(fig, key="AVG Price", on_select="rerun")


toggle = st.checkbox("Toggle Between Graphs")


if toggle:
      event
else:
      event2
   