import pandas as pd 
import numpy as np
import mysql.connector as mysql
from sqlalchemy.exc import SQLAlchemyError
import sqlalchemy 
import pymysql 
import os
import pyfiglet
import argparse
import sys

parser = argparse.ArgumentParser(description = "This program shows metrics about football(soccer) teams perfomance.")
parser.add_argument("-v", action = "version", version = "Club Stats 1.0")
msg = parser.parse_args()

os.system("clear")

def total():

    value_1 = "SELECT round((GFt/(GFt+GAt))*100, 2) AS 'Aprov', round(GFt/Mt, 2) AS 'Avg_Goals_For', round(GAt/Mt, 2) AS 'Avg_Goals_Against' FROM Season_2019" 
    value_2 = "SELECT round((GFt/(GFt+GAt))*100, 2) AS 'Aprov', round(GFt/Mt, 2) AS 'Avg_Goals_For', round(GAt/Mt, 2) AS 'Avg_Goals_Against' FROM Season_2020" 
    value_3 = "SELECT round((GFt/(GFt+GAt))*100, 2) AS 'Aprov', round(GFt/Mt, 2) AS 'Avg_Goals_For', round(GAt/Mt, 2) AS 'Avg_Goals_Against' FROM Season_2021" 
    value_4 = "SELECT Clubs FROM Season_2021"

    result_1 = pd.read_sql_query(value_1, connect) 
    result_2 = pd.read_sql_query(value_2, connect) 
    result_3 = pd.read_sql_query(value_3, connect) 
    result_4 = pd.read_sql_query(value_4, connect)

    frame = (result_1 + result_2 + result_3)/3
    frame.insert(0, "Clubs", result_4)
    frame.Aprov = frame.Aprov.round(decimals=2)
    frame.Avg_Goals_For = frame.Avg_Goals_For.round(decimals=2)
    frame.Avg_Goals_Against = frame.Avg_Goals_Against.round(decimals=2)
    frame_new = frame.rename(columns={"Aprov" : "(%)Goals For", "Avg_Goals_For" : "Avg.Goals For", "Avg_Goals_Against" : "Avg.Goals Against"})  
    frame_new = frame_new.sort_values(by="(%)Goals For", ascending=False)

    print("=" * 70) 
    print("BRAZILIAN FOOTBALL DATA".center(70)) 
    print("=" * 70) 
    print("-" * 70)
    print("Total Results".center(70))
    print("-" * 70)
    print(frame_new.to_string(index=False))
    print("=" * 70)

def home():

    value_1 = "SELECT round((GFh/(GFh+GAh))*100, 2) AS 'Aprov', round(GFh/Mh, 2) AS 'Avg_Goals_For', round(GAh/Mh, 2) AS 'Avg_Goals_Against' FROM Season_2019" 
    value_2 = "SELECT round((GFh/(GFh+GAh))*100, 2) AS 'Aprov', round(GFh/Mh, 2) AS 'Avg_Goals_For', round(GAh/Mh, 2) AS 'Avg_Goals_Against' FROM Season_2020" 
    value_3 = "SELECT round((GFh/(GFh+GAh))*100, 2) AS 'Aprov', round(GFh/Mh, 2) AS 'Avg_Goals_For', round(GAh/Mh, 2) AS 'Avg_Goals_Against' FROM Season_2021" 
    value_4 = "SELECT Clubs FROM Season_2021"

    result_1 = pd.read_sql_query(value_1, connect) 
    result_2 = pd.read_sql_query(value_2, connect) 
    result_3 = pd.read_sql_query(value_3, connect) 
    result_4 = pd.read_sql_query(value_4, connect)

    frame = (result_1 + result_2 + result_3)/3
    frame.insert(0, "Clubs", result_4)
    frame.Aprov = frame.Aprov.round(decimals=2)
    frame.Avg_Goals_For = frame.Avg_Goals_For.round(decimals=2)
    frame.Avg_Goals_Against = frame.Avg_Goals_Against.round(decimals=2)
    frame_new = frame.rename(columns={"Aprov" : "(%)Goals For", "Avg_Goals_For" : "Avg.Goals For", "Avg_Goals_Against" : "Avg.Goals Against"})  
    frame_new = frame_new.sort_values(by="(%)Goals For", ascending=False)

    print("=" * 70) 
    print("BRAZILIAN FOOTBALL DATA".center(70)) 
    print("=" * 70) 
    print("-" * 70)
    print("Home Results".center(70))
    print("-" * 70)
    print(frame_new.to_string(index=False))
    print("=" * 70)

