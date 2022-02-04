#import numpy as np



def swap_sum(A, B):
    """
    A and B are list of sorted numbers
    t is the target to be found
    """
    # since the two arrays are sorted. we start with
    # initializing one pointer with the first index of any one array
    # and the other pointer with the last index of the other array
    A_i, B_i = 0, 0

    while A_i < len(A) and B_i < len(B):



        sum_a = sum(A) - A[A_i] + B[B_i]
        sum_b = sum(B) - B[B_i] + A[A_i]

        #print(sum_a)
        #print(sum_b)
        #print()
        #print(A_i)
        #print(B_i)

    # found target then return the values a and b
        if sum_a - sum_b == -10:
            return (A_i, B_i)
        elif sum(A) + 10 > sum(B):
    # current_sum was smaller! since we are incrementing the values in A
    # and decrementing the values in B
    # Increasing A_i will mean that the element in A that we get next will
    # increase our current sum, which is what is expected to find the target
            A_i += 1
        else:
    # current sum was larger!
    # Decreasing B_i will mean that the element in B that we get next will
    # decrease our current sum, which is what is expected to find the target
            B_i += 1
    return None

#print(swap_sum(np.array([1,4,8, 20, 50]), np.array([0, 50,60,70])))




