# sql.py
import pyodbc
import random

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

def fetch_product_data(conn):
    """
    Fetch data from tProduct table.
    @param conn: Database connection object
    @return: List of rows from the tProduct table
    """
    cursor = conn.cursor()
    query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def fetch_manufacturer_name(conn, manufacturer_id):
    """
    Fetch the manufacturer name for a given ManufacturerID.
    @param conn: Database connection object
    @param manufacturer_id: Manufacturer ID to search for
    @return: Manufacturer name as a string
    """
    cursor = conn.cursor()
    query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0] if result else None

def fetch_brand_name(conn, brand_id):
    """
    Fetch the brand name for a given BrandID.
    @param conn: Database connection object
    @param brand_id: Brand ID to search for
    @return: Brand name as a string
    """
    cursor = conn.cursor()
    query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0] if result else None

def fetch_items_sold(conn, product_id):
    """
    Fetch the number of items sold for a specific ProductID.
    @param conn: Database connection object
    @param product_id: Product ID to search for
    @return: Total number of items sold as an integer
    """
    cursor = conn.cursor()
    query = (
        "SELECT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold "
        "FROM dbo.tTransactionDetail INNER JOIN dbo.tTransaction "
        "ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID "
        "WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = ?)"
    )
    cursor.execute(query, product_id)
    result = cursor.fetchone()
    return result[0] if result else 0
