# Binary Search : In computer science, a binary search or half-interval search algorithm finds the position of a
# target value within a sorted array. The binary search algorithm can be classified as a dichotomies
# divide-and-conquer search algorithm and executes in logarithmic time.


# import numpy library
import numpy as np
class BinarySearch:

    def __init__(self, array, key, first, last):
        self.array = array
        self.key = key
        self.first = first
        self.last = last

    def binary_search(self):

        while self.last >= self.first:

            mid = (self.first + self.last) // 2

            # If element is present at the middle itself
            if array[mid] == self.key:
                return f"{array[mid]} number is founded at index {mid}"

            # If element is smaller than mid, then it
            # can only be present in left subarray

            elif array[mid] > self.key:
                self.last = mid - 1

            # Else the element can only be present
            # in right subarray
            else:
                self.first = mid + 1

        # Element is not present in the array
        else:
            return "Not founded"




if __name__ == '__main__':

    array = np.arange(1, 200, 5)
    print(array)

    binary_search = BinarySearch(array, 111, 0, len(array) - 1)
    result = binary_search.binary_search()
    print(result)
    
# The time complexity of above algorithm is O(logn).
