a = int(input("Введіть перше число : "))
b = int(input("Введіть друге число : "))
summa_1 = 0
summa_2 = 0
for i in range(a, b+1):
    summa_1 += i
for i in range(a, b + 1):
    ser_arifmet = summa_1 / (b - a + 1)
    if i % ser_arifmet == 0:
        summa_2 += i
print("Сума чисел в діапазоні від а до  b , які кратні середньому арифметичному цих чисел буде дорівнбвати : "
      + str(summa_2))
