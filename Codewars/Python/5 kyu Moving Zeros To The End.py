def move_zeros(array):
    return [i for i in array if not((type(i) == int or type(i) == float)and i == 0)] + [int(i) for i in array if (type(i) == int or type(i) == float) and i == 0]