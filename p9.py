"""
Write a python script to create an application like Truecaller where names and
numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
number and 2nd to add a new entry).
"""

class Truecaller:
    
    phone_dictionary={'Rahul':22222}

    @classmethod
    def add_contact(cls,name,number):
        if name in cls.phone_dictionary.keys() and number not in cls.phone_dictionary.values():
            ans=input('Contact Exists With This Name, Do You Want To Update With New Number ?(yes/no)')
            match ans:
                case 'yes':
                    cls.phone_dictionary[str(name)]=int(number)
                    print('Contact Updated')
                case _:
                    pass

        elif name not in cls.phone_dictionary.keys() and number in cls.phone_dictionary.values():
            ans=input('Contact Exists With This Number, Do You Want To Update With New Name ?(yes/no)')
            match ans:
                case 'yes':
                    cls.phone_dictionary[str(name)]=int(number)
                    print('Contact Updated')
                case _:
                    pass
        
        elif name in cls.phone_dictionary.keys() and number in cls.phone_dictionary.values():
            print('This Contact is Already Exists in Your ContactBook')

        else:
            cls.phone_dictionary[str(name)]=int(number)
            print('Added A New Contact')
    
    @classmethod
    def get_name(cls,number):
        for x,y in cls.phone_dictionary.items():
            if y==number:
                print('Name With This Number is :',x)
                break
        else:
            print('Sorry This Number Does Not Exists in Your ContactBook')

#Truecaller.get_name(22222)