
def sphere_volume(rad):
  pi = 3.141592
  frac = 1.333333
  vol = round(frac*pi*(float(rad)*float(rad)*float(rad)),2)
  print("\nThe volume of a sphere with a radius of " + str(rad) + "cm is approximately " + str(vol)+ "cm3.\n")

while True:
  radius = input("""Enter the length of radius in cm
or press Q to quit: \n""").lower()
  if radius == "q":
    break
  elif radius.isalpha():
    print("\nSorry, incorrect input. Try again:\n")
    continue
  else:
    sphere_volume(radius)
	
	#CHANGES ADDED TO TEST GIT

  