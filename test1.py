import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def find_peaks_with_derivative(data, threshold=0):
    # Calculate the derivative of the data
    derivative = np.diff(data)

    # Find peaks in the derivative signal
    peaks, _ = find_peaks(derivative, height=threshold)
    print(np.diff(data))
    return peaks


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
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Photoncounts (cumulative)')
    plt.title('')

    
    # Plot standard deviation as error bars
    x_values = [np.diff(x[i:i+10]) for i in range(0, len(x), 10)]
    plt.errorbar(x_values, std_devs, fmt='none', yerr=std_devs, label='Standard Deviation')

    plt.grid(True)
    plt.legend()
    plt.show()
    return x, y

file_path = 'Data\S1 signal 9 ll-c peak measurement background spot.asc'  # Replace 'data.asc' with your file path
xdata, ydata =plot_graph_with_peaks_and_std_dev(file_path)
std_dev=calculate_std_dev(ydata)
calculate_mean_std_devs(std_dev)


