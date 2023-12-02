import datetime




# #Use property to get ,set and delete the name
# class Student():
#     def __init__(self , input_name , input_school_name , input_birth_year , input_age):
#         self.name = input_name
#         self.school_name = input_school_name
#         self.birth_year = input_birth_year
#         self.age = input_age

#     @property
#     def Name(self):
#         return self.name
    
#     @Name.setter
#     def Name(self , input_name):
#         self.name = input_name

#     @Name.deleter
#     def Name(self):
#         del self.name

#     @property
#     def Age(self):
#         now = datetime.datetime.now()
#         return now.year - self.birth_year
    
#     @Age.setter
#     def Age(self , input_age):
#         self.age = input_age

# Student1 = Student('Zack' , 'SCU' , 2000 , 1)

# print(Student1.Name)
    
# print(Student1.Age)











# class Person():
#     def __init__(self , input_first_name , input_last_name , input_full_name):
#         self.first_name = input_first_name
#         self.last_name = input_last_name
#         self.full_name = input_full_name

#     @property
#     def Full_name(self):
#         return self.first_name + " " + self.last_name


# Person1 = Person('Ray' , 'Chen' , 'Eason lee')

# print(Person1.Full_name)


class order_count():
    def __init__(self , input_order_count):
        self.order_count = input_order_count

    @property
    def Order_count(self):
        if self.order_count < 5 or self.order_count > 50:
            raise ValueError('請重新輸入')
        return self.order_count
    
    @Order_count.setter
    def Order_count(self , input_order_count):
        
        self.order_count = input_order_count

order1 = order_count(2)

order1.Order_count = 23

print(order1.Order_count)

