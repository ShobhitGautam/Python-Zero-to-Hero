# Assignment 3
# from a dict, how can we print the key whose value is maximum.


s = input("Enter any Word: ")
s = s.replace(" ", "")
d = {}
for i in s:
  d[i] = d.get(i, 0) + 1
 
print(d)
max_key = max(d, key = d.get)
print(max_key)
