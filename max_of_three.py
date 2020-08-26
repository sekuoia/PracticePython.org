def max_of_three(a,b,c):
    if a > b:
        if a > c:
            return a
    elif b > a:
        if b > c:
            return b
    return c

print(max_of_three(7,20000,0.15))