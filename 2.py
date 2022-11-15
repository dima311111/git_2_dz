a = int(input("Введіть число : "))
faktorial = 1
for i in range(1, a+1):
    faktorial *= i
print("Факторіалом введеного числа буде : " + str(faktorial))
