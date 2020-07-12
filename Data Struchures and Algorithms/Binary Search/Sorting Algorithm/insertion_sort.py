# python program for implementation of insertion sort algorithm

# Function to do insertion sort algorithm

# Time Complexity: O(n*2)
# 
# Auxiliary Space: O(1)
# 
# Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes 
# minimum time (Order of n) when elements are already sorted. 
# 
# Algorithmic Paradigm: Incremental Approach
# 
# Sorting In Place: Yes
# 
# Stable: Yes
# 
# Online: Yes
# 
# Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost 
# sorted, only few elements are misplaced in complete big array. 

def insertionSort(array):

    for i in range(1, len(array)):

        key = array[i]

        j = i-1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            array[j] = key
            j -= 1
    return array




if __name__ == '__main__':
     array = [5, 10, 9, 4, 8, 3, 2, 12]
     print(insertionSort(array))
