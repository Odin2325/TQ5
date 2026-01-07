def perf_test(number):
    div_list = []
    div_sum = 0
    if number <= 1:
        return False
    for i in range (1, number):
        if number % i == 0:
            div_list.append(i)
            div_sum += i
    if div_sum == number:
        return True
    return False

for i in range(0, 501):
    if perf_test(i):
        print(f'{i} ist eine perfekte Zahl')
