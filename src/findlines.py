
import numpy as np
import math
import statistics
import pandas as pd

def variance(x):
    n = len(x)
    total = 0
    var = 0
    for i in range(n):
        total += x[i]
    avg = total / n
    for i in range(n):
        total += (x[i] - avg) ** 2
    var = total / n
    return var

def localmaxima(mat, minmat, maxmat, nrow, ncol, s):
    """
    This function checks for local maxima in a matrix. It takes in three matrices (mat, minmat and maxmat), the number of rows and columns of the matrix, and a threshold value (s). It then checks the four corners of the matrix and any elements in between to see if they are greater than their surrounding elements and also greater than the threshold value. If they are, they are added to the lines matrix and the function returns the lines matrix containing all the local maxima.
    """
    k = 0
    lines = np.zeros((nrow * ncol, 5), dtype=int)
    # check top left
    if mat[0][0] > mat[1][0] and mat[0][0] > mat[0][1] and mat[0][0] > mat[1][1] and mat[0][0] > s:
        lines[k][0] = 0
        lines[k][1] = 0
        lines[k][2] = mat[0][0]
        lines[k][3] = minmat[0][0]
        lines[k][4] = maxmat[0][0]
        k += 1
    # check bottom left
    if mat[nrow - 1][0] > mat[nrow - 2][0] and mat[nrow - 1][0] > mat[nrow - 1][1] and mat[nrow - 1][0] > mat[nrow - 2][1] and mat[nrow - 1][0] > s:
        lines[k][0] = nrow - 1
        lines[k][1] = 0
        lines[k][2] = mat[nrow - 1][0]
        lines[k][3] = minmat[nrow - 1][0]
        lines[k][4] = maxmat[nrow - 1][0]
        k += 1
    # check bottom right
    if mat[nrow - 1][ncol - 1] > mat[nrow - 1][ncol - 2] and mat[nrow - 1][ncol - 1] > mat[nrow - 2][ncol - 1] and mat[nrow - 1][ncol - 1] > mat[nrow - 2][ncol - 2] and mat[nrow - 1][ncol - 1] > s:
        lines[k][0] = nrow - 1
        lines[k][1] = ncol - 1
        lines[k][2] = mat[nrow - 1][ncol - 1]
        lines[k][3] = minmat[nrow - 1][ncol - 1]
        lines[k][4] = maxmat[nrow - 1][ncol - 1]
        k += 1
    # check top left
    if mat[0][ncol - 1] > mat[0][ncol - 2] and mat[0][ncol - 1] > mat[1][ncol - 1] and mat[0][ncol - 1] > mat[1][ncol - 2] and mat[0][ncol - 1] > s:
        lines[k][0] = 0
        lines[k][1] = ncol - 1
        lines[k][2] = mat[0][ncol - 1]
        lines[k][3] = minmat[0][ncol - 1]
        lines[k][4] = maxmat[0][ncol - 1]
        k += 1

    for i in range(1, nrow-1):
        for j in range(1, ncol-1):
            if mat[i][j] > mat[i-1][j] and mat[i][j] > mat[i+1][j] and mat[i][j] > mat[i][j-1] and mat[i][j] > mat[i][j+1] and mat[i][j] > s:
                lines[k][0] = i
                lines[k][1] = j
                lines[k][2] = mat[i][j]
                lines[k][3] = minmat[i][j]
                lines[k][4] = maxmat[i][j]
                k += 1
    return lines[:k]



def envelopescore(lines, n1, x, y, rbucket, abucket, flag, flag2):
    """
    The envelopescore() function is used to calculate a score for each line in the set of lines returned by the localmaxima() function. The score is used to indicate the quality of the fit of each line to the set of points.

    The function takes in several parameters:

    lines is a matrix containing information about the lines being evaluated, such as the indices of the range and angle bins they correspond to.
    n1 is the number of lines in the lines matrix.
    x and y are the x and y coordinates of the points in the image, respectively.
    rbucket and abucket are the range and angle bins, respectively, used to determine the number of possible lines to vote on.
    flag is an integer used to indicate which type of line detection was performed.
    flag2 is a boolean flag to indicate whether to use all points or only the points that voted for each line.
    The function starts by initializing some variables such as n2, start, end, limit, count, dist, r, theta, rquanta, mse, and score. n2 is the number of points in the image, while start, end, limit, and count are used to iterate through the lines and points. dist, r, theta, rquanta, and mse are used to calculate the distance between each point and its corresponding line, while score is an array used to store the scores of each line.

    The function then iterates through the lines, and for each line, it retrieves the start and end indices of the points that voted for it from the lines matrix. If flag2 is set to True, it also retrieves the limit of the points to use, which is the number of points in the image.

    For each point in the range [start, limit], the function calculates the distance between the point and the line. If flag is equal to -1, it adds the square of the distance to the mean squared error (mse) if the distance is less than rquanta, otherwise, if flag is equal to 1, it adds the square of the distance to the mean squared error (mse) if the distance is greater than rquanta.

    After all the points have been processed, the function calculates the score of the line by dividing the mse
    """

    n2, start, end, limit, count = 0, 0, 0, 0, 0
    dist, r, theta, rquanta, mse = 0.0, 0.0, 0.0, 0.0, 0.0
    score = [0] * n1
    pi = math.pi
    n2 = len(x)
    rquanta = rbucket[2] - rbucket[1]

    for i in range(n1):
        start = lines[i][3]
        end = lines[i][4]
        limit = end + 1
        if flag2:
            limit = n2
        for j in range(start, limit):
            if j >= n2:
                break
            r = rbucket[lines[i][0]]
            theta = abucket[lines[i][1]]
            dist = y[j] - (r/math.sin(theta*pi/180) - x[j]/math.tan(theta*pi/180))
            if flag == -1:
                if dist + rquanta < 0:
                    mse = mse + dist*dist
                    count += 1
            if flag == 1:
                if dist - rquanta > 0:
                    mse = mse + dist*dist
                    count += 1
        if count != 0:
            score[i] = mse/count
        mse = 0
        count = 0

    return score



