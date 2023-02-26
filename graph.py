import streamlit as st
import plotly.express as px
import pandas as pd
from main import temp_file

df = pd.read_csv(temp_file)

temp_graph = px.line(x=df["date"],
                     y=df["temperature"],
                     labels={"x": "Date/Time",
                             "y": "Average Global Temperature"})
st.title("Global Average Temperatures By Date")
st.plotly_chart(temp_graph)
