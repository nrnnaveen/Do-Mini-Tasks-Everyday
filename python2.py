"""
13. Write a program to print all prime numbers between 1 to 100.
14. Write a program to print the Fibonacci sequence up to `n` terms.
15. Write a program to find the greatest common divisor (GCD) of two numbers.
16. Write a program to print a pattern like a pyramid using stars.
17. Write a program to print numbers in reverse order using a `for` loop.
18. Write a program to print the multiplication table from 1 to 10.
19. Write a program to check whether a number is an Armstrong number.
20. Write a program to find the sum of digits of a number.
"""

#13
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)                                                                      

#14
n_terms = 10
n1, n2 = 0, 1
for _ in range(n_terms):        
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth