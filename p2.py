#Write a python script to update the above Profile class with encapsulation.

class Profile:
    def __init__(self,name=None,email=None,age=None):
        self.name,self.email,self.age=name,email,age

    def update_prof_data(self,name,email,age):
        self.name,self.age,self.email=name,age,email


# Profile1=Profile('Rahul Bhutaiya','rahulbhutaiya@gmail.com',20)
# Profile1.update_prof_data('Rahul Bhungaliya','rahul@gmail.com',20)