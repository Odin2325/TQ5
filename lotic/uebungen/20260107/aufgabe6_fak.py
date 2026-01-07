def faculty(n):
    if n == 0:
        return 1
    fac = 1
    for i in range (1, n+1):
        fac *= i
    return fac

print(faculty(52))


