print("Ermit")
while not resp = "games" or "movies" or "music":
  resp = input("What do you want to look at today?")
  if resp == "games":
    print("Browse games...")
  elif resp == "movies":
    print("Browse movies...")
  elif resp == "music":
    print("Browse music...")
  else:
    print("Could not find that. Please try again!")
quit()
