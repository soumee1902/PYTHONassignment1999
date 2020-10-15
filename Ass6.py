#5.1
pizza=["veggie forest","peperoni","farmhouse","cheese","onion"]
for x in pizza:
    print("I want to have a: "+x)
    print("I like "+x+"\n")
    print("i love pizza as anything, i crave for pizza's quite often\n"+pizza[0]+", "+pizza[1]+", "+pizza[2]+" is always my fav\n"+pizza[3]+", "+pizza[4]+"is not that favourite ")
print("I JUST LOVE PIZZA")

#5.2
animal=["dog","cat","cow","goat"]
for y in animal:
    print("A "+y+" will make a great pet\n")
    print(y+" they all have four legs")
print(animal[0]+", "+animal[2]+", "+animal[3]+"one would make a great pet!")

#5.3
for x in range(1,21):
    print(x)

#5.4
numbers=list(range(1,100000001))
for y in numbers:
    print(y)

    
#5.5
summ=list(range(1,10000001))
print(min(summ))
print(max(summ))
print(sum(summ))

#5.6
odds=list(range(1,20,2))
for x in odds:
    print(x)

#5.7
threes=list(range(3,31))
for x in threes:
    if x%3==0:
        print(x)

#5.8
cubes=list(range(1,11))
for x in cubes:
    print(x**3)

#5.9
cube=[value**3 for value in range(1,21)]
print(cube)

#5.10
animal=["dog","cat","cow","goat","rat","bird"]
x=slice(0,3)
print("The first three elements of the list are: "+str(animal[x]))
print("\n")
x=slice(2,5)
print("The items from the middle of the list are: "+str(animal[x]))
print("\n")
x=slice(3,6)
print("The last items in the list are: "+str(animal[x]))


#5.11
pizza=["veggie forest","peperoni","farmhouse","cheese","onion"]
friend_pizzas=["veggie forest","peperoni","farmhouse","cheese","onion","chicken pizza"]
for x in pizza:
    print("My favourite pizza are: "+x)
for y in friend_pizzas:
    print("My friend's favourite pizza are: "+y)

