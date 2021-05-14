import pyfiglet
from termcolor import colored
import os
import argparse

parser = argparse.ArgumentParser(description = "This program helps to estimate expected value of football betting.")
parser.add_argument("-v", action = "version", version = "Oddsmaker 1.0")
msg = parser.parse_args()

os.system("clear")

global bookie_odds
global bookie_probs 
global my_odds
global my_probs 
global diff_odds
global profit
      
def results():

    print("*" * 80)
    title = "ODDs Comparision"
    print(title.center(80))
    print("")
    print("*" * 80)

    print("=" * 80) 
    txt1 = "Bookie Odd: {:.2f} or {:.2f}%".format(bookie_odds,bookie_probs)
    print(txt1.center(80)) 
    print("-" * 80)
    txt2 = "My Odd: {:.2f} or {:.2f}%".format(my_odds,my_probs) 
    print(txt2.center(80))
    print("-" * 80)

    if (diff_odds > 0):
        txt3 = "Positive Expected Value: +{:.2f}% (profit)".format(profit) 
        print(colored(txt3.center(80), "green"))
    elif (diff_odds == 0):
        txt4 = "Null Expected Value: {:.2f}% (breakeven)".format(profit) 
        print(colored(txt4.center(80), "yellow"))
    else:
        txt5 = "Negative Expected Value: {:.2f}% (loss)".format(profit) 
        print(colored(txt5.center(80), "red"))  
    
    print("-" * 80)

while True:

    try:
        print("=" * 80)        
        intro = pyfiglet.figlet_format("Football Betting")
        print(intro)
        print("=" * 80)
        print("Use decimal point (.) instead of decimal comma (,)".center(80))
        print("=" * 80)
        bookie_odds = float(input("Bookmaker Odd (decimal): "))
        bookie_probs = float(100/bookie_odds) #Convert to implied probabilities (0.00%)
        my_probs = float(input("Your Estimated Probabilities (%): "))
        my_odds = float(100/my_probs) #Convert to decimal odds (1.00)
        diff_odds = (bookie_odds - my_odds)
        profit = (diff_odds * 100)
        os.system("clear")
        results()        

        question = str(input("Want to continue? [y,n]: ")).lower()            
        os.system("clear")                        

        if (question == "n"):
            print("-" * 80)
            print("Finished... Good luck!".center(80))
            print("-" * 80)
            exit()                
        elif (question != "y"):
            print("=" * 80)    
            print("Type 'y' for YES or 'n' for NO (in the last question)...".center(80))
            print("=" * 80)    
            question = str(input("Want to continue? [y,n]: ")).lower()
            if (question == "n"):
                print("-" * 80)
                print("Finished... Good luck!".center(80))
                print("-" * 80)
                exit()
            elif (question != "y"):
                print("-" * 80)
                print("Try again".center(80))
                print("-" * 80)
                exit()         

    except ValueError:
        os.system("clear")
