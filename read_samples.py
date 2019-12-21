import numpy as np
from matplotlib import pyplot as plt
import plotovanje


#read one sample
def read_periodogram_sample(letter, sample_number, label):
    with open("periodogram/EMG_" + str(letter) + str(sample_number) + ".txt", 'r') as file:
        lines = file.readlines()
        X = []
        for line in lines:
            X.extend([float(val) for val in line.split(' ')[:-1]])

    return (X, label)

def read_periodogram_training():
    chars = ["A", "B", "C", "CH", "CJ", "D", "DJ", "DZ", "E", "F", "G", "H", "I", "J", "K", "L", "LJ", "M", "N",
             "NJ", "O", "P", "R", "S", "SH", "T", "U", "V", "Z", "ZJ"]
    X = []
    Y = []
    for j in range(1, 5):
        for i in range(0, 30):
            X_tmp, Y_tmp = read_periodogram_sample(chars[i], j, i)
            X.append(X_tmp)
            Y.append(Y_tmp)
            for k in range(0, 4):
                X_shift = np.random.uniform(-0.07, 0.07, 8208)
                X_tmp_tmp = X_tmp + X_shift
                X.append(X_tmp_tmp)
                Y.append(Y_tmp)

    return (X, Y)

def read_periodogram_test():
    chars = ["A", "B", "C", "CH", "CJ", "D", "DJ", "DZ", "E", "F", "G", "H", "I", "J", "K", "L", "LJ", "M", "N",
             "NJ", "O", "P", "R", "S", "SH", "T", "U", "V", "Z", "ZJ"]
    X = []
    Y = []
    for j in range(5, 6):
        for i in range(0, 30):
            X_tmp, Y_tmp = read_periodogram_sample(chars[i], j, i)
            X.append(X_tmp)
            Y.append(Y_tmp)


    return X, Y

def read_emg_training():
    chars = ["A", "B", "C", "CH", "CJ", "D", "DJ", "DZ", "E", "F", "G", "H", "I", "J", "K", "L", "LJ", "M", "N",
             "NJ", "O", "P", "R", "S", "SH", "T", "U", "V", "Z", "ZJ"]
    X = []
    Y = []
    for j in range(1, 5):
        for i in range(0, 30):
            emg_left = plotovanje.read_emg("dataset/EMG_" + chars[i] + str(j) + "_L.txt")
            emg_right = plotovanje.read_emg("dataset/EMG_" + chars[i] + str(j) + "_D.txt")
            for ch in range(0, 8):
                while (len(emg_left[ch]) < 750):
                    emg_left[ch].append(0)
                while (len(emg_right[ch]) < 750):
                    emg_right[ch].append(0)
            emg_left = np.reshape(emg_left, -1)
            emg_right = np.reshape(emg_right, -1)
            emg = np.append(emg_left, emg_right)
            X.append(emg_left)
            Y.append(i)



    return (X, Y)

def read_emg_test():
    chars = ["A", "B", "C", "CH", "CJ", "D", "DJ", "DZ", "E", "F", "G", "H", "I", "J", "K", "L", "LJ", "M", "N",
             "NJ", "O", "P", "R", "S", "SH", "T", "U", "V", "Z", "ZJ"]
    X = []
    Y = []
    for j in range(5, 6):
        for i in range(0, 30):
            emg_left = plotovanje.read_emg("dataset/EMG_" + chars[i] + str(j) + "_L.txt")
            emg_right = plotovanje.read_emg("dataset/EMG_" + chars[i] + str(j) + "_D.txt")
            for ch in range(0, 8):
                while(len(emg_left[ch]) < 750):
                    emg_left[ch].append(0)
                while(len(emg_right[ch]) < 750):
                    emg_right[ch].append(0)
            emg_left = np.reshape(emg_left, -1)
            emg_right = np.reshape(emg_right, -1)
            emg = np.append(emg_left, emg_right)
            X.append(emg_left)
            Y.append(i)



    return (X, Y)

def main():
    X, Y = read_periodogram_training()

if(__name__ == "__main__"):
    main()