#Write a python script to update 2nd Question, change email and age to __email and__age.

class Profile:
    def __init__(self,name=None,email=None,age=None):
        self.name,self.__email,self.__age=name,email,age

    def update_prof_data(self,name,email,age):
        self.name,self.__age,self.__email=name,age,email


# Profile1=Profile('Rahul Bhutaiya','rahulbhutaiya@gmail.com',20)
# Profile1.update_prof_data('Rahul Bhungaliya','rahul@gmail.com',20)
# print(Profile1.__age)#it will give an error due to data abstraction
# print(Profile1._Profile__age)#it is the way to use data wich is abstracted