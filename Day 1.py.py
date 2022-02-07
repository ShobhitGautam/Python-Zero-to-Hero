# Assignment 1
# Take multiple numbers as input and print the sum.

x = [int(i) for i in input('Enter integer values: ').split()]

s = 0
for j in x:
  s += j # sum = sum + j

print(s)
