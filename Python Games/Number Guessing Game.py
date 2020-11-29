import random
a = random.randint(1, 100)
i = 10
while(i!=0):
	print("You have", i , "guesses")
	b = int(input("Enter a number between 1 &100:    "))
	if b>a:
		print("\nLower Number please.")
		i-= 1
		continue
	if b<a:
		print("\nHigher number please.")
		i-= 1
		continue
	else:
		print("\nCongratulations!🤩")
		i-=1
		break
if i==0:
	print("\nSorry. You have spent 10 guesses.☹️The number is", a)
else:
	print("You have guessed it in" , 10-i , "guesses")