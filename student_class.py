class Student():
    #Create constructor and attribute
    def __init__(self , input_school , input_department ,input_ID, input_credit , input_GPA , input_school_address , input_personal_address):
        self.school = input_school
        self.department = input_department 
        self.ID = input_ID
        self.credit = input_credit
        self.GPA = input_GPA
        self.school_address = input_school_address
        self.personal_address = input_personal_address

    #Set the attribute ,and it can make chanege attribute more convenient
    def setschool(self,input_school):
        self.school = input_school

    #Get the attribute and return 
    def getschool(self):
        return self.school

    def setdepartment(self,input_department):
        self.department = input_department

    def getdepartment(self):
        return self.department

    def setID(self,input_ID):
        self.ID = input_ID

    def getID(self):
        return self.ID

    def setcredit(self,input_credit):
        self.credit = input_credit

    def getcredit(self):
        return self.credit

    def setGPA(self,input_GPA):
        self.GPA = input_GPA

    def getGPA(self):
        return self.GPA

    def setschool_address(self,input_school_address):
        self.school_address = input_school_address

    def getschool_address(self):
        return self.school_address

    def setpersonal_address(self,input_personal_address):
        self.personal_address = input_personal_address

    def getpersonal_address(self):
        return self.personal_address
    

    
#Create a object and give it the attribute
student1 = Student('STUST' , 'CSIE' , '13' , '56' , '5' , 'Tainan' , 'Taipei')

#Use 'set' to change stuff in the attribute
student1.setschool('NTU')

student1.setschool_address('Taipei')

#Print every details of student1``
print('School name : ',student1.getschool())
print('Department : ',student1.getdepartment())
print('GPA : ',student1.getGPA())
print('ID : ',student1.getID())
print('Personal address : ',student1.getpersonal_address())
print('School address : ',student1.getschool_address())
print('Credit : ',student1.getcredit())

