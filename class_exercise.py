#1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        
    def open_restaurant(self):
        print("The restaurant is open!")

restaurant = Restaurant("Pizza Palace", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

#2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        
    def open_restaurant(self):
        print("The restaurant is open!")
        

restaurant1 = Restaurant("Pizza Palace", "INigerian")
restaurant2 = Restaurant("Burger Joint", "American")
restaurant3 = Restaurant("Sushi Spot", "Japanese")


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#3
class User:
    def __init__(self, first_name, last_name, age, city, country, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
        self.email = email
        
    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
        print(f"Email: {self.email}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}! Nice to see you.")

user1 = User("Alamin", "Muss", 25, " kaduna", "Nigeria", "alaminmusamagaga@gmail.com")

user1.describe_user()
user1.greet_user()

#4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        
    def set_number_served(self, num_customers):
        self.number_served = num_customers
        print(f"Number of customers served: {self.number_served}")
        
    def increment_number_served(self, num_customers):
        self.number_served += num_customers
        print(f"Number of customers served: {self.number_served}")

restaurant = Restaurant("Burger King", "American")

# the initial number of customers served
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(10)
restaurant.increment_number_served(20)

restaurant = Restaurant("Burger King", "American")


print(f"Number of customers served: {restaurant.number_served}")


#5

class User:
    def __init__(self, first_name, last_name, age, city, country, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
        self.email = email
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
        print(f"Email: {self.email}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}! Nice to see you.")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
user1 = User('Alamin', 'Musa', 30, 'Kaduna', 'Nigeria', 'alamin@exp.com')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts) 
user1.reset_login_attempts()
print(user1.login_attempts)  

#6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        
    def set_number_served(self, num_customers):
        self.number_served = num_customers
        print(f"Number of customers served: {self.number_served}")
        
    def increment_number_served(self, num_customers):
        self.number_served += num_customers
        print(f"Number of customers served: {self.number_served}")

restaurant = Restaurant("Burger King", "American")

# the initial number of customers served
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(10)
restaurant.increment_number_served(20)

restaurant = Restaurant("Burger King", "American")


print(f"Number of customers served: {restaurant.number_served}")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        
    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        
    def display_flavors(self):
        print(f"The available flavors are: {', '.join(self.flavors)}")

# Example usage
ice_cream_stand = IceCreamStand("Ben & Jerry's", "Ice Cream")
ice_cream_stand.add_flavor("Chocolate Fudge Brownie")
ice_cream_stand.add_flavor("Phish Food")
ice_cream_stand.display_flavors()

#7 & 8
class User:
    def __init__(self, first_name, last_name, age, city, country, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Nice to see you.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, city, country, email):
        super().__init__(first_name, last_name, age, city, country, email)
        self.privileges = Privileges()

admin = Admin('Alamin', 'Musa', 40, 'Kaduna', 'Nigeria', '@example.com')
admin.privileges.show_privileges()

#10
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


my_restaurant = Restaurant("Italiano", "Italian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#11
class User:
    def __init__(self, first_name, last_name, age, city, country, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
        self.email = email
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        
 #12       
class User:
    def __init__(self, first_name, last_name, age, city, country, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
        self.email = email
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
        print(f"Email: {self.email}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}! Nice to see you.")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age, city, country, email):
        super().__init__(first_name, last_name, age, city, country, email)
        self.privileges = Privileges()



admin = Admin('Alamin', 'Musa', 35, 'Kaduna', 'Nigeria', 'alamin@gmail.com')
admin.privileges.show_privileges()


#13
import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def rolldie(self):
        print(random.randint(1, self.sides))

# create a 6-sided die and roll it 10 times
d6 = Die()
for i in range(10):
    d6.rolldie()

# create a 10-sided die and roll it 10 times
d10 = Die(sides=10)
for i in range(10):
    d10.rolldie()

# create a 20-sided die and roll it 10 times
d20 = Die(sides=20)
for i in range(10):
    d20.rolldie()

#14


