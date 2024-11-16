#!/usr/bin/env python3

import seaborn as sns
sns.set_style("dark")
import matplotlib.pyplot as plt
from datetime import datetime

from chainlink_utils import get_assets, get_price_ts


def plot_price_time_series(t_start, ts_prices, name=''):

    # Extract timestamps and prices from the data.
    timestamps = [datetime.fromtimestamp(i+t_start) for i in range(len(ts_prices))]

    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, ts_prices, marker='o', label='Price')

    # Add labels, title, and legend.
    plt.xlabel('Timestamp')
    plt.ylabel('Price')
    plt.title('Price Time Series'+(' ' + name if name else ''))
    plt.legend()
    plt.grid(True)

    # Format x-axis for better readability.
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot.
    plt.show()


def main():
    for asset in get_assets():
        t_start, ts_prices = get_price_ts(asset)
        plot_price_time_series(t_start, ts_prices, asset.capitalize())


if __name__ == '__main__':
    main()
