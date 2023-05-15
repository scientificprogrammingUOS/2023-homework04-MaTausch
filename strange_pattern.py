import numpy as np

# implement the function strange pattern

def strange_pattern(tupel):
    # delete the NotImplementedError when you write your function.
    hight = tupel[0]
    print(hight)
    width = tupel[1]
    bool_array = np.zeros((hight, width), dtype = bool)
    bool_array[0::3, 0::3] = 1
    bool_array[2::3, 1::3] = 1
    bool_array[1::3, 2::3] = 1
    return bool_array
    #raise NotImplementedError


if __name__ == "__main__":
    print(strange_pattern((6,8)))
