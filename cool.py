import math
def reverse(lst, start, stop):
    """(Supposedly) reverses the list lst[start:stop] in-place."""
    if stop - start <= 1:
        return

    if stop - start == 2:
        lst[stop-1], lst[start] = lst[start], lst[stop-1]

    middle = math.floor((start + stop) / 2)

    reverse(lst, start, middle)
    reverse(lst, middle, stop)




def product(numbers, start, stop):
    """Should return the product of all elements
    in numbers[start:stop]"""
    if stop - start == 0:
        return 0
    elif stop - start == 1:
        return numbers[start]
    else:
        return numbers[start] * product(numbers, start+1, stop)

cool = [1,1,1,4]
print(cool)
print(product(cool, 0,4))
print(cool)


def binary_search(arr, start, stop, target):
    print("iter")
    if stop <= start:
        return None

    middle = math.floor((start + stop) / 2)


    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return binary_search(arr, middle + 1, stop, target)
    else:
        return binary_search(arr, start, middle, target)

binary_search([-10, 0, 20, 40, 50, 100],0, 6, 30)