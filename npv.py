initial_cost = 9000.0
feet = 0.15
lata = [3400.0, 2200.0, 1400.0, 2000.0, 1800.0, 0.0]
sumator = 0.0
for i in range(len(lata)):
    print("dla ", lata[i])
    ans = lata[i] / (1 + feet) ** (i + 1)
    sumator += ans
    print("ans", i, "=", ans)
    print("suma = ", sumator)
    print(20 * "-")
