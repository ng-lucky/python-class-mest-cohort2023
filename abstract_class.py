from abc import ABC, abstractmethod

class User:
    first_name =''
    last_name = ''
    email = ''
    phone_number = ''
    alias = ''
    password = ''

class Product:
    name =''
    type = ''
    price = 0
    expiry_date = ''
    weight = 0

class UserAbstract(ABC):
    @abstractmethod
    def create_user(self, user: User):
        pass
    
    @abstractmethod
    def get_all_users(self):
        pass
    
    @abstractmethod
    def get_user_by_id(self, user_id):
        pass


class UserManager(UserAbstract):
    def create_user(self, user: User):
        print("Saving's in progress...  \n")
        print(f"First Name: {user.first_name}")
        
    
    def get_all_users(self):
        print("hello tiny! we are getting all users here")
    
    def get_user_by_id(self, user_id):
        first_name = 'Olamide'
        last_name = 'Ahmed'
        print(f"Hello {first_name} {user_id}")
        
class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self, product: Product):
        pass
    
    
    
    
user = User()
user.alias = 'peru1234'
user.first_name = 'Peru'
user.last_name="Para"
       
user_manager = UserManager()
user_manager.get_user_by_id(78)
user_manager.create_user(user)