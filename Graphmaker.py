import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks


def plot_graph_overlay(file_path_1, file_path_2, file_path_9, file_path_10):
    x = []
    y = []
    z = []
    y1 = []
    y2 = []

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

    with open(file_path_9, 'r') as file: 
        for line in file: 
            if line.strip(): 
                data = line.split()
                y1.append(float(data[1]))

    #with open(file_path_10, 'r') as file: 
        for line in file: 
            if line.strip(): 
                data = line.split()
                y2.append(float(data[1]))


    #for i in range(0, len(y), 1):
    #    y[i]= y[i]/50
    #for i in range(0, len(z), 1):
    #    z[i]= z[i]/50
    for i in range(0, len(y1), 1):
        y1[i]= y1[i]/40
    #for i in range(0, len(y2), 1):
    #    y2[i]= y2[i]/50

   

    #only on sample 9 measurements (offset of about 20 nm)
    #for i in range(0, len(x), 1):
    #    x[i]= x[i] - 2.2

    # Plot the graph
    plt.figure(1, figsize=[13, 5])
    #plt.subplot(121)                                        #put plots next to eachother in same figure
    plt.plot(x, y, color='red', alpha= 1, label='1 step')
    plt.plot(x, z, color='green', alpha= 1, label='1 step')
    plt.plot(x, y1, color='blue', alpha= 1, label='50 step')
    #plt.plot(x, y2, color='orange', alpha= 1, label='50 step')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Photoncounts')
    plt.title('Ge on Si')
    plt.figtext(0.15, 0.7, "1 mW laser power")
    plt.grid(True)
    plt.legend()
    #plt.ylim(400, 2000)                                     # Set the y-axis limit for left plot
   
    return x, y,


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
    plt.ylim(400, 2000)                                     #Set the y-axis limit for right plot                             
    
    return x, y1,



#single step measurements
file_path_1 = 'Data\sample #10\Bright spot\signal 4 1 step.asc'
file_path_2 = 'Data\sample #10\Bright spot\signal 4 1 step unstable peak caught at 623.asc'
file_path_9 = 'Data\sample #10\Bright spot\signal 4 50 steps second acq 1mW.asc'
file_path_10 = 'Data\\7\sample 9\signal 2 50 steps 4 0,5mW.asc'

#cumulative measurements of 50 steps

file_path_3 = 'Data\\7\sample 9\signal 2 50 steps 1 1,0mW.asc'
file_path_4 = 'Data\\7\sample 9\signal 2 50 steps 2 1,0mW.asc'
file_path_5 = 'Data\\7\sample 9\signal 2 50 steps 3 1,0mW.asc'
file_path_6 = 'Data\\7\sample 9\signal 2 50 steps 4 1,0mW.asc'
file_path_7 = 'Data\\7\sample 9\signal 2 50 steps 1 1,0mW.asc'

#cumulative measurements of 400 steps / 8
#file_path_8 = 'Data\sample #9\Bright spot\signal 4 400 steps after 10 minutes of stopwatch 1,1mW.asc'


xdata, ydata =plot_graph_overlay(file_path_1, file_path_2, file_path_9, file_path_10)
#xdata, ydata =plot_graph_rescale(file_path_3, file_path_4, file_path_5, file_path_6, file_path_7, file_path_8)
plt.show()





