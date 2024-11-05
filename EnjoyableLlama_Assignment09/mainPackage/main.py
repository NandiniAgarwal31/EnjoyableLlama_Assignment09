# main.py

from itertools import product
import re
import pyodbc
from sqlPackage.sql import * 
try:
    conn = connect_to_database()  # Add parentheses to call the function
    cursor = conn.cursor()
   
except Exception as e:
    print("Error accessing database")
    print(e)
    exit()  # Give up

# If I got this far, I have a cursor object
product_ID = input("Enter a Big 12 school: ")
query_string = "SELECT * FROM tProduct WHERE NameID  = '" + product_ID +"'"
print(query_string)

# submit the qury string to our databse server and srore the results in a varible
results = cursor.execute(query_string)
for row in results.fetchall(): 
    print(row[4]) # we tried to print results and we tried to print.description 


conn.close() # close the connection to the DB server