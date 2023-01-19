import numpy as np

def argmax(x):
    k = 0
    for i in range(1, len(x)):
        if x[i] > x[k]:
            k = i
    return k

def argmin(x):
    k = 0
    for i in range(1, len(x)):
        if x[i] < x[k]:
            k = i
    return k

def head(x, k):
    if len(x) < k:
        return x
    return x[:k]

def tail(x, k):
    if len(x) < k:
        return x
    return x[-k:]

def ols_estimate(x, y):
    n = x.size
    sumx = sumx2 = sumxy = sumy = sumy2 = 0
    ret = np.array([-1, -1])

    if x.size != y.size:
        return ret

    for i in range(n):
        sumx += x[i]
        sumx2 += x[i] ** 2
        sumxy += x[i] * y[i]
        sumy += y[i]
        sumy2 += y[i] ** 2

    denom = sumx2 - sumx ** 2 / n

    if denom == 0:
        return ret

    b = (sumxy - sumx * sumy / n) / denom
    a = sumy / n - b * sumx / n

    ret[0] = a
    ret[1] = b

    return ret


def ols_llk(x, y, k):
    n = x.size
    r = residsq = variance = ret = 0
    ols = ols2 = np.array([-1, -1])

    if x.size != y.size:
        return -1
    else:
        n = x.size

    if k == 0:
        ols = ols_estimate(x, y)
    else:
        x1 = x[:k]
        x2 = x[-k:]
        y1 = y[:k]
        y2 = y[-k:]
        ols = ols_estimate(x1, y1)
        ols2 = ols_estimate(x2, y2)

    if (ols[0] == -1 and ols[1] == -1) or (ols2[0] == -1 and ols2[1] == -1 and k != 0):
        return -1

    if k == 0:
        for i in range(n):
            r = y[i] - (ols[0] + ols[1] * x[i])
            residsq += r ** 2
    else:
        for i in range(n):
            if i < k:
                r = y[i] - (ols[0] + ols[1] * x[i])
            else:
                r = y[i] - (ols2[0] + ols2[1] * x[i])
            residsq += r ** 2

    variance = residsq / n
    if variance == 0:
        return -1

    ret = n / 2 * np.log(2 * np.pi) + n / 2 * np.log(variance) + n / 2

    return ret


def cpt_trend_AMOC(x, y, minseglen, penalty):
    n = x.size
    nn = 0
    stat = critical_stat = 0

    if x.size != y.size:
        return -1
    else:
        n = x.size

    if n < 2 * minseglen:
        return -1

    llc = np.zeros(n-2*(minseglen-1))

    for i in range(len(llc)):
        llc[i] = ols_llk(x, y, minseglen + i)
        if llc[i] == -1:
            return -1

    nn = np.argmin(llc)
    stat = ols_llk(x, y, 0) - llc[nn]
    critical_stat = (2 + (2*nn/n-1)**2)*np.log(n)*penalty

    if stat < critical_stat:
        nn = -1
    else:
        nn = nn + minseglen

    return nn


def cpt_trend_binary(x, y, cpts, Q, minseglen, penalty, k, last_pt):
    pt = pt1 = pt2 = 0
    if k[0] >= len(cpts):
        return cpts
    if Q < 2:
        pt = cpt_trend_AMOC(x, y, minseglen, penalty)
        if pt < 1:
            return cpts
        cpts[k[0]] = pt + last_pt
        k[0] += 1
        return cpts
    else:
        pt = cpt_trend_AMOC(x, y, minseglen, penalty)
        if pt < 1:
            return cpts
        cpts[k[0]] = pt + last_pt
        k[0] += 1
        cpts = cpt_trend_binary(x[:pt], y[:pt], cpts, Q-2, minseglen, penalty, k, last_pt)
        cpts = cpt_trend_binary(x[pt:], y[pt:], cpts, Q-2, minseglen, penalty, k, pt+last_pt)
    return cpts


def cpt_trend(x, y, Q, minseglen, penalty):
    n = int(2 * np.log2(Q + 1) - 1)
    if n % 2 != 0:
        n += 1
    k = [0]
    cpts = np.zeros(Q, dtype=int)
    return cpt_trend_binary(x, y, cpts, n, minseglen, penalty, k, 0)


"""
You're welcome! Yes, the cpt_trend_binary() function is called recursively, and it updates the values of the cpts array, which is then returned by the cpt_trend() function. It's always a good idea to test the functions with sample inputs to ensure they're working as expected.
If you have any issues, please don't hesitate to reach out.
"""