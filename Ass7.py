#8.1
name={'first_name': 'Pallavi',
'last_name': 'Prajakta',
'age': '22',
'city': 'Ranchi'}
print(name['first_name'])
print(name['last_name'])
print(name['age'])
print(name['city'])

#8.2
fav_name={'Pallavi': '13',
'Vaisho': '21',
'Neeladri': '24',
'Soumyashree': '19',
'Sumonto':'4'}
print("Pallavi: "+fav_name['Pallavi'])
print("Vaisho: "+fav_name['Vaisho'])
print("Neeladri: " +fav_name['Neeladri'])
print("Soumyashree: "+fav_name['Soumyashree'])
print("Sumonto: "+fav_name['Sumonto'])

#8.3
glossary={'List': 'A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements',
'Tuple': 'A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.',
'Dictionary': 'A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.',
'for loop': 'Looping statement',
'String': 'A string in Python is a sequence of characters.'}
print("List: "+glossary['List']+"\n")
print("Tuple: "+glossary['Tuple']+"\n")
print("Dictionary: "+glossary['Dictionary']+"\n")
print("for loop: "+glossary['for loop']+"\n")
print("String: "+glossary['String']+"\n")

#8.4
glossary={'List': 'A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements',
'Tuple': 'A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.',
'Dictionary': 'A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.',
'for loop': 'Looping statement',
'String': 'A string in Python is a sequence of characters.',
'Data types': 'It is a type of data used of a variable',
'python': 'its a programming language',
'Java': 'Its an OOP Language',
'C': 'Its a basic programming language',
'Ruby': 'Its a outdated programmig language'}
for  keyprop,valueprop in glossary.items():
    print("key: "+keyprop.title()+"\ndefinition: "+valueprop+"\n")

#8.5
rivers={'Nile': 'Egypt',
'Damodar': 'India',
'Brahmaputra': 'Nepal'}
for river,countries in rivers.items():
    print(river.title()+" flows through the country "+countries+"\n")
for river in rivers.keys():
    print(river.title())
print("\n")
for countries in rivers.values():
    print(countries)

#8.6
fav_lang={'Pallavi': 'C',
'Vaisho': 'Ruby',
'Neeladri': 'Java',
'Soumyashree': 'Java',
'Sumonto':'Python'}
for names,lang in fav_lang.items():
    print(names.title()+"'s favourite language is: "+lang)
print("\n")
namepoll=['Harry','rohn','peter','mike','steve','chris','Pallavi','Vaisho','Neeladri','Soumyashree','Sumonto']
for name in namepoll:
    if name in fav_lang.keys():
        print(name+" you are in the poll")
    else:
        print(name.title()+" your fav language is?")


#8.7
people = []
person={'first_name': 'Pallavi',
'last_name': 'Prajakta',
'age': '22',
'city': 'Ranchi'}
people.append(person)

person={'first_name': 'Soumyashree',
'last_name': 'Goswami',
'age': '21',
'city': 'Asansol'}
people.append(person)

person={'first_name': 'Sumonto',
'last_name': 'Chatterjee',
'age': '22',
'city': 'Chaibasa'}
people.append(person)
 
#for name in people:






#8.8
pets = []
doggo={'animal': 'dog',
'owner': 'Kate'}
pets.append(doggo)
brain={'animal': 'Cat',
'owner': 'John'}
pets.append(brain)
fatty={'animal': 'rabbit',
'owner': 'Rony'}
pets.append(fatty)

# for name in pets:
#     print(name.title()+"pet details are as follows")
#     for animal in 

    









