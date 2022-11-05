#  Question 1
#  Developer Strange in the Multidimension of Madness

import numpy as np


def transpose_axes(arr, axes):
    a = np.array(arr)
    b = np.transpose(a, axes)
    return (b)


# 1st Test Case
a = [[1, 2], [3, 4]]
print(transpose_axes(a, [1, 0]))


# 2nd test Case
a = [[1, 2], [3, 4]]
print(transpose_axes(a, [0, 1]))


# 3rd test case
a = [[[1, 2, 3], [3, 4, 5]], [[1, 2, 3], [3, 4, 5]]]
print(transpose_axes(a, [2, 0, 1]))
