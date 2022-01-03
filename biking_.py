yes_answer = set(["y", "yes", "Yes", "Y", "Yup", "yup"])
no_answer = set(["n", "N","no", "No", "nope", "Nope"])
biking = set(["biking", "bike", "take my bike"])
public = set(["public transportation", "metro", "bus", "take the bus", "take the metro", "public transport"])
walk = set(["walk", "Walk", "walking"])
import walking
import wbk
def bikingFunc():
  choice = input("\nhave your lock? y/n \n")
  if choice in yes_answer:
    wbk.doing(1,2,2)
    print("\ngood person! You get to your destination and you can feel safe that your bike won't be stolen\n")
  else:
    back = input("\nBike stolen! walk or public transport back?\n")
    if back in walk:
      walking.walkingFunc()
    elif back in public:
      import publicTransport
      publicTransport.public()
    else:
      print("Not a choice in this game. You get crushed by the GhostBuster mashmallow man and die happy with the sweet taste of is candy foot")
      exit()