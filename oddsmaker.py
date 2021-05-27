import pyfiglet
from termcolor import colored
import argparse
import os
import sys

parser = argparse.ArgumentParser(description = "This program helps to estimate expected value in football betting.")
parser.add_argument("-v", action = "version", version = "Oddsmaker 1.0")
msg = parser.parse_args()

os.system("clear")

global back_odds, back_probs, lay_odds, lay_probs, my_odds, my_probs, diff_odds, odds_sum, margin, fair_back_probs, fair_lay_probs, fair_back, fair_lay

def results():

    print("*" * 80)
    title = "ODDs Comparision"
    print(title.center(80))
    print("")
    print("*" * 80)
    print("=" * 80)
    fair = "Fair Odds"
    print(colored(fair.center(80), "white", "on_blue")) 
    print("=" * 80)    
    print(f"Back: @{fair_back:.2f} or {fair_back_probs:.2%} | Lay: @{fair_lay:.2f} or {fair_lay_probs:.2%}".center(80))
    print("-" * 80)    
    print(f"Bookie Margin: {margin:.2%}".center(80))
    print("=" * 80)  
    odd = "My Odd (in Back)"  
    print(colored(odd.center(80), "white", "on_blue"))
    print("=" * 80)
    print(f"@{my_odds:.2f} or {my_probs:.2f}%".center(80))
    print("-" * 80)

    if (diff_odds > 0):
        result_3 = "Positive Expected Value: +{:.2%} (profit)".format(diff_odds) 
        print(colored(result_3.center(80), "green"))
    elif (diff_odds == 0):
        result_4 = "Null Expected Value: {:.2%} (breakeven)".format(diff_odds) 
        print(colored(result_4.center(80), "yellow"))
    else:
        result_5 = "Negative Expected Value: {:.2%} (loss)".format(diff_odds) 
        print(colored(result_5.center(80), "red"))  
    
    print("-" * 80)
 
try:    

    while True:

        try:
            print("=" * 80)        
            intro = pyfiglet.figlet_format(" Oddsmaker 1.0")
            print(intro)
            print("=" * 80)        
            print("A football betting App CLI".center(80))
            print("Use decimal point (.) instead of decimal comma (,)".center(80))
            print("=" * 80)
            print("For exit, type: CTRL + C".center(80))
            print("=" * 80)            

            back_odds = float(input(" Back Bookmaker Odd: "))
            back_probs = float(1/back_odds) 
            lay_odds = float(input(" Lay Bookmaker Odd: "))
            lay_probs = float(1/lay_odds)
            my_probs = float(input(" Your Implied Probabilities (%): "))       

            my_odds = float(100/my_probs)               
            odds_sum = float(back_probs + lay_probs)
            margin = float(odds_sum - 1)
            fair_back_probs = float(back_probs - (margin/2))  
            fair_lay_probs = float(lay_probs - (margin/2))        
            fair_back = float(1/fair_back_probs)
            fair_lay = float(1/fair_lay_probs)
            diff_odds = (fair_back - my_odds)              

            os.system("clear")
            results()
            question = str(input(" Want to continue? [y,n]: ")).lower()            
            os.system("clear")                        

            if (question == "n"):
                print("-" * 80)
                final_1 = "Finished... Good luck!"
                print(colored(final_1.center(80), "blue", "on_green"))
                print("-" * 80)
                exit()                
            elif (question != "y"):
                print("=" * 80)
                msg = "Type 'y' for YES or 'n' for NO (in the last question)..."    
                print(colored(msg.center(80), "white", "on_red"))
                print("=" * 80)    
                question = str(input(" Want to continue? [y,n]: ")).lower()
                os.system("clear")
                if (question == "n"):
                    print("-" * 80)
                    final_2 = "Finished... Good luck!"
                    print(colored(final_2.center(80), "blue", "on_green"))
                    print("-" * 80)
                    exit()
                elif (question != "y"):
                    while (question != "y"):
                        os.system("clear")
                        print("=" * 80)
                        terminate = "Try again!"
                        print(colored(terminate.center(80), "blue", "on_green"))
                        print("=" * 80)
                        question = str(input("Want to continue? [y/n]: ")).lower()                    
                        os.system("clear")
                        if (question == "n"):                            
                            print("-" * 80)
                            final_2 = "Finished... Good luck!"
                            print(colored(final_2.center(80), "blue", "on_green"))
                            print("-" * 80)
                            exit()                

        except ValueError:
            os.system("clear")

except KeyboardInterrupt:
    os.system("clear")
    sys.exit(0)