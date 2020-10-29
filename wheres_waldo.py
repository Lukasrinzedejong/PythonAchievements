import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

count=0
for x in people:
    count +=1
    print(x)
    if x == "Waldo":
        print("Waldo is on seat number ", + count)
        print(people)
        break

    
