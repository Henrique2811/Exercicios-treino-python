x = 0
n = 1

while True:
    print(f"{n}x{x} = {n * x}")
    x += 1
    if x > 10:
        n += 1
        x = 0
        print(f"{n}x{x} = {n * x}")
        x += 1
    if n > 10:
        break
