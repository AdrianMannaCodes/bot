fruits = [] 
for i in range(5): 
    x = input("what u like to add?") 
    fruits.append(x) 
print(fruits) 
vegetables = [] 
for i in range(5): 
    x = input("what u like to add?") 
    vegetables.append(x) 
print(vegetables) 
berries = [] 
for i in range(5): 
    x = input("what u like to add?") 
    berries.append(x) 
print(berries) 
superlist = [fruits, 
             vegetables, 
             berries]
print(superlist)
y = int(input("which list u wanna me to return by index"))
print(superlist[y])