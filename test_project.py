import pytest
import sqlite3

from class_helper import Crud_db

db = Crud_db() 



def test_exist_tables():
    db.connect()
    query = """ SELECT name FROM sqlite_master WHERE type='table' """
    db.execute(query)
    result = db.cursor.fetchall()

    # print(result)
    
    assert len(result) == 8

