import random
import tkinter

stats = []


def get_winner(call):
    if random.random() <= (1 / 3):
        throw = "rock"
    elif (1 / 3) < random.random() <= (2 / 3):
        throw = "scissor"
    else:
        throw = "paper"

        if (throw == "rock" and call == "paper") or (throw == "paper" and call == "scissor") \
                or (throw == "scissor" and call == "rock"):
            stats.append('W')
            result = "You won!"
        elif throw == call:
            stats.append('D')
            result = "It's a draw"
        else:
            stats.append('L')
            result = "You lost!"

            global output
            output.config(text="computer did: " + throw + "\n" + result)

            def pass_s():
                get_winner("scissor")

                def pass_r():
                    get_winner("rock")

                    def pass_p():
                        get_winner("paper")


window = tkinter.Tk()

scissor = tkinter.Button(window, text="scissor", bg="#ff9999", padx=10, pady=5, command="pass_s", width=20)
rock = tkinter.Button(window, text="rock", bg="#80ff80", padx=10, pady=5, command="pass_r", width=20)
paper = tkinter.Button(window, text="paper", bg="#3399ff", padx=10, pady=5, command="pass_p", width=20)
output = tkinter.Button(window, text="rock", width=20, fg="red", command="what's your call?")
scissor.pack(side="left")
rock.pack(side="left")
paper.pack(side="left")
output.pack(side="right")
window.mainloop()

for i in stats:
    print('i', end=" ")
if stats.count('L') > stats.count('W'):
    result = "\nYou loose the series."
elif stats.count('L') == stats.count('W'):
    result = "\nSeries ended in a draw."
else:
    result = "\nYou win the series."

print(result)
