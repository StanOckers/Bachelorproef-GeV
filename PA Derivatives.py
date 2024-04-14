import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def get_derivatives(x, y):
    derivatives = []
    for i in range(len(x)):
        if i == len(x)-1:
            derivatives.append(0.0)
        else:
            diffX = x[i] - x[i+1]
            diffY = y[i] - y[i+1]
            derivatives.append(diffY/diffX)
    return derivatives

def get_peaks(x, y):
    derivatives = get_derivatives(x, y)
    peaks = []
    for i in range(1, len(derivatives)-1):
        if derivatives[i-1] > 10000 and derivatives[i+1] < 10000:
            peaks.append(i)
    return peaks


def plot_graph_with_peaks(file_path):
    x = []
    y = []

    # Read data from the file
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                data = line.split()
                x.append(float(data[0]))
                y.append(float(data[1]))

    # Plot the original data
    plt.plot(x, y)
    
    plt.errorbar(x, get_derivatives(x, y), label='derivative')

    for i in get_peaks(x, y):
       plt.plot(x[i], y[i], "ro", label="peaks")


    # Set labels and title
    plt.xlabel('Wavelenght (nm)')
    plt.ylabel('Photoncount (cumulative)')
    plt.title('Derivatives')
    
    # Add grid and legend
    plt.grid(True)
    plt.legend()
    
    # Show plot
    plt.show()

# Example usage:
file_path = 'Data\S1 signal 8 lr-c caught peak.asc'  # Replace 'data.asc' with your file path

plot_graph_with_peaks(file_path)
