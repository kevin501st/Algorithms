def find_min(numbers):

    return min(numbers), numbers.index(min(numbers))


def largest(array):
    final = []
    min_element = 10 ^ 60
    min_index = -1
    for i in range(len(array)):  # O(N)
        if len(final) < 3:
            final.append(array[i])
            if array[i] < min_element:
                min_element = array[i]
                min_index += 1
        else:
            if array[i] > min_element:
                final[min_index] = array[i]
                min_element, min_index = find_min(final)

    return final


print(largest([11, 5, 9, 10, 12]))
