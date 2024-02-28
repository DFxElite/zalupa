import sqlite3
from typing import Union
import datetime
import json

dbpath = "data/bot.db"

def user_exists(user_id: int) -> bool:
    with sqlite3.connect(dbpath) as db:
        sql = f'SELECT count(*) FROM users WHERE user_id = "{user_id}"'
        count = db.execute(sql).fetchone()[0]
        return True if count == 1 else False

def create_user(user_id: int, username: str):
    with open('data/config.json') as file:
        config = json.load(file)
        perc = config['Bot_Data']['Referal_Percentage']

    with sqlite3.connect(dbpath) as db:
        sql = f'INSERT INTO users VALUES ("{user_id}", "{username}", 0, 0, 0, 0, "{perc}")'
        db.execute(sql)
        db.commit()

def get_user(user_id: int) -> dict:
    with sqlite3.connect(dbpath) as db:
        sql = f'SELECT * FROM users WHERE user_id = "{user_id}"'
        user_data = db.execute(sql).fetchone()
    
    if str(user_id) == '0':
        return {'user_id': '0', 'username': '0', 'balance': '0', 'invited_by': '0',  'unlimited': '0', 'subscribed': '0', 'percentage': '0'}
    mapping = ['user_id', 'username', 'balance', 'invited_by', 'unlimited', 'subscribed', 'percentage']
    user_data_dictionary = dict(zip(mapping, user_data))

    if user_data[5] == 1:
        user_data_dictionary.update({'subscribed': True})
    else:
        user_data_dictionary.update({'subscribed': False})
    date = user_data_dictionary['unlimited']

    if str(date) == '0':
        date = datetime.datetime(2000, 1, 1).date()
    else:
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    user_data_dictionary.update({'unlimited': date})
    return user_data_dictionary

def update_user(user_id: int, column: str, value: Union[int, str]):
    with sqlite3.connect(dbpath) as db:
        sql = f'UPDATE users SET {column} = "{value}" WHERE user_id = "{user_id}"'
        db.execute(sql)
        db.commit()

def get_user_referals_count(user_id: int):
    with sqlite3.connect(dbpath) as db:
        sql = f'SELECT count(*) FROM users WHERE invited_by = "{user_id}"'
        count = db.execute(sql).fetchone()[0]
        return count

def get_all_users_ids():
    with sqlite3.connect(dbpath) as db:
        sql = 'SELECT user_id FROM users'
        users = db.execute(sql).fetchall()
        return users

def get_balances_sum():
    with sqlite3.connect(dbpath) as db:
        sql = 'SELECT balance FROM users'
        balances = db.execute(sql).fetchall()
        total = 0
        
        for balance in balances:
            total += int(balance[0])
        return total

def get_referals():
    with sqlite3.connect(dbpath) as db:
        sql = 'SELECT invited_by FROM users WHERE invited_by != 0'
        users = db.execute(sql).fetchall()
        users = list(set(users))
        map = {}
        for user in users:
            map.update({f'{user[0]}': db.execute(f'SELECT count(*) FROM users WHERE invited_by = "{user[0]}"').fetchone()[0]})
        return map
    
    
    
    