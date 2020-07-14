# Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself
# for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The
# merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted
# sub-arrays into one. See following C implementation for details.


def mergeSort(array):

    if len(array) > 1:

        mid = len(array) // 2  # Finding the middle of array
        left_array = array[:mid]  # divide the array elements tow halves
        right_array = array[mid:]

        mergeSort(left_array)
        mergeSort(right_array)


        i = j = k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        while len(left_array) > i:
            array[k] = left_array[i]
            i += 1
            k +=1
        while len(right_array) > j:
            array[k] = right_array[j]
            j += 1
            k += 1


if __name__ == '__main__':
    array = [12, 11, 13, 5, 6, 7]

    print(array)

    mergeSort(array)

    print(array)
