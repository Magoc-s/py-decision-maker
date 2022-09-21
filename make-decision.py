#!/usr/bin/env python3
import sys
import random
from termcolor import colored, cprint
import time

if (len(sys.argv) == 1):
    print(f"Usage: {sys.argv[0]} [number of choices] choices")
    print("I.e.:")
    print(f"{sys.argv[0]} pizza pasta \"take out\" <--- picks 1 of the three options implicitly ")
    print(f"{sys.argv[0]} 3 olives fetta \"iceburg lettuce\" \"cos lettuce\" \"red capsicum\" chives <--- picks 3 of the 6 options")
    exit(0)

def load_choices(start_idx: int):
    opts = []
    for i in range(start_idx, len(sys.argv)):
        if not sys.argv[i].isalnum():
            print(f"Error: {sys.argv[i]} is not a valid argument.")
            exit(1)
        opts.append(sys.argv[i])
    return opts
    
def main():
    
    cprint("┌────────────────────────────┐", "green")
    cprint("│ Py Decision Maker v0.0.02a │", "green")
    cprint("└────────────────────────────┘", "green")
    num_choices = 1
    prov_options = []
    chosen_options = []
    if (sys.argv[1].isdecimal()):
        if (int(sys.argv[1]) <= 0 or int(sys.argv[1]) > len(sys.argv) - 2):
            print(f"Error: {sys.argv[1]} is not a valid number of choices to make.")
            exit(1)
        num_choices = int(sys.argv[1])
        prov_options = load_choices(2)
    else:
        prov_options = load_choices(1)
    #       │ Decisions:
    string = ""
    input_len = 1
    if num_choices > 1:
        inject = ", ".join(random.choices(population=prov_options,k=num_choices))
        string = "│ Decisions: " + inject + " │"
        input_len = len(string) - 2
    else:
        chosen = random.choice(prov_options)
        string = "│  Decision: " + chosen + " │"
        input_len = len(string) - 2

    cprint("┌" + "─"*input_len + "┐", "yellow")
    cprint(string, "yellow", attrs=["bold"])
    cprint("└" + "─"*input_len + "┘", "yellow")

if __name__ == "__main__":
    main()