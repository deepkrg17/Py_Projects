import random

a = random.randint(1, 100)
i = 10
while i != 0:
	# pylint: disable=bad-indentation
	print(f"You have {i} guesses")
	b = int(input("\nEnter a number between 1 & 100:    "))
	if b>a:
		print("\nLower Number please.")
		i -= 1
	elif b<a:
		print("\nHigher number please.")
		i -= 1
	else:
		print("\nCongratulations!🤩")
		i-=1
		print(f"You have guessed it in {10-i} guesses.")
		break
	if i==0:
		print(f"\nSorry. You have spent 10 guesses.☹️ The number is {a}.")
