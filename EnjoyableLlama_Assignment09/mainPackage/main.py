# main.py
from sqlPackage.sql import *
import random

if __name__ == "__main__":
    # Step 1: Connect to the database
    conn = connect_to_database()
    if conn is None:
        print("Failed to connect to the database.")
    else:
        # Step 2: Fetch product data
        product_data = fetch_product_data(conn)
        if not product_data:
            print("No product data found.")
            conn.close()
        else:
            # Step 3: Randomly select one row from product data
            selected_product = random.choice(product_data)
            product_id, upc, description, manufacturer_id, brand_id = selected_product

            # Step 4: Fetch manufacturer name
            manufacturer_name = fetch_manufacturer_name(conn, manufacturer_id)
            if not manufacturer_name:
                print("Manufacturer not found.")
                conn.close()
            else:
                # Step 5: Fetch brand name
                brand_name = fetch_brand_name(conn, brand_id)
                if not brand_name:
                    print("Brand not found.")
                    conn.close()
                else:
                    # Step 6: Fetch number of items sold
                    items_sold = fetch_items_sold(conn, product_id)

                    # Step 7: Construct output sentence
                    output_sentence = (
                        f"The product '{description}', manufactured by '{manufacturer_name}' under the brand '{brand_name}', "
                        f"has sold a total of {items_sold} items."
                    )
                    print(output_sentence)

                    # Close the database connection
                    conn.close()