
# Optical spectrum
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import csv
#1


path = r'C:\Users\Stan\Documents\GitHub\BachelorProef\Data'
fig = plt.figure(figsize = [16, 6], dpi = 300)

with open(path +  "Data\sample #9\dark spot 2.asc", 'r') as fp:
        reader = csv.reader(fp, delimiter = '\t')
        data_read = [row for row in reader]
        x = []
        y = []

        for i in range(1, len(data_read)):
            x.append(float(data_read[i][0]))
            y.append(float(data_read[i][1]))
            x = np.array(x)
            y = np.array(y)
            plt.plot(x, y)

peaks, _ = find_peaks(y, height = 17000, width = 10)# = 16000)#width = 10)
plt.plot(x[peaks], y[peaks], "x")

plt.xlabel('Wavelength, nm', fontsize = 20)
plt.ylabel('PL, counts', fontsize = 20)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)

#2

path = r'C:\Users\Stan\Documents\GitHub\BachelorProef\Data'
fig = plt.figure(figsize = [16, 6], dpi = 300)

with open(path +  "Data\sample #9\dark spot bg.asc", 'r') as fp:
    reader = csv.reader(fp, delimiter = '\t')
    data_read = [row for row in reader]
x = []
y = []
for i in range(1, len(data_read)):
    x.append(float(data_read[i][0]))
    y.append(float(data_read[i][1]))
x = np.array(x)
y = np.array(y)
plt.plot(x, y)

peaks, _ = find_peaks(y, height = 25000, width = 5)# = 16000)#width = 10)
plt.plot(x[peaks], y[peaks], "x")

plt.xlabel('Wavelength, nm', fontsize = 20)
plt.ylabel('PL, counts', fontsize = 20)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)