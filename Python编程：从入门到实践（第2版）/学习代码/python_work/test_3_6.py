people = ['mike','may','king']
popped_guest = people.pop()
people.append('john')
people.insert(0,'white')
people.insert(2,'black')
people.append('green')
message = "I would invite you to have a dinner together"
print(f"{popped_guest.title()} can't come")
print(f"{people[0].title()},{message}")
print(f"{people[1].title()},{message}")
print(f"{people[2].title()},{message}")
print(f"{people[3].title()},{message}")
print(f"{people[4].title()},{message}")
print(f"{people[5].title()},{message}")