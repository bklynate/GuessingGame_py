#1. Display instructions on how to play the game
#2. Randomly choose a number between 1 and 10
#3. Have player guess the correct number
#4. If player guesses the wrong number continue to loop until they guess right
#5. Display a 'You Win' if number is correctly guessed
#6. Display a "Try Again" if number is incorrectly guessed
#7. if player guess is wrong, alert player is guess is too high or too low
#8. Player is allowed only 3 guesses


from random import randint

def prompt(words):
	print ("=> {}".format(words))

prompt("I will choose a random number number BETWEEN 1 & 20.")
prompt("You will have only 3 chances to guess correctly.")
prompt("Guess What my number is... ")

correct_number = randint(2,9)
guesses = 0

while guesses < 3:
	player_guess = int(input("=> "))

	if player_guess == correct_number:
		prompt("You Win!")
		break
	elif player_guess != correct_number:
		if player_guess > correct_number:
			prompt("Guess is too high")
			guesses += 1
			continue
		elif player_guess < correct_number:
			prompt("Guess is too low")
			guesses += 1
			continue
		prompt("Guess Again!!")
		continue