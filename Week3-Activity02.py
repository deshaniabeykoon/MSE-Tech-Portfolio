num = 4
factorial = 1
  
def factorial_m1(n, f):
  if n < 0:
    return (print("Sorry, factorial does not exist for negative numbers"))
  else:
    for i in range(1,n + 1):
      f = f*i
    print(n,'! :',f)
    return f

factorial_m1(num,factorial)