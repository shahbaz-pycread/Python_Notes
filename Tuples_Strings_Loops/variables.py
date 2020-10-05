print(
"""
    A Python variable is a symbolic name that is a reference or pointer to an object.
    Once an object is assigned to a variable, we can refer to that object by name.
"""
)

#Creating a variable

user_name = "Shahbaz"

print(f"My name is {user_name}")


# Rules for defining variables in Python

# a)A variable name must start with a letter or the underscore character.

_username = "Shahbaz Alam"
print(f"My name is {_username}")

# b)A variable name cannot start with a number

#) c) A vaiable name can only contain alpha-numeric characters  and underscores.

#) d)Variable names are case-sensitive (age, Age and AGE are three different variables)



#Legal variable names:
print(
"""
    LEGAL VARIABLE NAME
    -----------------
    myvar = "Shahbaz"
    my_var = "Shahbaz"
    _my_var = "Shahbaz"
    myVar = "Shahbaz"
    MYVAR = "Shahbaz"
    myvar2 = "Shahbaz"
"""
)

#Illegal variable names:
print(
"""
    ILLEGAL VARIABLE NAME
    -----------------
    2myvar = "Shahbaz"
    my-var = "Shahbaz"
    my var = "Shahbaz"
"""
)
