"""
Write a python script to update 2nd Question, add a class variable (platform) and
create a classmethod to access it.
"""


class Profile:

    platform='ineuron.ai'

    def __init__(self,name=None,email=None,age=None):
        self.name,self.email,self.age=name,email,age

    def update_prof_data(self,name,email,age):
        self.name,self.age,self.email=name,age,email

    @classmethod
    def get_platform(cls):
        return cls.platform

#print(Profile.get_platform())