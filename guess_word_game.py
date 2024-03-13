#Intro
print ("Welcome To The Word Game!")

#Asking Player 1 to input the word to be guessed.
print ("Player 1 please enter the secret word")
secret_word = input("Secret Word:")

#Now we present the secret word to Player 2 and a hint.
print("Player 2, you must guess the secret word")
print("The world length is " + str(len(secret_word)))

#Player 2 guesses one letter, first try
guess = input("Player 2, enter a letter: ")
n = secret_word.count(guess)
print("Letter "+ guess + ":count: " + str(n))

#Player 2 guesses another letter, second try
guess = input ("Player 2, enter a second letter: ")
n = secret_word.count(guess)
print("Letter " + guess + ": count: " + str(n))

#Player 2 guesses another letter, third try
guess = input("Player 2, enter a letter: ")
n = secret_word.count(guess)
print("Letter " + guess + ": count: " + str(n))

#Player 2 guess a word
guess_word = input ("Player 2, enter a word: ")
if secret_word == guess_word:
    print("Player 2 wins!")
else:
    print("Player 1 wins!")

#end of game