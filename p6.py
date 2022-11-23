"""
Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
and division of 2 values and inherit it from the Calculator class.
"""

from p5 import Calculator

class Calculator2(Calculator):

    @staticmethod
    def mul(val1,val2):
        return val1*val2

    @staticmethod
    def div(val1,val2):
        if val2==0:
            return "We Can't Divide Any Value By Zero[0]"
        else:
            return val1/val2


# print(Calculator2.add(10,20))
# print(Calculator2.subtract(80,20))
# print(Calculator2.mul(10,20))
# print(Calculator2.div(40,20))