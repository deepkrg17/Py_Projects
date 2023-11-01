from random import choice

print("-: Welcome to Rock  //  Paper  // Scissor :-".center(70))

# pylint: disable-next=invalid-name
c = p = 0

for _ in range(10):
    # pylint: disable=bad-indentation
	prs = ["Paper", "Rock", "Scissor"]
	comp = choice(prs)
	di = {"r":"Rock", "p":"Paper", "s":"Scissor"}
	player = input("\nEnter r for Rock, p for Paper, s for Scissor: ")
	if not player or player not in "rps":
		print("Enter a valid input.❌")
	elif di[player] == comp:
		print("Tie!🛡️")
	else:
		match [player, comp]:
			case ['r','Scissor'] | ['p','Rock'] | ['s','Paper']:
				p+=1
				print(f"Computer => {comp} : You win.😊")
			case ['r','Paper'] | ['p','Scissor'] | ['s','Rock']:
				c+=1
				print(f"Computer => {comp} : You lose.😐")

print(f"""
	After 10 rounds: Computer = {c}
	                 You = {p}
	""")

if p>c: print("\tYou Win.🤩")
elif p<c: print("\tComputer Wins.☹")
else: print("\tDraw...👍")
