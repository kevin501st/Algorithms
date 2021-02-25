def move_element_to_end(array, toMove):
    swap_index = len(array) - 1
    while array[swap_index] == toMove and swap_index >= 0:
        swap_index -= 1

    i = 0
    while i <= swap_index:
        if array[i] == toMove:
            array[i], array[swap_index] = array[swap_index], array[i]
        while array[swap_index] == toMove:
            swap_index -= 1
        i += 1

    return array


array = [2, 2, 1, 2, 2, 3, 3, 5]
toMove = 1
print(move_element_to_end(array, toMove))
