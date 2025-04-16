import pandas as pd
from forStreamLit import points

import matplotlib.pyplot as plt
plt.matplotlib.use('Agg')

from dao.Charts import Charts


class ChartsImpl(Charts):
    def lineChart(self):
        chartData = pd.DataFrame({
                "Ultrasonic distance": points.getdistanceHisory(),
                "Pixel distance": points.getpixelDistanceHistory()
            })
        return chartData
    
    def subPlots(self):
        allXpoints = points.getAllXpoints()
        allYpoints = points.getAllYpoints()
        if allXpoints:
            fig, ax = plt.subplots()
            ax.set_xlim(0, points.getoriginalWidth())
            ax.set_ylim(0, points.getoriginalHeight())
            ax.scatter(allXpoints, allYpoints, color="red", s=100)
            return fig
        
        return None

        # test_x = [100, 200, 300, 400]
        # test_y = [100, 200, 150, 300]
        
        # fig, ax = plt.subplots(figsize=(6, 4))
        # ax.set_xlim(0, points.getoriginalWidth())
        # ax.set_ylim(0, points.getoriginalHeight())
        # ax.scatter(test_x, test_y, color="red", s=100)
        # ax.set_title("Test Plot")
        # ax.set_xlabel("X Position")
        # ax.set_ylabel("Y Position")
        # return fig