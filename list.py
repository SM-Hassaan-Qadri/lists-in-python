games = ['minecraft', 'PUBG', 'COD', 'FNAF', 'granny' ]
series = ["All of us are dead", "Alice in Borderland", "Peaky blinders", "Squid game" ]

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

games.extend(series) #takes value from other list and combines it
print(games)

print("PUBG appears:", count_pubg, "times")


games.clear()# as the name suggest, clear method removes every element
print(games)

series.insert(3 , "Young sheldron")# Adds value in existing list
print(series)

series.reverse()# Reverses a series
print(series)

series.sort()# Arranges a list in an ascending order
print(series)
