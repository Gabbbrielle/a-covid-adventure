go2walk = """\nGood choice, walking is good for you if you are able to. While walking, minding your own business, you see a group of people walking towards you.\nThey take a lot of space…and they’re not wearing masks.\n\nDo you keep walking towards them, make room for them to pass or cross the street to avoid them (type keep walking, make room or cross street).\n"""
zombieWalkers = """\nwell that didn't go well! As they get closer, they smell your brain and eat it. You're last thought before turning into a zombie is to question your life choices."""
walk = set(["walk", "Walk", "walking"])
cross = set(["cross the street", "cross", "cross street"])
keepWalking = set(["keep walking", "walk", "keep going"])
makeRoom = set(["make room", "Make room"])
def walkingFunc():
  choice = input(go2walk)
  if choice in makeRoom:
    print("""\nsmart choice. Always a good idea to keep a 2 meter distance between you and others, including while walking.\n""")
  elif choice in cross:
    print("\nsmart choice. You keep walking")
  elif choice in keepWalking:
    print(zombieWalkers)
    exit("like you....")
  else:
    print("\n*******************\nNot really a option in this game so a wild unicorn runs you over and your last thought is 'I knew they exist!'\n*******************\n")
    exit("like you...")
    