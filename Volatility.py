import numpy as np
import pandas as pd

def average_volatility(asset1_data, asset2_data):
    # Calculate daily returns for each asset
    asset1_returns = asset1_data['Close'].pct_change()
    asset2_returns = asset2_data['Close'].pct_change()

    # Calculate the standard deviation of the daily returns for each asset
    asset1_volatility = asset1_returns.std() * np.sqrt(252)
    asset2_volatility = asset2_returns.std() * np.sqrt(252)

    # Calculate the average volatility between the two assets
    average_volatility = (asset1_volatility + asset2_volatility) / 2
    return average_volatility

# Example usage
asset1_data = pd.read_csv('asset1.csv')
asset2_data = pd.read_csv('asset2.csv')
average_vol = average_volatility(asset1_data, asset2_data)
print(average_vol)