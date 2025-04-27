class Numbers:
    def __init__(self, num1):
        self.num1 = num1

    # 1. Iterative method: Using a loop to calculate the factorial
    def calculate_factorial(self):
        print("Calculating factorial...")
        if self.num1 < 0:
            return (print(self.num1,"! : Sorry, factorial does not exist for negative numbers"))
        elif self.num1 == 0:
            print(self.num1,'! :',1)
            return 1
        else:
            factorial = 1
            for i in range(1,self.num1 + 1):
                factorial = factorial*i #multiply i with factorial
                print(self.num1,'! :',factorial)
            print("Factorial of ", self.num1, "is:", factorial)
            return factorial

    def check_prime(self):
        print("Checking if prime...")
        if self.num1 > 1: 
            for i in range(2, int(self.num1**0.5) + 1): #  check for factors up to the square root of num1
                if (self.num1 % i) == 0:
                    print(self.num1, "is not a prime number")
                    break
                else:
                    print(self.num1, "is a prime number")
        else:
            print(self.num1, "is not a prime number")

input_number = int(input("Enter a number: "))
number = Numbers(input_number)
number.calculate_factorial()
number.check_prime()