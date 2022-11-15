a = int(input("a"))
b = int(input("b"))
for k in range(a, b + 1):

    prime = True

    for i in range(a, k):
        if k % i == 0:
            prime = False
            break

    if prime:
        print('{} - простое число'.format(k))
