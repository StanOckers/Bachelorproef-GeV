import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks


def plot_graph_decay(file_path_1, file_path_2, file_path_3, file_path_4):
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []

    # Read data from the files
    with open(file_path_1, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                data = line.split()
                x.append(float(data[0]))
                y1.append(float(data[1]))

    with open(file_path_2, 'r') as file: 
        for line in file: 
            if line.strip(): 
                data = line.split()
                y2.append(float(data[1]))

    with open(file_path_3, 'r') as file: 
        for line in file: 
            if line.strip(): 
                data = line.split()
                y3.append(float(data[1]))

    with open(file_path_4, 'r') as file: 
        for line in file: 
            if line.strip(): 
                data = line.split()
                y4.append(float(data[1]))

    #Divide by 100 (to compare to single capture scale)                                             #Change for amount of steps in accumlative acquisiton
    for i in range(0, len(y1), 1):
        y1[i]= y1[i]/100
    
    for i in range(0, len(y2), 1):
        y2[i]= y2[i]/100
    
    for i in range(0, len(y3), 1):
        y3[i]= y3[i]/100
    
    for i in range(0, len(y4), 1):
        y4[i]= y4[i]/100

    # Plot the graph
    plt.figure()
    plt.plot(x, y1, color='black', alpha= 0.9, label='1mW')
    plt.plot(x, y2, color='black', alpha= 0.7, label='1mW')
    plt.plot(x, y3, color='black', alpha= 0.5, label='1mW')
    plt.plot(x, y4, color='black', alpha= 0.3, label='1mW')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Photoncounts (cumulative/100)')
    plt.title('cumulative/100')
    plt.grid(True)
    plt.legend()
    #plt.ylim(400, 3000)                                                                             #Set the y-axis limit for right plot                             
    
    return x, y1, y2, y3, y4


#measurements with same parameters b sorted by measurement time.
file_path_1 = 'Data\sample #8\S1 signal 8\S1 signal 8 first acq 100 steps 1mW.asc'
file_path_2 = 'Data\sample #8\S1 signal 8\S1 signal 8 second acq 100 steps 1mW.asc'
file_path_3 = 'Data\sample #8\S1 signal 8\S1 signal 8 third acq 100 steps 1mW.asc'
file_path_4 = 'Data\sample #8\S1 signal 8\S1 signal 8 fourth acq 100 steps 1mW.asc'


plot_graph_decay(file_path_1, file_path_2, file_path_3, file_path_4)
plt.show()



