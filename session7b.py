class User:
    pass
class Driver:
    pass

data = []
print(type(data))
# Object Construction Statement
u = User()
d = Driver()
v= User()
print(type(u))
print(type(d))
print(u)
print(d)

# 2. Write Data in Object
u.address = "st 2 vendor park "
u.name = "John"
u.phone = "+91 99999 99999"
u.email = "john@gmail.com"

v.name = "Fionna"
v.age= " 42 years"
v.salary = 30,000

# reference copy
w=v

print(w)
d.name = "George"
d.phone = "+91 99999 01234"
d.email = "george@gmail.com"
d.experience = 3
d.license = "PBXRET3"

#3. Update Operation
u.name= "rahul"
v.age = 30
print(v.age)

#4. Delete Operation in Object
del u.phone
del d.license

#5. Read Operation on Object
print(u.__dict__)
print(v.__dict__)
print(d.__dict__)