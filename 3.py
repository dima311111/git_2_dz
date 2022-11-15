# найпростіший варіант
for i in range(1, 30):
    print("*" * i)
# З використанням вкладених циклів
for i in range(0, 30):
    print()
    for x in range(0, i):
        print("*", end="")
        