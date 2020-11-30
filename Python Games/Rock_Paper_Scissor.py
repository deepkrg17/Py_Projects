from random import choice
print("  -: Welcome to Rock  //  Paper  // Scissor :-")
i = 0
c = 0
p = 0
def win():
	global p
	p+=1
	print(f"Computer={comp} : You win.😊")
def lose():
	global c
	c+=1
	print(f"Computer={comp}: You lose.😐")
while(i<10):
	prs = ["Paper", "Rock", "Scissor"]
	comp = choice(prs)
	di = {"r":"Rock", "p":"Paper", "s":"Scissor"}
	player = input("\nEnter r for Rock, p for Paper, s for Scissor: ")
	if player!="r" and player!="p" and player!="s":
		print("Enter a valid input.❌")
	elif di[player] == comp:
		print("Tie!🛡️")
	elif player=="r":
		if comp=="Paper":
			lose()
		if comp=="Scissor":
			win()
	elif player=="p":
		if comp=="Rock":
			win()
		if comp=="Scissor":
			lose()
	elif player=="s":
		if comp=="Paper":
			win()
		if comp=="Rock":
			lose()
	i+=1
print(f"\nAfter 10 rounds: Computer = {c}\n                          You = {p}")
if p>c: print("You Win.🤩")
elif p<c: print("Computer Wins.☹️")
else: print("Draw...👍")