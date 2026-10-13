import time as t

entry={"a": 1,
       "b": 5,
       "c": 10}
print(entry)
del entry["b"]
t.sleep(1)
print(entry)
entry["a"]=12
t.sleep(1)
print(entry)