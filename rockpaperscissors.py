import random, time

options = ("🪨", "🧻", "✂️")
computerchoice = random.choice(options)
choice = input("Choose one of the three (Rock, Paper, Scissors): ").lower()
if choice == "rock":
    choice = "🪨"
elif choice == "paper":
    choice = "🧻"
elif choice == "scissors":
    choice = "✂️"
else:
    print("Invalid choice")

if computerchoice == choice:
    result = "You tie!"
elif choice == "🪨" and computerchoice == "🧻":
    result = "😭You lose!"
elif choice == "🪨" and computerchoice =="✂️":
    result = "🏆You win!"
elif choice == "🧻" and computerchoice == "✂️":
    result = "😭You lose!"
elif choice == "🧻" and computerchoice == "🪨":
    result = "🏆You win!"
elif choice == "✂️" and computerchoice == "🧻":
    result = "🏆You win!"
elif choice == "✂️" and computerchoice == "🪨":
    result = "😭You lose!"





for i in range(3, 0, -1):
    time.sleep(0.5)
    print(i)
print(f"{choice} VS {computerchoice}")
print(result)


