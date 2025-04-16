import streamlit as st
import matplotlib.pyplot as plt
plt.matplotlib.use('Agg')

from datetime import datetime

from dao.RecieveViaMQTTImpl import RecieveViaMQTTImpl

reciever = RecieveViaMQTTImpl()

lineChartData = reciever.recieveForLineChart()
subPlotData = reciever.recieveForSubPlot()

lineChart = st.empty()
subPlot = st.empty()

while True:
    lineChart.line_chart(lineChartData)

# subPlotData.pyplot(fig=subPlotData)
# plt.close(subPlotData)