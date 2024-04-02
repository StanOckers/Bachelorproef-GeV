import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def calculate_std_dev(y_values):
    std_devs = []
    for i in range(0, len(y_values), 10):
        std_dev = np.std(y_values[i:i+10])
        std_devs.append(std_dev)
    return std_devs

def plot_graph_with_peaks_and_std_dev(file_path):
    x = []
    y = []

    # Read data from the file
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                data = line.split()
                x.append(float(data[0]))
                y.append(float(data[1]))

    # Plot the graph
    plt.plot(x, y)
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Graph Title')

    # Calculate standard deviation of Y values for every 10 X values
    std_devs = calculate_std_dev(y)

    # Find peaks with prominence based on standard deviation
    prominence_multipliers = np.array(std_devs)  # Use std_devs as prominence multipliers

    # Ensure the length of prominence_multipliers matches the length of y
    while len(prominence_multipliers) < len(y):
        prominence_multipliers.append(prominence_multipliers[-1])

    peaks, _ = find_peaks(y, prominence=prominence_multipliers)

    # Mark peaks on the graph
    plt.plot([x[i] for i in peaks], [y[i] for i in peaks], "ro", label="peaks")

    # Plot standard deviation as error bars
    x_values = [np.mean(x[i*10:(i+1)*10]) for i in range(len(std_devs))]  # Adjusted calculation of x_values
    plt.errorbar(x_values, std_devs, fmt='none', yerr=std_devs, label='Standard Deviation')

    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage:
file_path = 'S3.asc'  # Replace 'data.asc' with your file path
plot_graph_with_peaks_and_std_dev(file_path)
