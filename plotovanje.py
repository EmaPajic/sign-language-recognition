import numpy as np
from matplotlib import pyplot as plt

NUM_OF_EMG_CHANNELS = 8


def read_emg(file_name):

    emg = [[],[],[],[],[],[],[],[]]
    with open(file_name, 'r') as file:
        data = file.readlines()
    for line in data:

        pos = 1
        for i in range(0, NUM_OF_EMG_CHANNELS):

            s = ""
            while(line[pos] != ',' and line[pos] != ']'):
                s += line[pos]
                pos += 1

            pos += 2
            emg[i].append(float(s))

    return emg

def plot_emg(emg, figure_number):

    plt.figure(figure_number)
    for i in range(0, NUM_OF_EMG_CHANNELS):
        plt.subplot(4, 2, i + 1)
        plt.plot(emg[i])
    plt.show()


