people = ['mike','may','king']
popped_guest = people.pop()
people.append('john')
people.insert(0,'white')
people.insert(2,'black')
people.append('green')
message1 = "I can't invite you"
message2 = "I would invite you to have a dinner together"
print(f"{popped_guest.title()} can't come")
popped_guest = people.pop()
print(f"Sorry {popped_guest.title()},{message1}")
popped_guest = people.pop()
print(f"Sorry {popped_guest.title()},{message1}")
popped_guest = people.pop()
print(f"Sorry {popped_guest.title()},{message1}")
popped_guest = people.pop()
print(f"Sorry {popped_guest.title()},{message1}")
print(f"{people[0].title()},{message2}")
print(f"{people[1].title()},{message2}")
del people[1]
del people[0]
print(people)