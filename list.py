names = ["Barinskij Ženâ", "Nikitina Anna", "Ražnikov Savva", "Alonzo Church"]
print(names)
intequery = int(input("1 - sort, 2 - reverse "))
if intequery==1:
    names.sort()
    print(names)
elif intequery==2:
    names.reverse()
    print(names)