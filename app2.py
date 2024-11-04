import pandas as pd
import streamlit as st
import plotly.express as px
vehicles_df = pd.read_csv('vehicles_us.csv')

st.header('Share of Odometer Readings')
#First Plot
fig1 = px.histogram(vehicles_df, x='odometer')
fig1.update_layout(width=800, height=400, margin=dict(l=50, r=50, t=50, b=50))
event1 = st.plotly_chart(fig1, key="odometer", on_select="rerun")


avg_price_per_year = vehicles_df.groupby('model_year')['price'].mean()
avg_price_per_year = avg_price_per_year.reset_index()
avg_price_per_year['model_year'] = avg_price_per_year['model_year'].astype(str)


#2nd Plot
fig2 = px.scatter(avg_price_per_year, x='model_year', y='price', title='AVG Price per Model Year')
event2 = st.plotly_chart(fig2, key="AVG Price", on_select="rerun")



toggle = st.toggle("Toggle Between Graphs")
if toggle:
    st.write(event2)