import pytest
import sqlite3
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


class TestSQLiteQuery:
    def test_run_with_no_db(self):
        sqlite_query = db.connect()

        msg_match = "The db must be specified"
        with pytest.raises(ValueError, match=msg_match):
            sqlite_query
