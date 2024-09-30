def exist(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return True
    return False