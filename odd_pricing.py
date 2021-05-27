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

home_team_goals_for = input(" Home Team 'Goals For' Average: ")
home_team_goals_against = input(" Home Team 'Goals Against' Average: ")
away_team_goals_for = input(" Away Team 'Goals For' Average: ")
away_team_goals_against = input(" Away Team 'Goals Against' Average: ")
home_league_goals_for = input(" Home League 'Goals For' Average: ")
home_league_goals_against = input(" Home League 'Goals Against' Average: ")
away_league_goals_for = home_team_goals_against
away_league_goals_against = home_league_goals_for

home_attack_strength = (home_team_goals_for / home_league_goals_for)
home_defense_strength (home_team_goals_against / home_league_goals_against)
away_attack_strength = (away_team_goals_for / away_league_goals_for)
away_defense_strength = (away_team_goals_against / away_league_goals_against)

home_goals_expectancy = (home_attack_strength * away_defense_strength * home_league_goals_for)
away_goals_expectancy = (away_attack_strength * home_defense_strength * away_league_goals_for)

match_goals_expectancy = (home_goals_expectancy + away_goals_expectancy)