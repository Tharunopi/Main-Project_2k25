import streamlit as st
import matplotlib.pyplot as plt
plt.matplotlib.use('Agg')
import time
import pandas as pd

from dao.RecieveViaMQTTImpl import RecieveViaMQTTImpl

st.title("MQTT Chart Viewer")

debug = st.empty()
lineChart = st.empty()
subPlot = st.empty()

reciever = RecieveViaMQTTImpl()
reciever.connect()

while True:
    lineChartData = reciever.recieveForLineChart()
    subPlotData = reciever.recieveForSubPlot()

    # Debug information
    debug.text(f"Line data type: {type(lineChartData)}, Subplot data type: {type(subPlotData)}")

    if lineChartData is not None:
        try:
            # If it's a DataFrame, use line_chart
            if isinstance(lineChartData, pd.DataFrame):
                lineChart.line_chart(lineChartData)
            # If it's raw data, convert to DataFrame first
            else:
                debug.text(f"Converting line data of type {type(lineChartData)} to DataFrame")
        except Exception as e:
            debug.text(f"Error displaying line chart: {e}")
    
    if subPlotData is not None:
        try:
            # Make sure we're passing a figure object to pyplot
            if isinstance(subPlotData, plt.Figure):
                subPlot.pyplot(subPlotData)
                plt.close(subPlotData)
            else:
                debug.text(f"Subplot data is not a matplotlib Figure: {type(subPlotData)}")
        except Exception as e:
            debug.text(f"Error displaying subplot: {e}")
    
    time.sleep(1)