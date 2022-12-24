def swap_case(s):
    array = [char for char in s]
    size = len(array)
    
    for index in range(size):
        if array[index].isupper():
            array[index] = array[index].lower()
        elif array[index].islower():
            array[index] = array[index].upper()
    
    return ''.join(array)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
