class Numbers:
    def __init__(self, num1):
        self.num1 = num1

# 1. Iterative method: Using a loop to calculate the factorial
    def calculate_factorial(self):
        if self.num1 < 0:
            return (print(self.num1,"! : Sorry, factorial does not exist for negative numbers"))
        else:
            factorial = 1
            for i in range(1,self.num1 + 1):
                factorial = factorial*i #multiply i with factorial
                print(self.num1,'! :',factorial)
            return factorial

number = Numbers(5)
number.calculate_factorial()