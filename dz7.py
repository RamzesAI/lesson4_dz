def factorial_n(fact_n, n):
    for el in range(1, n + 1):
        fact_n = fact_n * el
        yield fact_n

gen_f = factorial_n(1, 4)
for el in gen_f:
    print(el)