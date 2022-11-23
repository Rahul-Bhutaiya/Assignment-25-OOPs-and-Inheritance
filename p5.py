#Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values.

class Calculator:

    @staticmethod
    def add(val1,val2):
        return val1+val2

    @staticmethod
    def subtract(val1,val2):
        return val1-val2

# print(Calculator.add(11,22))
# print(Calculator.subtract(33,22))