def fitscore(lines, n1, x, y, rbucket, abucket, flag):
    n2, start, end, length = 0, 0, 0, 0
    dist, r, theta, mse = 0.0, 0.0, 0.0, 0.0
    score = [0] * n1
    pi = math.pi
    n2 = len(x)

    for i in range(n1):
        start = lines[i][3]
        end = lines[i][4]
        length = end - start + 1
        for j in range(start, end + 1):
            if j >= n2:
                break
            r = rbucket[lines[i][0]]
            theta = abucket[lines[i][1]]
            dist = y[j] - (r/math.sin(theta*pi/180) - x[j]/math.tan(theta*pi/180))
            mse = mse + dist*dist
        score[i] = 1 - (mse/length)/statistics.variance(y)
        mse = 0

    return score


def houghtransform(x1, y1, flag, rbucket, abucket, s):
    """
    The function houghtransform() is an implementation of the Hough transform, a technique used to detect lines in an image. It takes in a set of (x,y) coordinates, representing the points in the image where edges were detected, and uses these points to vote on possible lines that could have generated them.

    The function takes in several parameters:

    x1 and y1 are the x and y coordinates of the points in the image, respectively.
    flag is an integer used to indicate which type of line detection to perform.
    rbucket and abucket are the range and angle bins, respectively, which determine the number of possible lines to vote on.
    s is a threshold used to determine which lines are significant enough to be considered real lines.
    The function starts by initializing some variables and matrices, such as accumulator, accumulatorMin, and accumulatorMax, which are used to store the number of votes for each possible line.

    It then iterates through the input points and uses their coordinates to vote on the possible lines that could have generated them. This voting process is done by incrementing the value of the corresponding bin in the accumulator matrix. It also stores the indices of the first and last point that voted for each bin in the accumulatorMin and accumulatorMax matrices, respectively.

    After the voting process, the function calls the localmaxima() function which is used to find local maxima in the accumulator matrix and return the indices of the lines that were voted on the most.

    It then calls the envelopescore() and fitscore() functions on the returned lines and calculate the scores of the lines.

    Finally, the function returns a dataframe containing the r, theta, strength, start, end, score and fit of the lines.    
    """
    n, nA, nR, k, r, r_step = len(x1), len(abucket), len(rbucket), 0, 0.0, 0.0
    pi = math.pi
    accumulator = [[0 for _ in range(nA)] for _ in range(nR)]
    accumulatorMin = [[0 for _ in range(nA)] for _ in range(nR)]
    accumulatorMax = [[-1 for _ in range(nA)] for _ in range(nR)]
    lines = [[0 for _ in range(5)] for _ in range(nR*nA)]
    scores = [0.0 for _ in range(nR*nA)]
    fit = [0.0 for _ in range(nR*nA)]

    r_step = (rbucket[nR-1]-rbucket[0])/(nR-1)

    for i in range(n):
        for j in range(nA):
            r = x1[i]*math.cos(abucket[j]*pi/180) + y1[i]*math.sin(abucket[j]*pi/180)
            if r<rbucket[0] or r > rbucket[nR-1]:
                continue
            k = round((r-rbucket[0])/r_step)
            accumulator[k][j] += 1
            if accumulatorMin[k][j]==0:
                accumulatorMin[k][j] = i
            if accumulatorMax[k][j]<i:
                accumulatorMax[k][j] = i
    lines = localmaxima(accumulator,accumulatorMin, accumulatorMax,nR,nA,s)
    scores = envelopescore(lines,nR*nA,x1,y1,rbucket,abucket,flag, True)
    fit = fitscore(lines,nR*nA,x1,y1,rbucket,abucket,flag)

    return pd.DataFrame({
        "r": [lines[i][0] for i in range(nR*nA)],
        "theta": [lines[i][1] for i in range(nR*nA)],
        "strength": [lines[i][2] for i in range(nR*nA)],
        "start": [lines[i][3] for i in range(nR*nA)],
        "end": [lines[i][4] for i in range(nR*nA)],
        "score": scores,
        "fit": fit
    })
