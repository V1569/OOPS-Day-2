#day 3
# Father and Son (Single Inheritance + super())

class father:
    def __init__(self,surname,name):
        self.surname=surname
        self.father_name=name

    def display_surname(self):
        print("surname is ", self.surname)

    def display_father_name(self):
        print("The fathername is ", self.father_name)
class son(father):
    def __init__(self,name,surname,father_name):
        self.name=name
        super().__init__(surname,father_name)

    def display_name(self):
        print("name is ", self.name)
child_obj=son("john", "K","Rajesh")
child_obj.display_father_name()
child_obj.display_surname()
child_obj.display_name()


#Library Example (Single Inheritance)
class Books:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def display_books_details(self):
        print("The title of the book is ",self.title)
        print("The author of the book is ",self.author)

class IssuedBooks(Books):
    def __init__(self,title,author,issued_to,issued_date):
        self.issued_to=issued_to
        self.issued_date=issued_date
        super().__init__(title, author)

    def display_issued_books_details(self):
        print("The title of the book is ",self.title)
        print("The author of the book is ",self.author)
        print("The name of the person issued to is", self.issued_to)
        print("The date of issued is",self.issued_date)
IB=IssuedBooks("Python","John","Students","04-02-26")
IB.display_books_details()





#day 3 assignment

class Camera:
    def __init__(self, camera_quality):
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print("Camera Quality:", self.camera_quality)

class MusicPlayer:
    def __init__(self, sound_quality):
        self.sound_quality = sound_quality

    def display_music_details(self):
        print("Sound Quality:", self.sound_quality)

class SmartPhone(Camera, MusicPlayer):
    def __init__(self, brand, camera_quality, sound_quality):
        Camera.__init__(self, camera_quality)
        MusicPlayer.__init__(self, sound_quality)
        self.brand = brand
    def display_smartphone_details(self):
        print("Brand:", self.brand)
        self.display_camera_details()
        self.display_music_details()
phone = SmartPhone("Samsung", "108 MP", "Dolby Atmos")
phone.display_smartphone_details()




#task 2
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)

class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        self.display_product()
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)

class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        self.display_electronic_product()
        print("RAM:", self.ram)
        print("Storage:", self.storage)

mobile = MobilePhone(
    "Smartphone",
    25000,
    "OnePlus",
    "1 Year",
    "8GB",
    "128GB"
)
mobile.display_mobile_details()
