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
    plt.subplot(121)                                        #put plots next to eachother in same figure
    plt.plot(x, y, color='red', alpha= 1, label='1mW')
    plt.plot(x, z, color='green', alpha= 1, label='1mW')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Photoncounts')
    plt.title('Sample #7')
    plt.grid(True)
    plt.legend()
    #plt.ylim(400, 3000)                                     # Set the y-axis limit for left plot
   
    return x, y


#def plot_graph_rescale(file_path_3, file_path_4, file_path_5, file_path_6, file_path_7, file_path_8):
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []

    # Read data from the file
    with open(file_path_3, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                data = line.split()
                x.append(float(data[0]))
                y1.append(float(data[1]))

    with open(file_path_4, 'r') as file: 
        for line in file: 
            if line.strip(): 
                data = line.split()
                y2.append(float(data[1]))

    with open(file_path_5, 'r') as file: 
        for line in file: 
            if line.strip(): 
                data = line.split()
                y3.append(float(data[1]))

    with open(file_path_6, 'r') as file: 
        for line in file: 
            if line.strip(): 
                data = line.split()
                y4.append(float(data[1]))

    with open(file_path_7, 'r') as file: 
        for line in file: 
            if line.strip(): 
                data = line.split()
                y5.append(float(data[1]))

    with open(file_path_8, 'r') as file: 
        for line in file: 
            if line.strip(): 
                data = line.split()
                y6.append(float(data[1]))

    for i in range(0, len(y4), 1):
        y6[i]= y6[i]/8

    # Plot the graph
    plt.figure(1)
    plt.subplot(122)                                    #put plots next to eachother in same figure
    plt.subplots_adjust(left=0.074, bottom=0.13, right=0.97, top=0.921, wspace= 0.262, hspace=None)
    plt.plot(x, y1, color='pink', label='1mW')
    plt.plot(x, y2, color='blue', label='1mW')
    plt.plot(x, y3, color='green', label='1mW')
    plt.plot(x, y4, color='red', label='1mW')
    plt.plot(x, y5, color='yellow', label='1mW')
    plt.plot(x, y6, color='black', label='1mW')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Photoncounts (cumulative/100)')
    plt.title('cumulative/100')
    plt.grid(True)
    plt.legend()
    #plt.ylim(400, 3000)                                     #Set the y-axis limit for right plot                             
    
    return x, y1,



#single step measurements
file_path_1 = 'Data\\4\sample 7\S1 signal 1 lr-c.asc'
file_path_2 = 'Data\\4\sample 7\S1 signal 2 top middle.asc'

#cumulative measurements of 50 steps

#file_path_3 = 'Data\sample #9\Bright spot\signal 4 50 steps second acq 1,1mW.asc'
#file_path_4 = 'Data\sample #9\Bright spot\signal 4 50 steps third acq 1,1mW.asc'
#file_path_5 = 'Data\sample #9\Bright spot\signal 4 50 steps fourth acq 1,1mW.asc'
#file_path_6 = 'Data\sample #9\Bright spot\signal 4 50 steps fifth acq 1,1mW.asc'
#file_path_7 = 'Data\sample #9\Bright spot\signal 4 50 steps sixth acq 1,1mW.asc'

#cumulative measurements of 400 steps / 8
#file_path_8 = 'Data\sample #9\Bright spot\signal 4 400 steps after 10 minutes of stopwatch 1,1mW.asc'


xdata, ydata =plot_graph_overlay(file_path_1, file_path_2)
#xdata, ydata =plot_graph_rescale(file_path_3, file_path_4, file_path_5, file_path_6, file_path_7, file_path_8)
plt.show()



