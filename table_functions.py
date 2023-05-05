# Source: Used MySQL documentation as a starting point for table functions
# https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html

import mysql.connector as connector
import os

host = "localhost"
user = os.environ.get('user')
password = os.environ.get('password')
database = "war_game"

def update_table(winner):
    table = connector.connect(host, user, password, database)
    cursor = table.cursor()

    cursor.execute("SELECT num_wins FROM winner_history WHERE player = " + str(winner) + ";")
    num_wins = cursor.fetchone()

    cursor.execute("UPDATE winner_history SET num_wins = " + str(num_wins[0] + 1) + "WHERE player = " + str(winner) + ";")
    table.commit()

def clear_table():
    table = connector.connect(host, user, password, database)
    cursor = table.cursor()

    cursor.execute("UPDATE winner_history SET num_wins = 0;")
    table.commit()

def fetch_history():
    table = connector.connect(host, user, password, database)
    cursor = table.cursor()

    cursor.execute("SELECT * FROM games")

    return cursor.fetchall()