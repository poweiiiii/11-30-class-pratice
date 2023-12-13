import datetime

class Student():
    def __init__(self , first_name , last_name , full_name , Id , school_name , sex , birth_year) :
        self.first_name = first_name    
        self.last_name = last_name 
        self.full_name = full_name
        self.Id = Id
        self.school_name = school_name
        self.sex = sex
        self.birth_year = birth_year

    @property   
    def Age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    @property
    def First_name(self):
        return self.first_name
    
    @First_name.setter
    def First_name(self , input_first_name):
        self.first_name = input_first_name

    @property
    def Last_name(self):
        return self.last_name
    
    @Last_name.setter
    def Last_name(self , input_last_name):
        self.last_name = input_last_name

    @property
    def Full_name(self):
        return self.first_name + ' ' + self.last_name
    
    @property 
    def ID(self):
        return self.ID
    
    @property
    def School_name(self):
        return self.school_name
    
    @School_name.setter
    def School_name(self , input_school_name):
        self.school_name = input_school_name

    @property
    def Sex(self):
        return self.sex


John = Student('John' , 'Lin' , 'John Lin' , '31' , 'STUST' , 'Men' , 2003)

print(John.Age)

John.first_name = 'Aaron'

print(John.Full_name)


