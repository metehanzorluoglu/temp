import os
import sys
import subprocess
import time

def way(lang : int):
    return

def find_max_index(ar):
    max_index = 0
    for i in range(1, len(ar)):
        if ar[i] < ar[max_index]:
            max_index = i
    return max_index

def restart_program():
    filename = sys.argv[0]
    os.system("reboot")
    
def find_mins(arr):
    min_index = find_max_index(arr)
    if min_index != 3: 
        max_value = min(arr[min_index-1], arr[min_index+1])
    else:
        max_value = min(arr[2], arr[0])

    equal_elements = [x for x in arr if x == arr[min_index]]
    min_value = min(equal_elements)
    min_indexes = [i+1 for i, x in enumerate(arr) if x == min_value]
    return min_index+1, max_value - arr[min_index], arr.index(max_value)+1, min_indexes

def direction_find(t):
    min_index, diff, max_index, min_array = find_mins(t)
    
    if len(min_array) == 2:
        if min_array[0] == 1 and min_array[1] == 4 and diff == 0:
            print(1)
            return 1
        elif min_array[0] == 4 and min_array[1] == 1 and diff == 0:
            print(1)
            return 1
        elif min_array[0] == 1 and min_array[1] == 2 and diff == 0:
            print(3)
            return 3
        elif min_array[0] == 2 and min_array[1] == 1 and diff == 0:
            print(3)
            return 3
        elif min_array[0] == 2 and min_array[1] == 3 and diff == 0:
            print(5)
            return 5
        elif min_array[0] == 3 and min_array[1] == 2 and diff == 0:
            print(5)
            return 5
        elif min_array[0] == 4 and min_array[1] == 3 and diff == 0:
            print(7)
            return 7
        elif min_array[0] == 3 and min_array[1] == 4 and diff == 0:
            print(7)
            return 7
                
    if min_index == 4 and max_index == 1 and diff <= 1:
        print(1)
        return 1
    elif min_index == 1 and max_index == 4 and diff <= 1:
        print(1)
        return 1
    elif min_index == 1 and max_index == 4 and diff > 1:
        print(2)
        return 2
    elif min_index == 1 and max_index == 2 and diff > 1:
        print(2)
        return 2
    elif min_index == 1 and max_index == 2 and diff <= 1:
        print(3)
        return 3
    elif min_index == 2 and max_index == 1 and diff <= 1:
        print(3)
        return 3
    elif min_index == 2 and max_index == 1 and diff > 1:
        print(4)
        return 4
    elif min_index == 2 and max_index == 3 and diff > 1:
        print(4)
        return 4
    elif min_index == 2 and max_index == 3 and diff <= 1:
        print(5)
        return 5
    elif min_index == 3 and max_index == 2 and diff <= 1:
        print(5)
        return 5
    elif min_index == 3 and max_index == 2 and diff > 1:
        print(6)
        return 6
    elif min_index == 3 and max_index == 4 and diff > 1:
        print(6)
        return 6
    elif min_index == 3 and max_index == 4 and diff <= 1:
        print(7)
        return 7
    elif min_index == 4 and max_index == 3 and diff <= 1:
        print(7)
        return 7
    elif min_index == 4 and max_index == 3 and diff > 1:
        print(8)
        return 8
    elif min_index == 4 and max_index == 1 and diff > 1:
        print(8)
        return 8
                
                
                
    
            
def test(mic, chunks):
    timer = 0
    for chunk in mic.read_chunks():
        timer = timer +1
        direction = mic.get_direction(chunk)
        if int(direction) == 30:
            print('Start...')
            break
        else:
            print('Wrong..')
        if timer % 10 == 7:
            time.sleep(2)
            restart_program()
    
    