def away():

    value_1 = "SELECT round((GFa/(GFa+GAa))*100, 2) AS 'Aprov', round(GFa/Ma, 2) AS 'Avg_Goals_For', round(GAa/Ma, 2) AS 'Avg_Goals_Against' FROM Season_2019" 
    value_2 = "SELECT round((GFa/(GFa+GAa))*100, 2) AS 'Aprov', round(GFa/Ma, 2) AS 'Avg_Goals_For', round(GAa/Ma, 2) AS 'Avg_Goals_Against' FROM Season_2020" 
    value_3 = "SELECT round((GFa/(GFa+GAa))*100, 2) AS 'Aprov', round(GFa/Ma, 2) AS 'Avg_Goals_For', round(GAa/Ma, 2) AS 'Avg_Goals_Against' FROM Season_2021" 
    value_4 = "SELECT Clubs FROM Season_2021"

    result_1 = pd.read_sql_query(value_1, connect) 
    result_2 = pd.read_sql_query(value_2, connect) 
    result_3 = pd.read_sql_query(value_3, connect) 
    result_4 = pd.read_sql_query(value_4, connect)

    frame = (result_1 + result_2 + result_3)/3
    frame.insert(0, "Clubs", result_4)
    frame.Aprov = frame.Aprov.round(decimals=2)
    frame.Avg_Goals_For = frame.Avg_Goals_For.round(decimals=2)
    frame.Avg_Goals_Against = frame.Avg_Goals_Against.round(decimals=2)
    frame_new = frame.rename(columns={"Aprov" : "(%)Goals For", "Avg_Goals_For" : "Avg.Goals For", "Avg_Goals_Against" : "Avg.Goals Against"})  
    frame_new = frame_new.sort_values(by="(%)Goals For", ascending=False)

    print("=" * 70) 
    print("BRAZILIAN FOOTBALL DATA".center(70)) 
    print("=" * 70) 
    print("-" * 70)
    print("Away Results".center(70))
    print("-" * 70)
    print(frame_new.to_string(index=False))
    print("=" * 70)

try:

    while True:

        try:
            print("=" * 80)
            intro = pyfiglet.figlet_format(" Club Stats 1.0")
            print(intro)
            print("=" * 80)
            print("A football betting App CLI".center(80))
            print("=" * 80)
            print("For exit, type: CTRL + C".center(80))
            print("=" * 80)

            db_name = input(" Choose Your Database: ").capitalize()
            os.system("clear") 
            db = "USE {} ".format(db_name)
            connect = sqlalchemy.create_engine("mysql+pymysql://root:Hdt24p5t@@localhost:3306")        
            connect.execute(db)    
            
            try:   
                total()
                home()
                away()

                question = str(input(" Want to continue? [y/n]: ")).lower()
                os.system("clear")

                if (question == "n"):                               
                    print("=" * 80)
                    print("Next time!".center(80))
                    print("=" * 80)
                    exit()
                elif (question != "y"):
                    print("=" * 80)
                    print("Type a Correct Database!".center(80))
                    print("=" * 80)
                    question = str(input(" Want to continue? [y/n]: ")).lower()
                    os.system("clear")
                    if (question == "n"):                    
                        print("=" * 80)
                        print("Next time!".center(80))
                        print("=" * 80)
                        exit()
                    elif (question != "y"):
                        while (question != "y"):
                            os.system("clear")
                            print("=" * 80)
                            print("Type a Correct Database!".center(80))
                            print("=" * 80)
                            question = str(input(" Want to continue? [y/n]: ")).lower()                    
                            os.system("clear")
                            if (question == "n"):                            
                                print("=" * 80)
                                print("Next time!".center(80))
                                print("=" * 80)
                                exit()

            except ValueError:
                os.system("clear")

        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])        
            os.system("clear")    

except KeyboardInterrupt:
    os.system("clear")
    sys.exit(0)