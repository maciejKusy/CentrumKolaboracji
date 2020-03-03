import random

openlist = open("words.txt")                    # opening file containing a list of available words
words = (openlist.readlines())                  # creating array of lines - in this case words
words = [c.replace('\n','') for c in words]     # removing '\n' symbol from each item in array
openlist.close()                                # close the file
secretword = random.choice(words)               # selecting a random word from the list

print("The secret word has " + str(len(secretword)) + " letters. \n")     # a clue for the player

def guessword():
  global secretword

  # defining variables:

  counter = 0                           # counter to help control the number of iterations
  max_counter = len(secretword)         # the limit of iterations based on counter
  guesses = list(len(secretword)*"_")   # create a list - empty at first will be populated with guessed letters

  # commencing loop:
  while True:

    ans = input("Do you know the secret word?: \n")     # user input
    if len(ans) > 1:                                    # safeguard against partial word input since we want the user
      if ans == secretword:                             # to input either a single char or the entire word
        print(list(secretword))
        print("You win.\n")
        break
      else:
        print("Sorry, wrong input. Either type in a single letter or the entire word.\n")
    elif ans in secretword:                             # if answer char is indeed a part of the secret word
      for n in range(len(secretword)):                  # a quick loop to determine the index at which the char is
        if ans == secretword[n]:                        # located in the secret word and to put it at analogous
          guesses[n] = str(ans)                         # index in quesses: we want to show the player their
          print("Yes! You got one. \n")                 # partial answer
          partial = "".join([x for x in guesses])       # turning list into string for printing of partial answer
          print(partial)
    else:
      counter += 1                                      # if answer is neither the secret word nor a part of it
      print("Nope, try again. \n")                      # counter + 1 and message
      partial = "".join([x for x in guesses])           # turning list into string for printing of partial answer
      print(partial)
    if counter >= max_counter:                          # loop termination if counter reaches limit
      print("No more tries. Better luck next time.\n")
      break

guessword()

input("Press ENTER to quit.")



