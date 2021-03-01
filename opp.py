# class Dog():
#     def __init__(self,breed, name):
#         self.breed=breed
#         self.name=name

#     def bark(self):
#         print(f'Woof my name is {self.name}')

# my_dog=Dog('yorkie', 'Bear')

# print(my_dog.breed)
# print(my_dog.bark())

# class Animal():
#     def __init__(self):
#         print('ANIMAL CREATED')

#     def eating(self):
#         print('I am an animal eating')
    
#     def who_am_i(self):
#         print('I am an animal')

# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print('Dog Created')

# my_dog=Dog()
# print(my_dog.eating())


# Volume ans Surface area of cylinder

# class Cylinder:

#     pi=3.14

#     def __init__(self, height, radius):
#         self.height=height
#         self.radius=radius

#     def volume(self):
#         return (Cylinder.pi)*(self.radius**2)*(self.height)

#     def surface_area(self):
#         result1=2*(Cylinder.pi*self.radius*self.height)
#         result2=2*(Cylinder.pi*self.radius**2)
#         return result1+result2

# c=Cylinder(2,3)

# print(c.volume())
# print(c.surface_area())

# Bank Practice

class Account:

    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    
    def deposit(self, value):
        self.balance=self.balance+value
        print('Deposit Accepted')

    def withdraw(self, value):
        if self.balance>=value:
            self.balance=self.balance-value
            print('Withdrawl Accepted')
        else:
            print('Withdrawal Failed')

    def __str__(self):
        return (f'Owner: {self.owner} \nBalance: {self.balance}')

myAccount=Account('Kaeneth', 1000)

print(myAccount)
myAccount.deposit(1000)
print(myAccount)
myAccount.withdraw(500)
print(myAccount)


