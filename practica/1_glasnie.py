str_in = input("Введите строку:")
a = 'а, у, о, ы, и, э, я, ю, ё, е'
b = 0
c = 0
e = ''

for i in str_in:
    if i in a:
        b+=1
        e+=i
    else:
        c+=1
if b == c:
    print(e)

print(b)
print(c)