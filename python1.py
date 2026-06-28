"""
11. Write a program to sum all numbers in a list.
12. Write a program to find the sum of even numbers between 1 to 100.
"""

#11

a=[10,20,30,40,50]
sum=0
for i in a:
    sum += i
print(sum)

#12

sum=0
for i in range(1,101):
    if i%2==0:
        sum += i
print(sum)
