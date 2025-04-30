# Week 3 Activity 2: Factorial Function

# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# It is denoted by n! and is defined as:
# n! = n * (n-1) * (n-2) * ... * 1
# For example, 5! = 5 * 4 * 3 * 2 * 1 = 120
# The factorial of 0 is defined to be 1 (0! = 1).

# Factorial function using two methods: iterative and recursive

def response(response,n):
  if response == 0:
    return (print(n,"! : Sorry, factorial does not exist for negative numbers"))
  elif response == 1:
    return (print(n,'! :',1))
  elif response > 1:
    return (print(n,'! :',response))
  return response

negative_number_response = "! : Sorry, factorial does not exist for negative numbers"

# 1. Iterative method: Using a loop to calculate the factorial
def factorial_m1(n):
  if n < 0:
    return (print(n,negative_number_response))
  else:
    factorial = 1
    for i in range(1,n + 1):
      factorial = factorial*i #multiply i with factorial
    print(n,'! :',factorial,'\n')
    return factorial
  
# # 2. Recursive method: Using recursion to calculate the factorial
def factorial_m2(n):
   result = 1
   if n < 0:
     result = 0
     return (response(result,n))
   elif (n == 0) or (n == 1):
     #print(response(1,n))
     return result
   else:
     result = (n*factorial_m2(n-1))
     #print(n,'! :',result)
     return (result)

#Test the function with different values
print("Factorial using Iterative method")
print("--------------------------------------------------")
# Test cases - Negative Values
print("Negative Values : -1 ")
factorial_m1(-1)

# Test cases - zero
print("Zero Value : 0 ")
factorial_m1(0)

# Test cases - Positive Values
print("Positive Values : 1, 2, 3, 4")
factorial_m1(1)
factorial_m1(2)
factorial_m1(3)
factorial_m1(4)

print("Factorial using Recursive method")
print("--------------------------------------------------")

# Test cases - Negative Values
print("Negative Values : -1 ")
factorial_m2(-1)

# Test cases - zero
print("Zero Value : 0 ")
print(factorial_m2(0))

# Test cases - Positive Values
print("Positive Values : 1, 2, 3, 4")
print("1 ! :",factorial_m2(1))
print("2 ! :",factorial_m2(2))
print("3 ! :",factorial_m2(3))
print("4 ! :",factorial_m2(4))