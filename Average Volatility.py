import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_return_distribution(asset_data):
    # Calculate daily returns
    returns = asset_data['Close'].pct_change()
    # Plot the distribution of returns
    plt.hist(returns, bins=50, density=True)
    plt.xlabel('Returns')
    plt.ylabel('Frequency')
    plt.title('Distribution of Returns')
    plt.show()

# Example usage
asset_data = pd.read_csv('asset_data.csv')
plot_return_distribution(asset_data)