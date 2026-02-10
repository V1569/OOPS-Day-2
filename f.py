#day 6
#eg for encapsulation
class BankAccount:
    account_holder_name="unknown"
    _account_type="Savings"

    def __init__(self,pin):
        self.__balance=0
        self.__pin=pin

    def set_pin(self,new_pin):
        self.__pin=new_pin
        print("Pin has been set.")
   
    def get_pin(self):
        return self.__pin

    def verify_pin(self,new_pin):
        return new_pin==self.__pin

    def get_balance(self,pin):
        if self.verify_pin(pin):
            return self.__balance
        else:
            return "Incorrect pin."
   
    def set_balance(self,pin,amount):
        if self.verify_pin(pin):
            self.__balance+=amount
            print("The updated balance is",self.__balance)
        else:
            print("Enter valid PIN")

BA=BankAccount(1234)
# print("Old account name is",BA.account_holder_name)
BA.account_holder_name="Raj"
print("The updated account holder name is",BA.account_holder_name)
# print("The account old pin is",BA.get_pin())
BA.set_pin(9955)
print("The account new pin is",BA.get_pin())
print("The old balance is",BA.get_balance(9955))
BA.set_balance(1234,100)




#eg for polymorphism
class media_player:
    def play(self):
        print("Playing media")

class audio_player(media_player):
    def play(self):
        print("Playing audio")

class video_player(media_player):
    def play(self):
        print("Playing video")

AP=audio_player()
AP.play()
VP=video_player()
VP.play()



#assignment
#eg for polymorphism
class Payment:
   def pay(self):
       print("Processing payment...")
       
class GooglePay(Payment):
    def pay(self):
       print("Payment done using Google Pay") 
        
class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe")

class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")

gpay = GooglePay()
phonepe = PhonePe()
card = CreditCard()
gpay.pay()
phonepe.pay()
card.pay()

        

#eg for abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started")

car = Car()
bike = Bike()
bus = Bus()
car.start_engine()
bike.start_engine()
bus.start_engine()
