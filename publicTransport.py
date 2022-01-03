public = set(["public transportation", "metro", "bus", "take the bus", "take the metro", "public transport"])
yes_answer = set(["y", "yes", "Yes", "Y", "Yup", "yup", "right"])
no_answer = set(["n", "N","no", "No", "nope", "Nope"])
mask = input("You're wearing your mask right? ")
def publicFunc():
  if mask in yes_answer:
    print("Good! You can get in and get to your destination")
    
  else:
    print("\n*******************\nYou're refused access and you need to back home walking. On your way back a zombie bits you and you roam the streets for ever\n*******************\n")
    print("Like you...")
    exit()