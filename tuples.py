people=("Drake","Jason","Rihanna","Beyonce","CardiB","Kehlani")
print(people)
print (people[3])
print(people[1:-2])
person=("LilMaina",)
people+=person
print(people)
# converting the tuple to a list
celebrities=list(people)
celebrities.append("QueenLatifa")
celebrities.extend(["a","b","c"])
print (celebrities)
# list back to a tuple
people=tuple(celebrities)
print(people)