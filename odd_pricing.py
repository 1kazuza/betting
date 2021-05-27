import numpy as np
from scipy.stats import poisson
import pandas as pd
import pyfiglet
import argparse
import os
import sys

parser = argparse.ArgumentParser(description = "This program determines the prices of odds in football events.")
parser.add_argument("-v", action = "version", version = "Odd Pricing 1.0")
msg = parser.parse_args()

os.system("clear")

global home_team_goals_for, home_team_goals_against, away_team_goals_for, away_team_goals_against 
global home_league_goals_for, home_league_goals_against, away_league_goals_for, away_league_goals_against
global home_attack_strength, home_defense_strength, away_attack_strength, away_defense_strength
global home_goals_expectancy, away_goals_expectancy, match_goals_expectancy
    
print("=" * 80)
intro = pyfiglet.figlet_format(" Odd Pricing 1.0")
print(intro)
print("=" * 80)
print("A football betting App CLI".center(80))
print("=" * 80)
print("For exit, type: CTRL + C".center(80))
print("=" * 80)

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

print(" It's works!")
print("", match_goals_expectancy)