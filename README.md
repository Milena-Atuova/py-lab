## Лабораторная работа 1

### Задание 1
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![Картинка 1](./images/lab01/01_greeting.png)

### Задание 2
```python
a = float(input("A: ").replace(",", "."))
b = float(input("B: ").replace(",", "."))

print(f"sum={a + b}; avg={(a + b) / 2}")
```
![Картинка 2]("C:\Users\admin\Downloads\2025-09-22_22-26-32.png")

### Задание 3
```python
price=float(input("Цена: "))
discount=float(input("Скидка: "))
vat=float(input("НДС: "))

base=price*(1-discount/100)
vat_amount=base*(vat/100)
total=base+vat_amount
print(f"Бфза после скидки: {base:.2f}")
print(f"НДС: {vat_amount:.2f}")
print(f"Итого к оплате: {total:.2f}")
```
![Картинка 3]("C:\Users\admin\Downloads\2025-09-18_11-52-53.png")

### Задание 4
```python
m=int(input("Минуты:"))
print(f"{m//60:02d}:{m%60:02d}")
```
![Картинка 4]("C:\Users\admin\Downloads\2025-09-18_11-54-35.png")

### Задание 5
```python
name=input("ФИО:").strip()
n=name.split()
print(f"Инициалы: {n[0][0]}{n[1][0]}{n[2][0]}.")
print(f"Длина: {len(name.strip())}")
```
![Картинка 5]("C:\Users\admin\Downloads\2025-09-18_11-56-13.png")

### Задание 6
```python
n=int(input("Количество студентов: "))
och=zoch=0
for i in range(n):
    inf=input("Фамилия, Имя, возраст, форма обучения: ").split()
    if inf[3]=="True":
        och+=1
    else:
        zoch+=1
print(och,zoch)
```
![Картинка 6]("C:\Users\admin\Downloads\2025-09-18_11-59-24.png")

