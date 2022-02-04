import random

def knn_distance(arr, q, k):


    euc_dist = quickselect(arr, k, 0, len(arr), q)

    return (abs(euc_dist), euc_dist + q )




def quickselect(arr, k , start, stop, q):

    pivot_ix = random.randrange(start, stop)
    pivot_ix = in_place_partition(arr, start, stop, pivot_ix, q)
    pivot_order = pivot_ix + 1
    if pivot_order == k:
        return arr[pivot_ix] - q
    elif pivot_order < k:
        return quickselect(arr, k, pivot_ix + 1, stop, q)
    else:
        return quickselect(arr, k, start, pivot_ix, q)


def in_place_partition(arr, start, stop, pivot_ix, q):
    def swap(ix_1, ix_2):
        arr[ix_1], arr[ix_2] = arr[ix_2], arr[ix_1]

    pivot = arr[pivot_ix]
    swap(pivot_ix, stop - 1)
    middle_barrier = start
    for end_barrier in range(start, stop - 1):
        if abs(arr[end_barrier] - q) < abs(pivot - q):
            swap(middle_barrier, end_barrier)
            middle_barrier += 1

    swap(middle_barrier, stop - 1)
    return middle_barrier


knn_distance([3, 10, 52, 15], 19, 1)
