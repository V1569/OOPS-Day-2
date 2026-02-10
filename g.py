#day 8
#eg for abstraction
#Example 1 (simple)
from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass

    def conc(self):
        print("I am concrete method")

class B(A):
    def method1(self):
        print("I am in class B")
    def method2(self):
        print("Method-2")

obj = B()
obj.method1()
obj.conc()



#Example 2 (vehicle)
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def brakes(self):
        print("Brakes are applied")

class Car(Vehicle):
    def start_engine(self):
        print("The car Engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("The Bike Engine started")

class Bus(Vehicle):
    def start_engine(self):
        print("The Bus Engine started")

c = Car()
c.start_engine()
c.brakes()


#eg for class variables class method
class A:
    x = 11

    def __init__(self):
        pass

    @classmethod
    def incrementation(cls):
        cls.x += 1

    @staticmethod
    def display_sum(a, b):
        print(a + b)

class B(A):
    def inc(self):
        A.x += 1
        print(A.x)

class C(A):
    def inc(self):
        A.x += 1
        print(A.x)

A.incrementation()
print(A.x)
a = A()
print(a.x)
b = B()
b.inc()
c = C()
c.inc()
A.display_sum(1, 2)


#eg for decorators
#Example 1 — Authentication decorator (login)
def login(decorated):
    def wrapper(user, password):
        if user == "admin" and password == "1234":
            print("Login successful")
            decorated(user, password)
        else:
            print("Login failed")
    return wrapper
@login
def login_page(user, password):
    print("welcome to the dashboard")
login_page("admin", "1234")
login_page("someone", "bad")


#Example 2 — Execution time decorator (timing)
import time
def execution_time(func):
    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time()
        print("Elapsed:", end - start)
    return wrapper
@execution_time
def first_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("sum :", total)
first_n(1000000)




#assignment
#task1
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")

d = Dog()
c = Cat()
cw = Cow()
d.sound()
d.sleep()
c.sound()
cw.sound()


#task 2
class Student:
    college_name = "ABC College"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    @staticmethod
    def is_pass(marks):
        return "Pass" if marks >= 35 else "Fail"
    
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print()

s1 = Student("Varshini", 101)
s2 = Student("Rahul", 102)
s1.display()
s2.display()
Student.change_college("XYZ College")
s1.display()
s2.display()
print("Result:", Student.is_pass(40))
print("Result:", Student.is_pass(20))



#task3 decorator
def admin_only(func):
    def wrapper(username):
        if username == "admin":
            func(username)
        else:
            print("Access Denied")
    return wrapper

@admin_only
def dashboard(username):
    print("Welcome to Admin Dashboard")

dashboard("admin")
dashboard("user")


