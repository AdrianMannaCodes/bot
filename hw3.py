# note: uses regex for easier inputs

import re
items = []


for i in range(24):
   user_value = input("Add anything, prefixes: n to remove index, i to show the index of element ")
   n=re.sub(r"\D+", "", user_value)
   i=re.sub(r"^i\s*", "", user_value)
   if user_value.startswith(("n", "n ")):
      items.pop(int(n))
   elif user_value.startswith("i" or "i "):
     print(items.index(i))
   else:
     items.append(user_value)
   print(items)