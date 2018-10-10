def exp(x, y, mod):
    ret = 1
    while (y):
        if (y & 1):
            ret = (ret * x) % mod
        y = int(y / 2)
        x = (x * x) % mod
    return ret
