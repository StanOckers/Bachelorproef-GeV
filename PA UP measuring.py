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

def get_y_in_data(file_path, x_to_find):
    x = []
    y = []

    # Read data from the file
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                data = line.split()
                x.append(float(data[0]))
                y.append(float(data[1]))

    i = 0
    while x[i] < x_to_find and i < len(x):
        i += 1
    
    x0 =  x[i - 1]
    x1 = x[i]
    t = (x_to_find - x0) / (x1 - x0)
    
    y0 =  y[i - 1]
    y1 = y[i]
    return y0 * (1-t) + y1 * t
    

def plot_graph_with_peaks_and_std_dev(file_path, file_path_no_peak):
    x = []
    y = []

    # Read data from the file
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                data = line.split()
                x.append(float(data[0]))
                y.append(float(data[1]))

    x_no_peak = []
    y_no_peak = []
    with open(file_path_no_peak, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                data = line.split()
                x_no_peak.append(float(data[0]))
                y_no_peak.append(float(data[1]))


    # Plot the graph
    plt.plot(x_no_peak, y_no_peak, color="gray")
    plt.plot(x, y)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Photoncounts')
    plt.title('Unstable peak height')

    # Calculate standard deviation of Y values for every 10 X values
    std_devs = calculate_std_dev(y)
    std_devs_no_peak = calculate_std_dev(y_no_peak)

    # Calculate prominence based on standard deviations
    prominence = calculate_prominence(std_devs)

    # Find peaks with prominence
    peaks, _ = find_peaks(y, prominence=prominence)

    


    # Mark peaks on the graph
    mean_std_dev = calculate_mean_std_devs(std_devs)
    for i in peaks:
        if y[i] > get_y_in_data(file_path_no_peak, x[i]) + 200:
            plt.plot(x[i], y[i], "ro", label="peaks")
            plt.text(x[i], y[i],  str(y[i] - get_y_in_data(file_path_no_peak, x[i])))
            plt.plot([x[i], x[i]], [y[i], get_y_in_data(file_path_no_peak, x[i])], linestyle = 'dotted')

    # Plot standard deviation as error bars
    x_values = [np.mean(x[i:i+10]) for i in range(0, len(x), 10)]
    plt.errorbar(x_values, std_devs, fmt='none', yerr=std_devs, label='Standard Deviation', elinewidth=2)
    plt.errorbar(x_values, std_devs_no_peak, fmt='none', yerr=std_devs_no_peak, label='Standard Deviation', elinewidth=2,color='gray')

    plt.grid(True)
    
    plt.show()
    return x, y

file_path = 'Data\sample #10\Bright spot\signal 4 1 step unstable peak caught at 623.asc'  # Replace 'data.asc' with your file path
file_path_no_peak = 'Data\sample #10\Bright spot\signal 4 1 step.asc'

xdata, ydata =plot_graph_with_peaks_and_std_dev(file_path, file_path_no_peak)
std_dev=calculate_std_dev(ydata)
calculate_mean_std_devs(std_dev)