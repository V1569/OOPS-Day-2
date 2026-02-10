# day4 calss work
#eg for multiple
class father:
    def __init__(self,surname,name):
        self.surname=surname
        self.father_name=name

    def display_surname(self):
        print("surname is ", self.surname)

    def display_father_name(self):
        print("The fathername is ", self.father_name)

class mother:
    def __init__(self, eye_color,name):
        self.eye_color=eye_color
        self.mother_name=name

    def display_eye_color(self):
        print("eye_color is ", self.eye_color)

    def display_mother_name(self):
        print("The mothername is ", self.mother_name)
    
class son(father,mother):
    def __init__(self,name,surname,father_name,eye_color,mother_name):
        self.name=name
        father.__init__(self,surname,father_name)
        mother.__init__(self,eye_color,mother_name)
        
    def display_name(self):
        print("name is ", self.name)

son_obj=son("raj","K","rajesh","Blue","rani")
son_obj.display_name()
son_obj.display_eye_color()
son_obj.display_mother_name()
son_obj.display_surname()
son_obj.display_father_name()



#eg for multilevel

class grand_father:
    def __init__(self,property):
        self.Grand_father_property=property

    def display_property1(self):
        print("The grand father property is",self.Grand_father_property)

class father(grand_father):
    def __init__(self,property,g_f_property):
        self.father_property=property
        super().__init__(g_f_property)

    def display_property2(self):
        print("The father property is",self.father_property)

class son(father):
    def __init__(self,property,f_property,g_f_property):
        self.property=property
        super().__init__(f_property,g_f_property)
        
    def display_property3(self):
        print("The son property is",self.property)

son_obj=son("bike","Car","house")
son_obj.display_property2()
son_obj.display_property3()
son_obj.display_property1()









 
#day4 assignment

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest Added: {interest}")

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn with overdraft: {amount}")
        else:
            print("Overdraft limit exceeded")

print("Savings Account Test")
savings = SavingsAccount("Varshini", 10000, 5)
savings.deposit(2000)
savings.withdraw(1500)
savings.add_interest()
savings.display_balance()

print("\nCurrent Account Test")
current = CurrentAccount("Dharmendra", 5000, 3000)
current.withdraw_with_overdraft(7000)
current.display_balance()




#task2

class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def display_student(self):
        print(f"Student ID: {self.student_id}")

class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        super().__init__(name)
        self.sport_name = sport_name

    def display_sports_player(self):
        print(f"Sport: {self.sport_name}")

class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        Student.__init__(self, name, student_id)
        SportsPlayer.__init__(self, name, sport_name)
        self.college_name = college_name

    def display_college_student(self):
        print(f"College: {self.college_name}")

print("\nCollege Student Details")
student = CollegeStudent("Varshini", "CS101", "Badminton", "Dr.AIT")
student.display_person()
student.display_student()
student.display_sports_player()
student.display_college_student()

