#day 5 pratice
#eg for hierarchical
class father:
    def __init__(self,surname,name):
        self.surname=surname
        self.father_name=name
    def display_surname(self):
        print("the surname is ",self.surname)
    def display_father_name(self):
        print("the surname is ",self.father_name)

class son(father):
    def __init__(self,name,surname,father_name):
        self.name=name
        super().__init__(surname,father_name)
    def display_name(self):
        print("The name of the son is",self.name)

class daughter(father):
    def __init__(self,name,surname,father_name):
        self.name=name
        super().__init__(surname,father_name)
    def display_name(self):
        print("The name of the daughter is ", self.name)

obj=son("Raj","S","likhith")
obj.display_name()
obj.display_father_name()
obj1=daughter("kumari", "K", "Rajesh")
obj1.display_name()
obj.display_father_name()

#eg 2 for hierarchical

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder=account_holder
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            self.display_balance()
        else:
            print("You have insufficient amount in your Account.")
    def display_balance(self):
        print("The balance is",self.balance)

class SavingsAccount(BankAccount):
    def __init__(self,interest_rate,name):
        temp_interest=interest_rate/100
        self.interest_rate=temp_interest
        super().__init__(name)
    def add_interest(self):
        self.balance*=(1+self.interest_rate)
        super().display_balance()

class CurrentAccount(BankAccount):
    def __init__(self,overdraft_limit, name):
        self.overdraft_limit=overdraft_limit
        super().__init__(name)
    def withdraw_with_overdraft(self,amount):
        if amount<self.balance+self.overdraft_limit:  # 590 < 600
            self.balance-=amount
            super().display_balance()
        else:
            print("Overdraft limit is exceeded")

SA=SavingsAccount(10,"Raja")
CA=CurrentAccount(100,"Raja")
# SA.deposit(100)
# SA.withdraw(30)
# SA.add_interest()
CA.deposit(500)
CA.withdraw_with_overdraft(590)



#eg 3 for hybrid
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
        print(f"Sport Name: {self.sport_name}")

class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        # Initialize Person only once
        Person.__init__(self, name)
        self.student_id = student_id
        self.sport_name = sport_name
        self.college_name = college_name

    def display_college_student(self):
        print(f"College Name: {self.college_name}")
student = CollegeStudent("supritha", "1SW24EC001", "Cricket", "mrit")
student.display_person()
student.display_student()
student.display_sports_player()
student.display_college_student()



#assisgnment 
# eg for encapsulation
class InstagramAccount:
    account_name="name"
    _private_reels=[]

    
    def __init__(self,password):
        self.__password = password
        self.__archived_reels=[]

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")
    
    def add__archived_reels(self,name):
        self.__archived_reels.append(name)
        print("Reel has been added",self.__archived_reels)

    def display__archived_reels(self,password):
        if password == self.__password:
            return self.__archived_reels
        else:
            print("Access Denied! Only account holder can view archived reels")
    
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"
        
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Incorrect old password.")
    
account = InstagramAccount("varshini_account", "1234")
account.add_private_reel("Trip Reel")
account.add_private_reel("Birthday Reel")
account.add_archived_reel("Old Memories")
account.add_archived_reel("College Fest")
account.display_private_reels(True)  
account.display_private_reels(False)  
account.display_archived_reels("1234")  
account.display_archived_reels("0000")  
account.set_password("1234", "5678")
account.display_archived_reels("5678")
print("Getter Output:", account.get_archived_reels("5678"))