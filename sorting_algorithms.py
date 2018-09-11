'''
Implement sorting algorithms.
'''


def selection_sort(L):
    '''
    Sort `L` array in ascending order.
    '''
    sorted_array = []
    for _ in range(len(L)):
        # Use element at position 0 as a starting point
        smallest_element = L[0]
        smallest_index = 0
        for i in range(len(L)):
            if smallest_element > L[i]:
                smallest_element = L[i]
                smallest_index = i
        # Add element to sorted_array and delete it from the input array L
        sorted_array.append(L.pop(smallest_index))
    return sorted_array
