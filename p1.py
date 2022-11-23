#Write a python script to create a Profile class with 3 attributes (name, email, age).

class Profile:
    def __init__(self,name=None,email=None,age=None):
        self.name,self.email,self.age=name,email,age

#Profile1=Profile('Rahul Bhutaiya','rahulbhutaiya@gmail.com',20)