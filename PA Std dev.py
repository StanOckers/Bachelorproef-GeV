import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def calculate_std_dev(y_values):
    std_devs = []
    for i in range(0, len(y_values), 10):
        std_devs.append(np.std(y_values[i:i+10]))
    print(std_devs)
    return std_devs

def calculate_prominence(std_devs):
    # Calculate the median of the standard deviations
    median_std_dev = np.median(std_devs)
    # Set the prominence as a factor of the median standard deviation
    prominence = median_std_dev * 5  # Adjust the factor as needed
    return prominence

def calculate_mean_std_devs(std_devs):
    mean_std_dev = np.mean(std_devs)
    print(mean_std_dev)
    return mean_std_dev


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


    for i in range(0, len(y), 1):
        if i < i+5:     
            if i > -5:
                plt.plot(x[i], y[i], "ro", label="test peaks")



    # Plot the graph
    plt.plot(x, y)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Photoncounts (cumulative)')
    plt.title('Standard Deviations')

    # Calculate standard deviation of Y values for every 10 X values
    std_devs = calculate_std_dev(y)

    # Calculate prominence based on standard deviations
    prominence = calculate_prominence(std_devs)

    # Find peaks with prominence
    peaks, _ = find_peaks(y, prominence=prominence)

    


    # Mark peaks on the graph
    mean_std_dev = calculate_mean_std_devs(std_devs)
    for i in peaks:
        if std_devs[int(i/10)] > mean_std_dev:
            plt.plot(x[i], y[i], "ro", label="peaks")

    # Plot standard deviation as error bars
    x_values = [np.mean(x[i:i+10]) for i in range(0, len(x), 10)]
    plt.errorbar(x_values, std_devs, fmt='none', yerr=std_devs, label='Standard Deviation')

    plt.grid(True)
    
    plt.show()
    return x, y

file_path = 'Data\sample #8\S1 signal 9\\first 1 step 0,5mW.asc'  # Replace 'data.asc' with your file path

xdata, ydata =plot_graph_with_peaks_and_std_dev(file_path)
std_dev=calculate_std_dev(ydata)
calculate_mean_std_devs(std_dev)


