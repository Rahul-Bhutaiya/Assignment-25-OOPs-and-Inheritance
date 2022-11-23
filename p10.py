"""
Write a python script to add the new method in SmartPhone class which accepts
Truecaller object as a parameter and call the fetch method of Truecaller.
"""

from p7 import Phone
from p6 import Calculator2
from p9 import Truecaller

class SmartPhone(Calculator2,Phone,Truecaller):

    def fetch_contact(num,obj=Truecaller()):
        obj.get_name(num)

#SmartPhone.fetch_contact(22222)