n = int(input("Количество студентов: "))
och = zoch = 0
for i in range(n):
    inf = input("Фамилия, Имя, возраст, форма обучения: ").split()
    if inf[3] == "True":
        och += 1
    else:
        zoch += 1
print(och, zoch)
