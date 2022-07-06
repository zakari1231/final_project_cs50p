import pytest
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



# test class helper

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

# def check_if_pdf_file():
#     savepdf = db.save_the_last_bill_to_html_pdf()
#     # savepdf
#     filename = Path('weasyprint_pdf_report.pdf')
#     # os.path.exists(filename)    
#     assert os.path.exists(filename) == True
#     assert savepdf == 'pdf file and html file created successfully'

# def check_if_file_created():
#     assert db.save_the_last_bill_to_html_pdf() == 1
    # db.save_the_last_bill_to_html_pdf()
    # filename = Path('weasyprint_pdf_report.pdf')
    # save_pdf = db.save_the_last_bill_to_html_pdf() 
    # # assert db.save_the_last_bill_to_html_pdf() == 'pdf file and html file created successfully'
    # # assert db.save_the_last_bill_to_html_pdf() == os.path.exists(filename) 
    # assert db.save_the_last_bill_to_html_pdf() == 1
    # assert os.path.isfile(filename)



# check_if_pdf_file()
# #using pathlib
# from pathlib import Path

# file_name = Path("file.txt")
# if file_name.exists():
#     print("exists") 
# else:
#     print("does not exist") 


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
