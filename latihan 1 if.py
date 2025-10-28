a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if a > b and a > c and a > d:
    terbesar1 = a
elif b > a and b > c and b > d:
    terbesar1 = b
elif c > a and c > b and c > d:
    terbesar1 = c
else:
    terbesar1 = d


print("The largest number is:", terbesar1)