spisok = []
while True:
    a = input("Введіть число або залиште пустим щоб закінчити: ")
    if a == "":
        break
    else:
        spisok.append(int(a))
dobytok = 1
for i in range(len(spisok)):
    dobytok *= spisok[i]
print("Сума чисел: " + str(sum(spisok)))
print("Добуток чисел: " + str(dobytok))
print(sorted(spisok))
print(sorted(spisok, reverse=True))
