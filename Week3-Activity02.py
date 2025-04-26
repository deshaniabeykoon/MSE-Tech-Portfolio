# Week 3 Activity 2: Factorial Function

# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# It is denoted by n! and is defined as:
# n! = n * (n-1) * (n-2) * ... * 1
# For example, 5! = 5 * 4 * 3 * 2 * 1 = 120
# The factorial of 0 is defined to be 1 (0! = 1).

# Factorial function using two methods: iterative and recursive

negative_number_response = "! : Sorry, factorial does not exist for negative numbers"

# 1. Iterative method: Using a loop to calculate the factorial
def factorial_m1(n):
  if n < 0:
    return (print(n,negative_number_response))
  else:
    factorial = 1
    for i in range(1,n + 1):
      factorial = factorial*i #multiply i with factorial
    print(n,'! :',factorial)
    return factorial
  
# # 2. Recursive method: Using recursion to calculate the factorial
def factorial_m2(n):
   if n < 0:
     return (print(n, negative_number_response))
   elif (n == 1):
     return 1
   else:
     result = (n*factorial_m2(n-1))
     return result

#Test the function with different values
print("Factorial using Iterative method")
print("--------------------------------------------------")
# Test cases - Negative Values
factorial_m1(-1)

# Test cases - zero
factorial_m1(0)

# Test cases - Positive Values
factorial_m1(1)
factorial_m1(2)
factorial_m1(3)
factorial_m1(4)

print("Factorial using Iterative method")
print("--------------------------------------------------")
factorial_m2(3)