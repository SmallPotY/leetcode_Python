def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        bonacci = [0,1]
        for i in range(2,n):
            bonacci.append(bonacci[i-1] + bonacci[i-2])
        return bonacci[n-1]


print(fibonacci(10))

