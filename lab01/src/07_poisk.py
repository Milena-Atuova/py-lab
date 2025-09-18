s=input("Строка: ")
index1=-1
correct=[""]


for i in range(len(s)):
    if s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        correct[0]=s[i]
        index1=i
elif (s[i] in '0123456789' and len(correct)==1 and index1!=-1):
