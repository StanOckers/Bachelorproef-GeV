import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks


def plot_graph_overlay(file_path_1, file_path_2):
    x = []
    y = []
    z = []

    # Read data from the file
    with open(file_path_1, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                data = line.split()
                x.append(float(data[0]))
                y.append(float(data[1]))

    with open(file_path_2, 'r') as file: 
        for line in file: 
            if line.strip(): 
                data = line.split()
                z.append(float(data[1]))


    # Plot the graph
    plt.figure(1, figsize=[13, 5])
    plt.subplot(121)                                   #put plots next to eachother in same figure
    plt.plot(x, y, color='red', alpha= 1, label='1mW')
    plt.plot(x, z, color='green', alpha= 1, label='1mW')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Photoncounts')
    plt.title('single step')
    plt.grid(True)
    plt.legend()
    plt.ylim(400, 3000)                                     # Set the y-axis limit for left plot
   
    return x, y


def plot_graph_rescale(file_path_3, file_path_4):
    x = []
    y = []
    z = []

    # Read data from the file
    with open(file_path_3, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                data = line.split()
                x.append(float(data[0]))
                y.append(float(data[1]))

    with open(file_path_4, 'r') as file: 
        for line in file: 
            if line.strip(): 
                data = line.split()
                z.append(float(data[1]))

    for i in range(0, len(y), 1):
        y[i]= y[i]/100
    
    for i in range(0, len(z), 1):
        z[i]= z[i]/100

    # Plot the graph
    plt.figure(1)
    plt.subplot(122)                                    #put plots next to eachother in same figure
    plt.subplots_adjust(left=0.074, bottom=0.13, right=0.97, top=0.921, wspace= 0.262, hspace=None)
    plt.plot(x, y, color='black', label='1mW')
    plt.plot(x, z, color='blue', label='1mW')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Photoncounts (cumulative/100)')
    plt.title('cumulative/100')
    plt.grid(True)
    plt.legend()
    plt.ylim(400, 3000)                                     #Set the y-axis limit for right plot                             
    
    return x, y



#single step measurements
file_path_1 = 'Data\sample #8\S1 signal 9\\first 1 step 0,5mW.asc'
file_path_2 = 'Data\sample #8\S1 signal 9\\second 1 step 0,5mW.asc'

#cumulative measurements 1mw
file_path_3 = 'Data\sample #8\S1 signal 9\\third acq 100 steps 1mW.asc'

#cumulative measurements 0.5mw
file_path_4 = 'Data\sample #8\S1 signal 9\\fourth acq 100 steps 1mW.asc'


xdata, ydata =plot_graph_overlay(file_path_1, file_path_2)
xdata, ydata =plot_graph_rescale(file_path_3, file_path_4)
plt.show()



