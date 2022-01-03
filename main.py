print('''
                    /
               ,.. /
             ,'   ';
  ,,.__    _,' /';  .
 :','  ~~~~    '. '~
:' (   )         )::,
'. '. .=----=..-~  .;' 
 '  ;'  ::   ':.  '"
   (:   ':    ;)
    \\   '"  ./
     '"      '"
               art by DR J \n ''')
print("for a good experience, make sure the file and the code window are hidden.\n")
beging = input("welcome to 2020 - a covid adventure.\nReady to play? type 'y'\n")
yes_answer = set(["y", "yes", "Yes", "Y", "Yup", "yup"])
no_answer = set(["n", "N","no", "No", "nope", "Nope"])
walk = set(["walk", "Walk", "walking"])
biking = set(["biking", "bike", "take my bike"])
public = set(["public transportation", "metro", "bus", "take the bus", "take the metro", "public transport"])
grocery = set(["grocery", "Grocery", "shopping"])
work = set(["work", "Work"])
import time

where2go = """\nYou’ve been at home for a while and now it’s time to get out of the house. You get out of your pjs, get dress, put your mask on (‘cause you’re awesome!) and leave the house. Are you going out to work, to do grocery, or for a walk (type work, grocery or walk). \n"""

go2walk = """\nGood choice, walking is good for you if you are able to. While walking, minding your own business, you see a group of people walking towards you.\nThey take a lot of space…and they’re not wearing masks.\nDo you keep walking towards them, make room for them to pass or cross the street to avoid them (type keep walking, make room or cross street).\n """
zombieWalkers = """\nwell that didn't go well! As they get closer, they smell your brain and eat it. You're last thought before turning into a zombie is to question your life choices."""
go2Grocery = """\nDelivery is fun but there is no reason not to go out to get what we need if we are careful right?\nAre you walking there, taking public transportation or taking your bike there? (type walking, public transportation or bike). \n"""
atTheGrocery = """"\nYou're at the grocery and get all you need for the week (pandemic and all, going once a week only is a good idea). You go back home the same way you came and live happely ever after \n"""
go2work = """\nSo many reason why you would work out there in the world!\nIf you are a frontline worker, know that you are awesome and appreciated.\nRegardless of your reasons, are you walking there, taking public transportation or taking your bike there? (type walking, public transportation or bike).\n"""

if beging in yes_answer:
  ready = input("Your mission is to survive a trip outside your house. Are you ready? \n")
  if ready in yes_answer:
    print("\ncooool. cool cool cool. Let's go!\n")
   
    import walking
    where = input(where2go)
    if where in walk:
      walking.walkingFunc()
      backhome = input("ready to go back home? ")
      if backhome in yes_answer:
        print("well that was a nice walk right? And you dinna even die or anything. ")
      elif backhome in no_answer:
        what2do = input("Do you want to stop at the grocery store while your at it? ")
        if what2do in yes_answer:
          walking.walkingFunc()
          print("You get to the store all good and with all that experience, you get back home in one piece. Yippee!!")
        else:
          print("ya, no. No time to fool around buddy. Go back home and enjoy the rest of your day")
      else:
        print("That's not really a choice now is it. That foolish choice will be rewarded with a encounter with the  ")
  # walk tested and functional
    elif where in grocery:
      how = input(go2Grocery)
      if how in walk:
        walking.walkingFunc()
        print("\n*********************\nYou go to the grocery store and come back home happy with food and snacks for the next week. Way to go!\n*************")  
  # walking to the grocery store tested and functional
      elif how in biking:
        import biking_
        biking_.bikingFunc()
        print("\n*******************\nDo the grocery by bike is fun stuff biking huh? Glad you had a bit of exercise.\nCome back another time to play again\n*******************\n")
  # biking to the grocery store tested and functional
      elif how in public:
        import publicTransport
        publicTransport.publicFunc()
        howBack = input("You got all that you need for the week. Going back home the same way?\n")
        if howBack in yes_answer:
          publicTransport.publicFunc()
          print("\n*******************\nThat was fun. A bit scary to take public transportation in these covid time but you did it!\n*******************\n ")
        elif howBack in no_answer:
            choice = input("cool to move things around. I reckon you'll be walking?\n")
            if choice in yes_answer:
              walking.walkingFunc()
              print("\n*******************\nyou get home safe and sound\n*******************\n")
        else:
            print("""\n*******************\nNot a choice in this game. You get crushed by the GhostBuster mashmallow man and die happy with the sweet taste of is candy foot\n*******************\n""")
            print("Like you...")
            exit()
  # public transport to the grocery store tested and functional 
      else:
          print("""\n*******************\nNot a choice in this game. You get crushed by the GhostBuster mashmallow man and die happy with the sweet taste of is candy foot\n*******************\n""")
          print("Like you...")
          exit()

    elif where in work:
      how = input(go2work)
  # walking to work tested and functional
      if how in walk:
          walking.walkingFunc()
          print("\n*******************\nYou get to work after a nice walk and are ready for a good day of work!\n*******************\n")
          print("\n**HOURS LATER...**\n")
          how_back = input("\nWhat a day!\nSo...\nwhat's your plan to get back? Walk or take the bus?\n")
          if how_back in walk:
            walking.walkingFunc()
            print("\n*******************\nGood job today! I'm really proud of you. \nWork AND exercise...you really rock it. Come and play again anytime\n*******************\n")
          elif how_back in public:
            import publicTransport
            publicTransport.publicFunc()
            print("\n*******************\nWhat a day! I'm really proud of you. \nYou did a full day of work aaaaand you navigated public transit. Hope you have a super nice evening. \nCome and play again anytime\n*******************\n")
  #biking to work tested and functional 
      elif how in biking:
        import biking_
        biking_.bikingFunc()
        time.sleep(2)
        print("\n**HOURS LATER...**\n")
        ready_back = input("\nWhat a day!\nSo...\nReady to get back?\n")
        if ready_back in yes_answer:
          import wbk
          wbk.doing(2,3,4)
          print("\n*******************\nGood job today! I'm really proud of you. \nWork AND exercise...you really rock it. Come and play again anytime\n*******************\n")
        elif ready_back in no_answer:
          what2do = input("Do you want to stop at the grocery store while your at it? ")
          if what2do in yes_answer:
            print("Good idea")
            time.sleep(1)
            biking_.bikingFunc()
            print("You get to the store all good and with all that experience, you get back home in one piece. Yippee!!")
          else:
            print("ya, no. No time to fool around buddy. Go back home and enjoy the rest of your day")
        else:
          print("Nope. Not a time to do other stuff buddy. Go back home and come back another time to play again")
      elif how in public:
        import publicTransport
        publicTransport.publicFunc()
        print("\n*******************\nGood job today! I'm really proud of you. \nWork AND navigating the public transport system...you really rock it. Come and play again anytime\n*******************\n")
    else:
      print("We's in a pandemic and you're living in a red zone so ya, those should be your only option. While trying to do something else, you get injected with 5g and become a super human with free internet connection and change the world into a utopian equalitarian society. Good job!")
      exit()
  else:
    print("super legitimate. Come back later or just enjoy the rest of your day. No harm done. ")
else:
  print("well that's awkward. Me I thought we were friends")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload