import random
def com_choice():
    return random.choice(["rock","paper","scissor"])

def get_winner(user,computer):
    if user == computer:
        return "draw"
    win={"rock":"scissor", "paper": "rock", "scissor": "paper"}
    if win[user] ==computer:
        return "user"
    return "computer"

def play():
    you=0
    cpu=0
    draw=0
    print("== ROCK PAPER SCISSOR ==")
    print("Type 'quit' to exit")
    while True:
        user_input=input("Enter your choice (rock/paper/scissor):").lower().strip()
        if user_input =="quit":
            break
        if user_input not in ["rock","paper","scissor"]:
            print("Invalid choice ! Try again\n")
            continue

        computer_input=com_choice()
        print(f"Computer choice:{computer_input}")
        result=get_winner(user_input,computer_input)

        if(result=="draw"):
            draw+=1
            print("It is draw!\n")
        elif(result=="user"):
            you+=1
            print("Ypu win\n")
        else:
            cpu+=1
            print("Computer win\n")

        print(f"Score -> You:{you} | Computer:{cpu} | Draws:{draw}\n")

    print(f"\n===Final Score===")
    print(f"You:{you} |Computer:{cpu} |Draws:{draw}")

play()
