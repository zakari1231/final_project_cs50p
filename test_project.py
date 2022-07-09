import pytest
import sys
import sqlite3
import time, datetime
from datetime import timedelta
# from prefect.tasks.database.sqlite import SQLiteQuery
from pathlib import Path
import os

from class_helper import Crud_db
from project import convert_date_format


db = Crud_db() 

# test project

def test_convert_date_format():
    assert convert_date_format('10-10-2022') =='2022-10-10'
    assert convert_date_format('09-25-2003') == '2003-09-25'
    assert convert_date_format('05-05-1989') == '1989-05-05'


def test_main(capsys):

    from project import main
    sys.argv = ['h', 'H', 'help']
    main()
    out, err = capsys.readouterr()
    assert out.startswith(" \n    This is a Seller Management Systeme that cont") is True
    

def test_tables():
    db.connect()
    query = """ SELECT name FROM sqlite_master WHERE type='table' """
    db.execute(query)
    result = db.cursor.fetchall()

    # print(result)
    
    assert len(result) == 8

def test_login_logout():
    # test if user login the time will be this time + 3 hours if not user is logout
    db.connect()
    date_time_now = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time_to_logout = datetime.datetime.now() + timedelta(hours=3)
    query = ''' SELECT max(date_time_logout) FROM login_or_not '''
    db.execute(query)
    result = db.cursor.fetchall()
    if result[0][0] < date_time_now:
        assert db.check_if_login() == False
    else:
        assert db.check_if_login() == True

