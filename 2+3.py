# Додаткове Завдання №2
int_list = []
new_list = []

while True:
    a = input("Введіть значення, або залиште пустим щоб закінчити список: ")
    if a == "":
        break
    else:
        int_list.append(int(a))
for i in range(len(int_list)):
    if int_list[i] % 2 == 0:
        new_list.append(int_list[i])
repeat = int(input("Введіть кількість повторів для парних чисел: "))
if repeat >= 1:
    new_list *= repeat
    print(new_list)
else:
    print(new_list)
int_list.clear()
# Додаткове Завдання № 3
b = input("Введіть значення щоб перевірити щи є воно в списку: ")
b = int(b)
count = new_list.count(b)
if count == 0:
    print("Данне число відсутнє в списку")
else:
    index_of_b = new_list.index(b)
    print("Данне число є в списку: {} разів".format(count))
    score = 0
    for o in range(len(new_list)):
        if b == new_list[o]:
            score += 1
            print("{} раз в списку воно знаходиться за індексом: {}".format(score, o))
