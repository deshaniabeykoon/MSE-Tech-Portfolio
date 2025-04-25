def factorial_m1(n):
  if n < 0:
    return (print("Sorry, No factorial defined for negative numbers"))
  else:
    factorial = 1
    for i in range(1,n + 1):
      factorial = factorial*i
    print(n,'! :',factorial)
    return factorial
  
# Test the function with different values
# Test cases - Negative Values
factorial_m1(-1)

# Test cases - zero
factorial_m1(0)

# Test cases - Positive Values
factorial_m1(1)
factorial_m1(2)
factorial_m1(3)
factorial_m1(4)