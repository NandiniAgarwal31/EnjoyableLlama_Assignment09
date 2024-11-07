# Name: Mahika Gunjkar, Nandini Agrawal, Ishani Roy Chowdhury
# email:  gunjkamg@mail.uc.edu, Agarwand@mail.uc.edu, roychoii@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   6/11/2024
# Course #/Section:  4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Team assignment based on sql quesries and its data relation with python. We coded such that the databse output is in terminal and reflects all the joins and statements.

# Brief Description of what this module does. This module has all the databse connections and joins required. It uses the fetch function to derive all the data.
# Citations:
# Anything else that's relevant: 





#sql.py

import pyodbc
import random

# establishing a connection to the database

def connect_to_database():
    """
    Connect to the SQL Server database.
    @return: Connection object if connection is successful, None otherwise
    """
    try:
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=GroceryStoreSimulator;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;'
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


# fetch data from the product table

def fetch_product_data(conn):
    """
    Fetch data from tProduct table, excluding rows with empty or NULL Description.
    @param conn: Database connection object
    @return: List of rows from the tProduct table
    """
    cursor = conn.cursor()
    query = """
    SELECT ProductID, [UPC-A], Description, ManufacturerID, BrandID 
    FROM tProduct 
    WHERE Description IS NOT NULL AND Description <> ''
    """
    cursor.execute(query)
    results = cursor.fetchall()
    return results



# fetch product details and the manufacturer name

def fetch_product_details_with_manufacturer(conn):
    """
    Join tProduct with tManufacturer to get product details along with manufacturer name.
    @param conn: Database connection object
    @return: List of products with manufacturer name
    """
    cursor = conn.cursor()
    query = """
    SELECT p.ProductID, p.Description, m.Manufacturer
    FROM tProduct p
    JOIN tManufacturer m ON p.ManufacturerID = m.ManufacturerID
    """
    cursor.execute(query)
    results = cursor.fetchall()
    return results


# fetch product sales information for each product

def fetch_product_sales_details(conn, product_id):
    """
    Join tTransactionDetail and tTransaction to get the sales details for a specific product.
    @param conn: Database connection object
    @param product_id: Product ID to filter sales details
    @return: Total quantity sold for the given product
    """
    cursor = conn.cursor()
    query = """
    SELECT SUM(td.QtyOfProduct) AS TotalQuantitySold
    FROM tTransactionDetail td
    JOIN tTransaction t ON td.TransactionID = t.TransactionID
    WHERE td.ProductID = ? AND t.TransactionTypeID = 1
    """
    cursor.execute(query, product_id)
    result = cursor.fetchone()
    return result[0] if result else 0

# fetch product brand details and brand name

def fetch_product_brand_details(conn):
    """
    Join tProduct with tBrand to get product details along with brand name.
    @param conn: Database connection object
    @return: List of products with brand name
    """
    cursor = conn.cursor()
    query = """
    SELECT p.ProductID, p.Description, b.Brand
    FROM tProduct p
    JOIN tBrand b ON p.BrandID = b.BrandID
    """
    cursor.execute(query)
    results = cursor.fetchall()
    return results

# fetch all of the details relating to a product

def fetch_full_product_details(conn):
    """
    Join tProduct, tManufacturer, and tBrand to get complete details for each product.
    @param conn: Database connection object
    @return: List of products with full details (product description, manufacturer, and brand)
    """
    cursor = conn.cursor()
    query = """
    SELECT p.ProductID, p.Description, m.Manufacturer, b.Brand
    FROM tProduct p
    JOIN tManufacturer m ON p.ManufacturerID = m.ManufacturerID
    JOIN tBrand b ON p.BrandID = b.BrandID
    """
    cursor.execute(query)
    results = cursor.fetchall()
    return results
