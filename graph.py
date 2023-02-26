import streamlit as st
import plotly.express as px
from main import temp_file


def read(data_file):
    with open(data_file, "r") as file:
        return file.readlines()


temp_data = read(temp_file)[1:]
times = []
temps = []

for item in temp_data:
    data = item.split(',')
    times.append(data[0])
    temps.append(data[1])

temp_graph = px.line(x=times, y=temps, labels={"x": "Date/Time",
                                               "y": "Average Global Temperature"})
st.title("Global Average Temperatures By Date")
st.plotly_chart(temp_graph)
