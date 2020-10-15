#invitations for the dinner
name=["ravi","rahul","rony"]
for x in name:
    print("you're invited for dinner "+x)

#inviting some others for the dinner
name.append("sonu")
name.append("preety")
name.append("diya")
for y in name:
    print("you're invited for dinner "+y)

#guest who cant make it to the dinner
removed_guests=name.pop(1)
print("the one who cant make it to the dinner "+removed_guests)
removed_guests=name.pop(2)
print("the one who cant make it to the dinner "+removed_guests)
removed_guests=name.pop(3)
print("the one who cant make it to the dinner "+removed_guests)

#replacing the members who are comming with the one who are not





#second set of invitations
for z in name:
    print("do come for the dinner "+z)

#4.3 3 more guests
name.insert(0,"pallavi")
name.insert(4,"vaisho")
name.append("bittu")
print(name)
for a in name:
    print("the table is now bigger "+a)
    
#4.4 print a message 
message="we can only invite two people for dinner"
print(message)
print("sorry we cant invite you for dinner "+name.pop(0),name.pop(1),name.pop(2))
for s in name:
    print("you are still invited for thr dinner "+s)
rr=name[2]
del name[0]
del name[1]
print("empty list "+rr)



#4.5
#places i want to visit
places=["delhi","mumbai","london","california","ooty","assam","saudi arab","mexico","italy"]
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
print(sorted(places))
print(sorted(places, reverse=True))




