
# Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
# If x matches with an element, return the index.
# If x doesn’t match with any of elements, return -1.

# import numpy library
import numpy as np
class LinearSearch:

    def search(self, array, value):

        for i in range(0, len(array)):
            if array[i] == value:
                return i
        return -1





if __name__ == '__main__':

    array = np.arange(1, 500, 9)
    print(array)

    linear_search = LinearSearch()

    result = linear_search.search(array, 181)
    if result == -1:
        print("Value is not present in array")
    else:
        print(f"The value {array[result]} is founded in index {result}")



# The time complexity of above algorithm is O(n).
