import numpy as np
from scipy.stats import poisson
import pyfiglet
from termcolor import colored
import argparse
import os
import sys

parser = argparse.ArgumentParser(description = "This program determines the prices of odds in football events.")
parser.add_argument("-v", action = "version", version = "Odd Pricing 1.0")
msg = parser.parse_args()

os.system("clear")

global home_team_goals_for, home_team_goals_against, away_team_goals_for, away_team_goals_against 
global home_league_goals_for, home_league_goals_against, away_league_goals_for, away_league_goals_against

try:

    while True:

        try:

            print("=" * 82)
            intro = pyfiglet.figlet_format(" Odd Pricing 1.0")
            print(intro)
            print("=" * 82)
            print("A football betting App CLI".center(82))
            print("=" * 82)
            print("For exit, type: CTRL + C".center(82))
            print("=" * 82)

            home_team_goals_for = float(input(" Home Team 'Goals For' Average: "))
            home_team_goals_against = float(input(" Home Team 'Goals Against' Average: "))
            away_team_goals_for = float(input(" Away Team 'Goals For' Average: "))
            away_team_goals_against = float(input(" Away Team 'Goals Against' Average: "))
            home_league_goals_for = float(input(" Home League 'Goals For' Average: "))
            home_league_goals_against = float(input(" Home League 'Goals Against' Average: "))
            away_league_goals_for = home_team_goals_against
            away_league_goals_against = home_league_goals_for

            home_attack_strength = (home_team_goals_for / home_league_goals_for)
            home_defense_strength = (home_team_goals_against / home_league_goals_against)
            away_attack_strength = (away_team_goals_for / away_league_goals_for)
            away_defense_strength = (away_team_goals_against / away_league_goals_against)
            home_goals_expectancy = (home_attack_strength * away_defense_strength * home_league_goals_for)
            away_goals_expectancy = (away_attack_strength * home_defense_strength * away_league_goals_for)
            match_goals_expectancy = (home_goals_expectancy + away_goals_expectancy)
            match_goals_expectancy =  round(match_goals_expectancy, 2)            
            
            home_poisson = poisson.pmf(range(7), home_goals_expectancy)
            away_poisson = poisson.pmf(range(7), away_goals_expectancy)

            line0 = home_poisson[0] * away_poisson 
            line1 = home_poisson[1] * away_poisson
            line2 = home_poisson[2] * away_poisson
            line3 = home_poisson[3] * away_poisson
            line4 = home_poisson[4] * away_poisson
            line5 = home_poisson[5] * away_poisson
            line6 = home_poisson[6] * away_poisson

            line0 = (line0 * 100).round(2) 
            line1 = (line1 * 100).round(2)
            line2 = (line2 * 100).round(2) 
            line3 = (line3 * 100).round(2)
            line4 = (line4 * 100).round(2)
            line5 = (line5 * 100).round(2)
            line6 = (line6 * 100).round(2)
            
            os.system("clear")       
            
            under0_5 = (line0[0]).round(2)
            over0_5 = (100 - under0_5).round(2)

            under1_5 = (under0_5 + line1[0] + line0[1]).round(2)
            over1_5 = (100 - under1_5).round(2)

            under2_5 = (under1_5 + line0[2] + line1[1] + line2[0]).round(2)
            over2_5 = (100 - under2_5).round(2)

            under3_5 = (under2_5 + line0[3] + line1[2] + line2[1]).round(2)
            over3_5 = (100 - under3_5).round(2)

            under4_5 = (under3_5 + line0[4] + line1[3] + line2[2] + line3[1] + line4[0]).round(2)
            over4_5 = (100 - under4_5).round(2)

            under5_5 = (under4_5 + line0[5] + line1[4] + line2[3] + line3[2] + line4[1] + line5[0]).round(2)
            over5_5 = (100 - under5_5).round(2)

            under6_5 = (under5_5 + line0[6] + line1[5] + line2[4] + line3[3] + line4[2] + line5[1] + line6[0]).round(2)
            over6_5 = (100 - under6_5).round(2)

            sum0_5 = (over0_5 + under0_5)
            sum0_5 = str(sum0_5) + "%"

            sum1_5 = (over1_5 + under1_5)
            sum1_5 = str(sum1_5) + "%"

            sum2_5 = (over2_5 + under2_5)
            sum2_5 = str(sum2_5) + "%"

            sum3_5 = (over3_5 + under3_5)
            sum3_5 = str(sum3_5) + "%"

            sum4_5 = (over4_5 + under4_5)
            sum4_5 = str(sum4_5) + "%"

            sum5_5 = (over5_5 + under5_5)
            sum5_5 = str(sum5_5) + "%"  

            sum6_5 = (over6_5 + under6_5)
            sum6_5 = str(sum6_5) + "%"  

            odd_u_05 = (100 / under0_5).round(2) 
            odd_o_05 = (100 / over0_5).round(2) 
            under0_5 = str(under0_5) + "%"
            over0_5 = str(over0_5) + "%"     

            odd_u_15 = (100 / under1_5).round(2) 
            odd_o_15 = (100 / over1_5).round(2) 
            under1_5 = str(under1_5) + "%"
            over1_5 = str(over1_5) + "%"  

            odd_u_25 = (100 / under2_5).round(2) 
            odd_o_25 = (100 / over2_5).round(2) 
            under2_5 = str(under2_5) + "%"
            over2_5 = str(over2_5) + "%"    

            odd_u_35 = (100 / under3_5).round(2) 
            odd_o_35 = (100 / over3_5).round(2) 
            under3_5 = str(under3_5) + "%"
            over3_5 = str(over3_5) + "%"     

            odd_u_45 = (100 / under4_5).round(2) 
            odd_o_45 = (100 / over4_5).round(2) 
            under4_5 = str(under4_5) + "%"
            over4_5 = str(over4_5) + "%"     

            odd_u_55 = (100 / under5_5).round(2) 
            odd_o_55 = (100 / over5_5).round(2) 
            under5_5 = str(under5_5) + "%"
            over5_5 = str(over5_5) + "%"  

            odd_u_65 = (100 / under6_5).round(2) 
            odd_o_65 = (100 / over6_5).round(2) 
            under6_5 = str(under6_5) + "%"
            over6_5 = str(over6_5) + "%"     

            home_probs = line1[0] + sum(line2[0:2]) + sum(line3[0:3]) + sum(line4[0:4]) + sum(line5[0:5]) + sum(line6[0:6])
            draw_probs = line0[0] + line1[1] + line2[2] + line3[3] + line4[4] + line5[5] + line6[6]
            away_probs = sum(line0[1:7]) + sum(line1[2:7]) + sum(line2[3:7]) + sum(line3[4:7]) + sum(line4[5:7]) + line5[6] 

            home_probs = home_probs.round(2)
            draw_probs = draw_probs.round(2)
            away_probs = away_probs.round(2)
            sum_probs = (home_probs + draw_probs + away_probs).round(2)
            sum_probs = str(sum_probs) + "%"            

            home_odd = (100 / home_probs).round(2)
            draw_odd = (100 / draw_probs).round(2)
            away_odd = (100 / away_probs).round(2)

            home_probs = str(home_probs) + "%"
            draw_probs = str(draw_probs) + "%"
            away_probs = str(away_probs) + "%"

            main_line = "OVER 2.5: {} - {} | UNDER 2.5: {} - {} | {}".format(odd_o_25, over2_5, odd_u_25, under2_5, sum2_5)            
            match_odds = "HOME: {} - {} | DRAW: {} - {} | AWAY: {} - {} | {}".format(home_odd, home_probs, draw_odd, draw_probs, away_odd, away_probs, sum_probs)
            goals0_5 = "OVER 0.5: {} - {} | UNDER 0.5: {} - {} | {}".format(odd_o_05, over0_5, odd_u_05, under0_5, sum0_5)
            goals1_5 = "OVER 1.5: {} - {} | UNDER 1.5: {} - {} | {}".format(odd_o_15, over1_5, odd_u_15, under1_5, sum1_5)
            goals3_5 = "OVER 3.5: {} - {} | UNDER 3.5: {} - {} | {}".format(odd_o_35, over3_5, odd_u_35, under3_5, sum3_5)
            goals4_5 = "OVER 4.5: {} - {} | UNDER 4.5: {} - {} | {}".format(odd_o_45, over4_5, odd_u_45, under4_5, sum4_5)
            goals5_5 = "OVER 5.5: {} - {} | UNDER 5.5: {} - {} | {}".format(odd_o_55, over5_5, odd_u_55, under5_5, sum5_5)
            goals6_5 = "OVER 6.5: {} - {} | UNDER 6.5: {} - {} | {}".format(odd_o_65, over6_5, odd_u_65, under6_5, sum6_5)

            print("=" * 82)
            print(" ASIAN HANDICAP | TOTAL GOALS".center(80))
            print("=" * 82)
            print("", "Match Expected Goals", round(match_goals_expectancy, 2), "|", "Home Expected Goals:", round(home_goals_expectancy, 2), "|", "Away Expected Goals:", round(away_goals_expectancy, 2))                       
            print("-" * 82)
            print(colored(main_line.center(82), "white", "on_blue"))
            print("-" * 82)
            print(colored(match_odds.center(82), "white", "on_red"))
            print("=" * 82)
            print(goals0_5.center(82))
            print("-" * 82)
            print(goals1_5.center(82))
            print("-" * 82)
            print(goals3_5.center(82))
            print("-" * 82)
            print(goals4_5.center(82))
            print("-" * 82)
            print(goals5_5.center(82))
            print("-" * 82)
            print(goals6_5.center(82))
            print("-" * 82)

            question = str(input(" Want to continue? [y/n]: ")).lower()
            os.system("clear")

            if (question == "n"):                               
                    print("=" * 82)
                    print("Next time!".center(82))
                    print("=" * 82)
                    exit()
            elif (question != "y"):
                print("=" * 82)
                print("Type a Correct Data!".center(82))
                print("=" * 82)
                question = str(input(" Want to continue? [y/n]: ")).lower()
                os.system("clear")
                if (question == "n"):                    
                    print("=" * 82)
                    print("Next time!".center(82))
                    print("=" * 82)
                    exit()
                elif (question != "y"):
                    while (question != "y"):
                        os.system("clear")
                        print("=" * 82)
                        print("Type a Correct Data!".center(82))
                        print("=" * 82)
                        question = str(input(" Want to continue? [y/n]: ")).lower()                    
                        os.system("clear")
                        if (question == "n"):                            
                            print("=" * 82)
                            print("Next time!".center(82))
                            print("=" * 82)
                            exit()

        except ValueError:
            os.system("clear")

except KeyboardInterrupt:
    os.system("clear")
    sys.exit(0)