print(
"""
    A list is a collection which is ordered and changeable.
    It allows duplicate members.
    In Python, lists are written with Square Brackets.

    ----------------------------------------------
"""
)

football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]

# Print the type

print(type(football_countries))

# Access the items
print(

    '''
        We can access the list items by referring to the index number.
        --------------------------------------------
    '''

)
# To access the first item of the list
print('The first element of the list is ' + football_countries[0])

# Negative Indexing
print(
'''
    Negative Indexing means beginning from the end, -1 refers to the last item.
    -2 refers to the second last item etc.
    ----------------------------------------------------
'''
)

#To access the last item of the list
print('The last item of the list is ' + football_countries[-1])


#List Length
print(
'''
    To determine how many items a list has, use the `len()` function.
    ---------------------------------------------
'''
)
# Number of items in the lists
print(f'The list has {len(football_countries)} items.')

#Loop through a lists
print(

'''
    We can loop through the list using a `for` loop.
    -----------------------------------
'''
)

#Looping
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]

for x in football_countries:
    print(x)

# Range of Indexes
print(
'''
    We can specify a range of indexes by specifying where to start and where to end the range.
    When specifying a range, the return value will be a new list with the specified items.
    ---------------------------------------
'''
)
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]

#Return the second, third:
print(football_countries[1:3])

print(
'''
    By leaving out the start value, the range will start at the first item.
    -------------------------------------
''')

#The example returns the items from the beginning to Spain
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
print(football_countries[:4])

print(
'''
    By leaving out the end value, the range will go on to the end of the list.
    ------------------------------------------
'''
)
#The example returns the items from the beginning to end of the list.
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
print(football_countries[0:])

#Change Item value
print(
'''
    To change the value of a specific item, refer to the index number.
    ---------------------------------
'''
)
#Change the Fifth item
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
football_countries[4] = 'England'
print(football_countries)

#Check of item exists in the list
print(
'''
    To determine if a specified item is present in a list
    use the `in` keyword.
    ----------------------------------------------
''')

#Check if 'Italy' is present in the list
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
if "Italy" in football_countries:
    index = football_countries.index('Italy')
    print(f"Yes, Index of Italy is {index}.")

#Add items
print(
'''
    To add an item to the end of the list,
    use the `append()` method.
    ---------------------------------------
''')

#Using the append() method to append an item.
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
football_countries.append('England')
print('England has been added to the list.')

print(
'''
    To add an item at the specified index,
    use the insert() method.
    ----------------------------------------
''')

#Insert an item in the second position
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
football_countries.insert(1,"Portugal")
print(football_countries)


#Remove item
print(
'''
    There are several methods to remove items from the list.
    ----------------------------------------
    a)remove()
    b)pop()
    c)del keyword
    d)clear()
'''
)
#The `remove()` method removes the specified item.
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
football_countries.remove("France")
print(football_countries)

#The `pop()` method removes the specified index, (or the last item if index is not specified.)
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
football_countries.pop()
print(football_countries)

#The `del` keyword removes the specified index.
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
del football_countries[5]
print(football_countries)

#The `del` keyword can also delete the list completely.
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
del football_countries

#The `clear()` method empties the list.
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
football_countries.clear()
print(football_countries)

#Copy a list
print(
'''
    We cannot copy a list simply by typing list2 = list1,
    because: list2 will only be a reference to list1,
    and changes made in list1 will automatically also be made in list2.
    There are ways to make a copy,
    a) One way is to use the built-in List method copy().
    b) Another way to make a copy is to use the built-in method list().


    ------------------------------------
''')

#Make a copy of list with the copy() method.
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
top_countries = football_countries.copy()
print(top_countries)

#Make a copy of list with the list() method.
football_countries = ["Argentina","Brazil","Germany","Spain","Italy","France"]
top_countries = list(football_countries)
print(top_countries)

#Join two lists
print(
'''
    There are several ways to join,
    or concatenate, two or more lists in Python.

    One of the easiest ways are by using the + operator.
    ----------------------------------
'''
)

#Join two lists
team1 = ["MI","DC","RCB","KKR"]
team2 = ["SRH","CSK","KP"]

teams = team1 + team2
print(teams)

#Another way to join two lists are by appending all the items from list2 into list1, one by one:
team1 = ["MI","DC","RCB","KKR"]
team2 = ["SRH","CSK","KP"]

for x in team2:
    team1.append(x)

print(team1)

#We can use the extend() method, which purpose is to add elements from one list to another list:
team1 = ["MI","DC","RCB","KKR"]
team2 = ["SRH","CSK","KP"]

team1.extend(team2)
print(team1)
