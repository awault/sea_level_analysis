import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.scatter(data['Year'],data['CSIRO Adjusted Sea Level'],s=20)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Create first line of best fit
    m_, b_ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])[:2]
    x_val = range(1880, 2051)
    y_val = m_ * x_val + b_
    plt.plot(x_val,y_val,color='red',label='Line of Best Fit (1880-2050)')

    # Create second line of best fit
    new_data = data[data['Year'] >= 2000]
    m_new, b_new = linregress(new_data['Year'], new_data['CSIRO Adjusted Sea Level'])[:2]
    x_new = range(2000, 2051)
    y_new = m_new * x_new + b_new
    plt.plot(x_new, y_new, color='green',linestyle='--',label='Line of Best Fit (2000 onwards)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()