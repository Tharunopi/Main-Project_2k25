import pandas as pd
from forStreamLit import points

import matplotlib.pyplot as plt
plt.matplotlib.use('Agg')

from dao.Charts import Charts
from forStreamLit import getXYpoints

class ChartsImpl(Charts):
    def lineChart(self):
        chartData = pd.DataFrame({
                "Ultrasonic distance": points.getdistanceHisory(),
                "Pixel distance": points.getpixelDistanceHistory()
            })
        return chartData
    
    def subPlots(self):
        allXpoints, allYpoints = getXYpoints()
        fig, ax = plt.subplots()
        ax.set_xlim(0, points.getoriginalWidth())
        ax.set_ylim(0, points.getoriginalHeight())
        ax.scatter(allXpoints, allYpoints, color="red", s=100)
        return fig

