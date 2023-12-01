import datetime




class Students():
    def __init__(self , input_school_name , input_major, input_student_name , input_birth_year , input_age):
        self.school_name = input_school_name 
        self.major = input_major
        self.student_name= input_student_name
        self.birth_year = input_birth_year
        self.age = input_age


    @property
    def get_school_name(self):
        return self.school_name
    
    @get_school_name.setter
    def set_school_name(self , input_school_name ):
        self.school_name =  input_school_name 

    @get_school_name.deleter
    def del_school_name(self):
        del self.school_name

    @property
    def get_birth_year(self):
        return self.birth_year
    
    @get_birth_year.setter
    def set_birth_year(self , input_birth_year):
        self.birth_year = input_birth_year

    @property
    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    @get_age.setter
    def set_age(self , input_age):
        self.age = input_age

Student1 = Students('STUST' , 'CSIE' , 'John' , 2001, 0)

Student1.set_school_name = 'SCU'



class Person():
    def __init__(self , input_first_name , input_last_name , input_full_name):
        self.first_name = input_first_name
        self.last_name = input_last_name
        self.full_name = input_full_name

    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self , input_first_name):
        self.first_name = input_first_name

    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self , input_last_name):
        self.last_name = input_last_name

    @property
    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    def set_full_name(self , input_full_name):
        self.full_name = input_full_name

person1 = Person('Kelvin' , 'Wu' , 'Kelvin Wu')

person1.set_first_name('Aaron')

print(person1.get_first_name())

print(person1.get_last_name())

print(person1.get_full_name)






class Purchase():
    def __init__(self , input_purchase_count ):
        self.purchase_count = input_purchase_count

    @property
    def purchase_count1(self):
        return self.purchase_count
    
    @purchase_count1.setter
    def purchase_count1(self , input_purchase_count):
        if input_purchase_count < 3 or input_purchase_count > 30:
            raise ValueError('請重新下單')
        self.purchase_count = input_purchase_count

Purchase1 = Purchase(1)

Purchase1.purchase_count1 = 50

print(Purchase1.purchase_count1)

