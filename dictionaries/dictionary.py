print(
'''
    A dictionary is a collection which is unordered,
    changeable and indexed. In Python, dictionaries are
    written with curly brackets, and they have
    keys and values.
    ---------------------------------------------------

'''
)

# Create and print a dictionary

csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'cup_last_won' : 2018
}


#Accessing Items
print(
'''
    We can access the items of a dictionary by referring
    to its key name, inside square brackets.
    -
'''
)
# Get the value of the `Captain` key:
print('The captain of the team is ' + csk_team['Captain'])

#There is also a method called `get()` that will give us same result
skipper = csk_team.get('Captain')

print(f'The captain of the team is {skipper}')

#Change Values
print(
'''
    We can change the values of a specific item by
    referring to its key name
    ---------------------------------
'''
)

#Change the `Coach`
csk_team['Coach'] = 'Mike Hussey'
print(csk_team)

#Loop through a dictionary
print(
'''
    We can loop through a dictionary by
    using a `for` loop.
    When looping through a dictionary, the return values are
    the keys of the dictionary, but there are methods to return
    the values as well.
    ---------------------------------------------
''')

#Print all key names in the dictionary, one by one

csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'cup_last_won' : 2018
}

for x in csk_team:
    print(x)

#Print all the values in the dictionary, one by one

csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'cup_last_won' : 2018
}

for y in csk_team:
    print(csk_team[y])


# We can also use the `values()` method to return values of a dictionary
csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'cup_last_won' : 2018
}
for y in csk_team.values():
    print(y)

print(
'''
    Loop through both keys and values,
    by using the `items()` method.
    ------------------------------------
''')

csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'cup_last_won' : 2018
}

for x,y in csk_team.items():
    print(x,':' ,y)


#Check if key exists
print(
'''
    To determine if the specified key is present
    in the dictionary, use `in` keyword.
    -------------------------------------
'''
)
#Check if "Coach" is pressnt in the dictionary.
csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'cup_last_won' : 2018
}

if "Coach" in csk_team:
    print("Yes, Coach is present and its value is " + csk_team['Coach'])

#Dictionary length
print(
'''
    To determine how many items(key-value) pairs
    a dictionary has, use the `len()` function.
    -----------------------------------------
'''
)
#Print the  number of the items in the dictionary.
csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'cup_last_won' : 2018
}
print('The length of the dictionary is ' + str(len(csk_team)))

#Adding items
print(
'''
    Adding an item to the dictionary is done
    by using a new index key and assigning a value
    to it.
    ----------------------------------
'''
)
#Add `Batting_Coach to the dictionary`
csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'cup_last_won' : 2018
}
csk_team['Batting_Coach'] = 'Mike Hussey'
print(csk_team)

#Removing items
print(
'''
    There are several methods to remove items
    from a dictionary.
    ***********************

    a)pop()
    b)popitem()
    c) del keyword
    d)clear()
'''
)

#pop() method
print("The pop() removes the item with the specified key name.")
csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'Batting_Coach' : 'Mike Hussey',
    'cup_last_won' : 2018
}
csk_team.pop('Batting_Coach')
print(csk_team)

#popitem()
print("The popitem() removes the last inserted item")
csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'Batting_Coach' : 'Mike Hussey',
    'cup_last_won' : 2018
}
csk_team.popitem()
print(csk_team)

#del keyword
# The del keyword removes the item with the specified key name:
# The del keyword can also delete the dictionary completely:
csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'Batting_Coach' : 'Mike Hussey',
    'cup_last_won' : 2018
}
del csk_team['cup_last_won']
print(csk_team)

#clear()
# The clear() method empties the dictionary:

csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'Batting_Coach' : 'Mike Hussey',
    'cup_last_won' : 2018
}
csk_team.clear()
print()

#Copy a dictionary
print(
'''
    We  cannot copy a dictionary simply by typing dict2 = dict1, because:
    dict2 will only be a reference to dict1,
    and changes made in dict1 will automatically also be made in dict2.
    ********************
    There are ways to make a copy,
    a) one way is to use the built-in Dictionary method `copy()`.
    b) Another way to make a copy is to use the built-in function dict().
'''
)
#Make a copy of dictionary with the copy() method
csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'Batting_Coach' : 'Mike Hussey',
    'cup_last_won' : 2018
}
fav_team = csk_team.copy()
print(fav_team)

# Make a copy of a dictionary with the dict() function:
csk_team = {
    'Captain' : 'MS Dhoni',
    'Coach' : 'Stephen Fleming',
    'Batting_Coach' : 'Mike Hussey',
    'cup_last_won' : 2018
}
fav_team = dict(csk_team)
print(fav_team)


#Nested Dictionaries
print(
'''
    A dictionary can also contain many dictionaries.
    This is called NESTED DICTIONARIES.
    --------------------------------------
'''
)
# Create a dictionary that contain three dictionaries:

csk = {
    "player1" : {
        "Name" : "MS Dhoni",
        "Country" : "India"
    },
    "player2" : {
        "Name" : "Shane Watson",
        "Country" : "Australia"
    },
    "player3" : {
        "Name" : "Faf Du Plesis",
        "Country" : "South Africa"
    },
    "player4" : {
        "Name" : "Dwayne Bravo",
        "Country" : "West Indies"
    }
}
print(csk)

#dict() Constructor
# It is also possible to use the dict() constructor to make a new dictionary:

team = dict(name = "CSK", captain = "MS Dhoni", coach="Stephen Fleming")
print(team)
