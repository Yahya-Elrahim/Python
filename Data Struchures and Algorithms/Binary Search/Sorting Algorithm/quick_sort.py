# Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given
# array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.
#
# Always pick first element as pivot. Always pick last element as pivot (implemented below) Pick a random element as
# pivot. Pick median as pivot. The key process in quickSort is partition(). Target of partitions is, given an array
# and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (
# smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear
# time.

def partition(array, low, high):
    pivot = array[high]  # pivot
    i = low

    for j in range(low, high):

        #  If current element is smaller than the pivot
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]

            i += 1  # increment index of smaller element
    array[i], array[high] = array[high], array[i]

    return i  # index of current pivot

def quickSort(array, low, high):

    if low < high:

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
    return array


if __name__ == '__main__':

    array = [4, 8, 12, 6, 7, 10, 2, 5]
    print(quickSort(array, 0, len(array) - 1))

