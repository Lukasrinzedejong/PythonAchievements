
import time
import sys
while True:
    print("You wake up at 6 am. You need to get out at 7. Do you you start your day EARLY, or do you go BACK TO SLEEP?")

    choice1 = input()

    if choice1 == 'EARLY':
          print("You start your day a little tired, but you easily get up and even have time for watching some television.")
    elif choice1 == 'BACK TO SLEEP':
        print("You fall asleep again, only to wake up at 8 am. You missed your train.")
    else:
        print(choice1, " is not a valuable option.")

    print(                         )
    print("You go downstairs to get some breakfast, but there is no more bread. Do you grab a BANANA, or get some YOGHURT?")

    choice2 = input()

    if choice2 == 'BANANA':
        print("You grab a banana and head to the station, but while cycling to the station, you get hungry again.")
    elif choice2 == 'YOGHURT':
        print("You get a bowl and fill it with cereal. You then open the fridge to find your family ate all the yoghurt already.")
    else:
        print(choice2, "is not a valuable option.")

    print(                         )
    print("You arrived at your destination. You walk past a small shop that sells alot of tasty things. Do you go in and BUY DONUTS, or do you WALK PAST and head to school?")

    choice3 = input()

    if choice3 == 'BUY DONUTS':
        print("You go to buy the donuts, but your card declines. oh no!")

    elif choice3 == 'WALK PAST':
        print("You get to school early and are able to get your favorite place in the classroom.")

    else:
        print(choice3, "is not a valuable option.")
        
    print(                         )
    print("While cycling back home, you want to listen to some music. do you turn it up super LOUD, or do you leave it QUIET, barely hearing it but hearing the traffic?")

    choice4 = input()

    if choice4 == 'LOUD':
        print("What did you awnser, i cannot hear you!!")
    elif choice4 == 'QUIET':
        print("You do not hear the music well, but you do hear oncoming traffic, giving you a safe trip back home.")
    else:
        print(choice4, "is not a valuable option")

    print(                         )
    print("You arrive back home. Do you MAKE HOMEWORK, or are you going to play VIDEOGAMES?")

    choice5 = input()

    if choice5 == 'MAKE HOMEWORK':
        print("You finish your homework just in time for dinner, but all your friends are now offline. You will have to play alone.")
    elif choice5 == 'VIDEOGAMES':
        print("You play games with your friends for hours, but forget about your homework. In the middle of the night you wake up realizing you forgot your homework.")
    else:
        print(choice5, "is not a valuable option")

    print(                         ) 


    time.sleep(3.5)
    words = "..."
    for char in words:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(                         )
    time.sleep(3.5)
    words = "..."
    for char in words:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(                         )
    time.sleep(3.5)
    words = "Simulation Complete"
    for char in words:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(                     )
    time.sleep(0.5)
    words = "Rebooting Program in:"
    for char in words:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(                        )
    
    time.sleep(1)
    words = "3     2     1     0"
    for char in words:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    print( )
    print( )
    print( )
    print( )
    print( )
    print( )
    print( )
    print( )
    print( )
    







    
    



