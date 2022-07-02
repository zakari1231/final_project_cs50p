import pytest
import sqlite3
import time, datetime
from datetime import timedelta
# from prefect.tasks.database.sqlite import SQLiteQuery

from class_helper import Crud_db

db = Crud_db() 



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


# # import writer

# class TestFile(object):

#     def test_my_function(self, tmpdir):

#         # test_path = tmpdir.join('F:/final_project_cs50p')
#         db_path =  tmpdir / "database.db"
#         save_csv = db.save_to_csv()

#         save_csv

#         assert db_path.read() == 'expenses_all'


# # def test_save_to_csv():
# #     assert db.save_to_csv() == 


# class TestSQLiteQuery:
#     def test_run_with_no_db(self):
#         sqlite_query = db.connect()

#         msg_match = "The db must be specified"
#         with pytest.raises(ValueError, match=msg_match):
#             sqlite_query
