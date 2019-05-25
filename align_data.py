"""
@author: EmaPajic
File for aligning the data from 2 armbands
"""
import plotovanje
""" function for getting hour, minute, second and microsecond from timestamp in dat"""
def get_timestamp(data_line):
    temp = data_line.find(']')
    temp += 2
    temp1 = temp + 1
    while data_line[temp1] != ':':
        temp1 += 1
    hours = data_line[temp:(temp1)]
    temp = temp1 + 1
    temp1 = temp + 1
    while data_line[temp1] != ':':
        temp1 += 1
    minutes = data_line[temp:(temp1)]
    temp = temp1 + 1
    temp1 = temp + 1
    while data_line[temp1] != '.':
        temp1 += 1
    seconds = data_line[temp:(temp1)]
    temp = temp1 + 1
    microseconds = data_line[temp:-1]
    
    return (hours, minutes, seconds, microseconds)

def time_to_microseconds(t):
    h, min, sec, micros = t
    micros_sum = int(h) * (3.6e+9) + int(min) * (6e+7) + int(sec) * (1e+6) + int(micros)
    return micros_sum

""" returnes absolute difference between two times"""
def time_difference(time1, time2):
    micros_sum1 = time_to_microseconds(time1)
    micros_sum2 = time_to_microseconds(time2)
    
    micros_diff = abs(micros_sum1 - micros_sum2)
    
    h_diff = int(micros_diff / (3.6e+9))
    micros_diff -= h_diff * (3.6e+9)
    min_diff = int(micros_diff / (6e+7))
    micros_diff -= min_diff * (6e+7)
    sec_diff = int(micros_diff / (1e+6))
    micros_diff -= sec_diff * (1e+6)
    micros_diff = int(micros_diff)
    
    return (str(h_diff), str(min_diff), str(sec_diff), str(micros_diff))

"""" compares two times that consist of hour, minute, second and microsecond
    information and returns true if time1 is later than time2, false otherwise"""
def compare_times(time1, time2):
    
    h1,min1,sec1,micros1 = time1
    h2,min2,sec2,micros2 = time2
    
    if int(h1) > int(h2):
        return True
    elif int(h1) < int(h2):
        return False
    else:
        if int(min1) > int(min2):
            return True
        elif int(min1) < int(min2):
            return False
        else:
            if int(sec1) > int(sec2):
                return True
            elif int(sec1) < int(sec2):
                return False
            else:
                if int(micros1) > int(micros2):
                    return True
                else:
                    return False
                
""" deletes data before given time"""
def delete_data_before(myo_data, time_limit):
    while compare_times(time_limit, get_timestamp(myo_data[0])):
        myo_data.pop(0)


""" deletes data after given time"""
def delete_data_after(myo_data, time_limit):
    while compare_times(get_timestamp(myo_data[-1]), time_limit):
        myo_data.pop()


""" deletes additonal data if it doesn't have pair"""
def pair_data(left_myo_data, right_myo_data):
    if len(left_myo_data) == len(right_myo_data):
        return
    
    diff_first_elements = time_difference(get_timestamp(left_myo_data[0]), get_timestamp(right_myo_data[0]))
    diff_last_elements = time_difference(get_timestamp(left_myo_data[-1]), get_timestamp(right_myo_data[-1]))
    
    if compare_times(diff_first_elements, diff_last_elements):
        if compare_times(get_timestamp(left_myo_data[0]), get_timestamp(right_myo_data[0])):
            right_myo_data.pop(0)
        else:
            left_myo_data.pop(0)
    else:
        if compare_times(get_timestamp(left_myo_data[-1]), get_timestamp(right_myo_data[-1])):
            left_myo_data.pop()
        else:
            right_myo_data.pop()

def align_data(left_myo_data, right_myo_data):
    first_left = left_myo_data[0]
    first_right = right_myo_data[0]
    last_left = left_myo_data[-1]
    last_right = right_myo_data[-1]
    
    """find hour, minute, second and microsec of first measurment from left myo"""
    fl_timestamp = get_timestamp(first_left)
    
    """find hour, minute, second, and microsec of first measurment from right myo"""
    fr_timestamp = get_timestamp(first_right)
    
    """find hour, minute, second and microsec of last measurment from left myo"""
    ll_timestamp = get_timestamp(last_left)
    
    """find hour, minute, second and microsec of last measurment from right myo"""
    lr_timestamp = get_timestamp(last_right)
    
    if compare_times(fl_timestamp, fr_timestamp):
        delete_data_before(right_myo_data, fl_timestamp)
    else:
        delete_data_before(left_myo_data, fr_timestamp)
    
    if compare_times(ll_timestamp, lr_timestamp):
        delete_data_after(left_myo_data, lr_timestamp)
    else:
        delete_data_after(right_myo_data, ll_timestamp)
        
    pair_data(left_myo_data, right_myo_data)
    
    return left_myo_data, right_myo_data
        
def create_aligned_txt(file_name_left, file_name_right):
    with open(file_name_left, 'r') as file:
        left_myo_data = file.readlines()
    with open(file_name_right, 'r') as file:
        right_myo_data = file.readlines()
        
    left_myo_data, right_myo_data = align_data(left_myo_data, right_myo_data)
    
    with open(file_name_left, 'w') as file:
        file.writelines(left_myo_data)
    with open(file_name_right, 'w') as file:
        file.writelines(right_myo_data)
        
def create_aligned_dataset():
    chars = ["A", "B", "C", "CH", "CJ", "D", "DJ", "DZ", "E", "F", "G", "H", "I", "J", "K", "L", "LJ", "M", "N", "NJ", "O", "P", "R", "S", "SH", "T", "U", "V", "Z", "ZJ"]
    for i in range(0,30):
        for j in range(1, 6):
            name_base = "EMG_" + chars[i] + str(j)
            create_aligned_txt(name_base + "_L.txt", name_base + "_D.txt")


    
if __name__ == "__main__":
    create_aligned_dataset()