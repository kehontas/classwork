#rps
#should ask for input
#should ask for done?
#should detect a winner
#keep track of the wins




import random 

computer = random.choice(["rock", "paper", "scissors"])

player1 = raw_input("Your Move: ")

print "Computer played: " + computer 



if player1 == computer:
	print "You tied"

elif player1 == "rock"and computer  == "scissors":  
  print "player1 wins"

elif player1 == "paper" and computer == "rock":
  print "player1 wins"

elif player1  == "scissors" and computer  == "paper": 
  print "player1 wins"

else:
  print "computer wins"