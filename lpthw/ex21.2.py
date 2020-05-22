def si(p, r, t, h):
    print("Calculating your simple interest:")
    print(f"{p} * {r} * {t} / {h}")
    return p * r * t / h

principle = input("principle : ")
rate = input("rate : ")
time = input("time : ")
h = input("h : ")
si(principle, rate, time, h)
