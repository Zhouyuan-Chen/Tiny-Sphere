# This is a sample Python script.
import igl
import meshplot
import scipy as sp
import numpy as np
from meshplot import plot, subplot, interact

def print_hi(name):
    V = np.array([
        [0., 0, 0],
        [1, 0, 0],
        [1, 1, 1],
        [2, 1, 0]
    ])

    F = np.array([
        [0, 1, 2],
        [1, 3, 2]
    ])
    meshplot.offline()
    plot(V, F)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
