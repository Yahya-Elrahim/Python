# python program for implementation of selection sort algorithm

# Function selection sort algoritim

# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
# from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
#
# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.
#
# In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray
# is picked and moved to the sorted subarray.
#
# Following example explains the above steps:

# Time Complexity: O(n2) as there are two nested loops.
# 
# Auxiliary Space: O(1)
# The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.

def selectionSort(array):


    for i in range(0, len(array)):

        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array





if __name__ == '__main__':
     array = [5, 10, 9, 4, 8, 3, 2, 12]
     print(selectionSort(array))
