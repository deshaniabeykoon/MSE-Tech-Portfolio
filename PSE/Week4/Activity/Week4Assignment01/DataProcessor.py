# Fetch the data for data analysis using See link:L https://data.niwa.co.nz/pages/clidb-on-datahub
import pandas as pd
import matplotlib.pyplot as plt

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def load_annual_rainfall_data(self,raindata):
        # Data Cleaning
        raindata['YEAR'] = raindata['YEAR'].astype(int)
        raindata['STATS_VALUE'] = raindata['STATS_VALUE'].astype(float)

        # Descriptive Statistics
        monthly_stats = raindata.groupby('PERIOD')['STATS_VALUE'].agg(['mean', 'median', 'std'])

        # Monthly Trends Visualization
        raindata.groupby(['YEAR', 'PERIOD']).mean().unstack().plot(kind='line')
        plt.title('Monthly Average Statistics Over Years')
        plt.ylabel('Stats Value')
        plt.show()

        # Yearly Trends Visualization
        yearly_stats = raindata.groupby('YEAR')['STATS_VALUE'].mean()
        yearly_stats.plot(kind='bar')
        plt.title('Average Statistics Per Year')
        plt.ylabel('Average Stats Value')
        plt.show()