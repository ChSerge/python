fold3 = "Fizz"
fold5 = "Buzz"
for i in range(100):
    if (i+1) % 3 + (i+1) % 5 == 0:
        print(fold3+fold5)
    elif (i+1) % 3 == 0:
        print(fold3)
    elif (i+1) % 5 == 0:
        print(fold5)
    else:
        print(i+1)

