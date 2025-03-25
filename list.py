games = ['minecraft', 'PUBG', 'COD', 'FNAF', 'granny' ]

print(games) # simple calling of list games
print (games[3]) # calling third element of games which is actualy at 4rth place
print(games[1:4]) # slicing starts from element 1 and ends at element 4
print(games[1:1]) # Why is it empty
#since it starts from 1 and ends at 1, the list apears empty

print(games[-1]) # in such cases, list is read in a reverse manner

games.append("smash it")# append adds an element at end of function
print(games)

games.pop(5)# removes an elemenet from the written location
print(games)

games.copy()# copies a list
print(games)

count_pubg =games.count("PUBG") # Counts occurrences of 'PUBG' in a list

print("PUBG appears:", count_pubg, "times")


games.clear()# as the name suggest, clear method removes every element
print(games)
