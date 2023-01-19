import numpy as np

def subset(x, i, j):
    y = x[i:j+1]
    return y

def findminima(xmin, xmax, threshold):
    """
    the function takes in three parameters - xmin, xmax and threshold. The xmin and xmax are the vectors containing the minimum and maximum values respectively. The threshold is a vector containing the threshold values.
    The function initializes some variables such as n, imin, k and y. n is the number of elements in the xmin vector. imin is the index of the minimum element
    """
    n = len(xmin)
    imin = 0
    k = 0
    y = np.zeros((n,2),dtype=int)

    for i in range(n):

        if xmin[i] < xmin[imin]:
            imin = i
        if xmax[i]/xmin[imin] > threshold[i]:
            if max(xmax[y[k][0]:imin+1])/xmin[imin] > threshold[i]:
                y[k][0] = imin
                y[k+1][0] = imin
                y[k][1] = -1
                k = k+1
            imin = i+1
    return(y)

def findmaxima(xmin, xmax, threshold):
    """
    This function takes in three parameters - xmin, xmax and threshold. The xmin and xmax are the vectors containing the minimum and maximum values respectively. The threshold is a vector containing the threshold values.
    The function initializes some variables such as n, imax, k and y. n is the number of elements in the xmin vector. imax is the index of the maximum element in the xmax vector. k is a counter variable and y is an integer matrix of size (n,2).
    The function then iterates through the elements of xmin and xmax and compares the elements to find the maxima and store the indices in the y matrix. The function also compares the elements with the threshold values and updates the maxima indices in the y matrix accordingly. It then returns the y matrix containing the indices of maxima.
    """
    n = len(xmin)
    imax = 0
    k = 0
    y = np.zeros((n,2),dtype=int)

    for i in range(n):

        if xmax[i] > xmax[imax]:
            imax = i
        if xmax[imax]/xmin[i] > threshold[i]:
            if xmax[imax]/min(xmin[y[k][0]:imax+1]) > threshold[i]:
                y[k][0] = imax
                y[k+1][0] = imax
                y[k][1] = 1
                k = k+1
            imax = i+1
    return(y)

def sortoptimaposition(pos, sign, value):
    """
    The function takes in 3 parameters: pos, sign, and value. pos and sign are integer vectors, and value is a numeric vector.
    The function starts by initializing a variable n which is the size of the pos vector. Then it iterates through the elements of pos and sign and compares the current element with the previous element. If the elements are the same, it compares the corresponding element of value and updates the sign vector accordingly. The function then returns the updated sign vector.
    """

    n = len(pos)
    for i in range(1,n):
        if pos[i] == pos[i-1]:
            if sign[i]==1:
                if value[i]>value[i-1]:
                    sign[i-1] = 0
                else:
                    sign[i] = 0
            else:
                if value[i]<value[i-1]:
                    sign[i-1] = 0
                else:
                    sign[i] = 0
    return sign
def sortoptimasign(pos, sign, value):
    """
    The function takes in 3 parameters: pos, sign, and value. pos and sign are integer vectors, and value is a numeric vector.
    The function starts by initializing a variable n which is the size of the pos vector. Then it iterates through the elements of sign and compares the current element with the previous element. If the elements are the same, it compares the corresponding element of value and updates the sign vector accordingly. The function then returns the updated sign vector.
    """
    n = len(pos)
    for i in range(1,n):
        if sign[i] == sign[i-1]:
            if sign[i]==1:
                if value[i]>value[i-1]:
                    sign[i-1] = 0
                else:
                    sign[i] = 0
            else:
                if value[i]<value[i-1]:
                    sign[i-1] = 0
                else:
                    sign[i] = 0
    return sign

def checkoptimasign(sign):
    n = len(sign)
    ret = True
    for i in range(1,n):
        if sign[i]==sign[i-1]:
            ret = False
            break
    return ret

def checkoptimapos(pos):
    n = len(pos)
    ret = True
    for i in range(1,n):
        if pos[i]==pos[i-1]:
            ret = False
            break
    return ret
