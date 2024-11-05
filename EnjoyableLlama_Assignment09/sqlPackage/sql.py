# sql.py
import pyodbc

def connect_to_database():
    """
    Connect to the database
    @ return Connection object: The open connection, or None or error
    """
   
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                              'Database=GroceryStoreSimulator;'
                              'uid=IS4010Login;'
                              'pwd=P@ssword2;')
        cursor = conn.cursor()
    except:
        conn = None

    return conn
   


