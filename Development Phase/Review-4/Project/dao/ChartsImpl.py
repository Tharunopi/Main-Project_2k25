from dao.Charts import Charts

import matplotlib.pyplot as plt
plt.matplotlib.use('Agg')

from entity.StorePoints import StorePoints

import pandas as pd

points = StorePoints()

class ChartsImpl(Charts):
    def lineChart(self, pixelDistanceHistory, distanceHistory):
        chart_data = pd.DataFrame({
                    "Ultrasonic distance": distanceHistory,
                    "Pixel distance": pixelDistanceHistory
                })
        
    def subPlots(self, allXpoints, allYpoints):
        if allXpoints and allYpoints:
            # fig, ax = plt.subplots()
            # ax.set_xlim(0, points.getoriginalWidth())
            # ax.set_ylim(0, points.getoriginalHeight)
            # ax.scatter(points.getAllXpoints(), points.getAllYpoints, color="red", s=100)
            # pyplot(fig)
            # plt.close(fig)
            pass