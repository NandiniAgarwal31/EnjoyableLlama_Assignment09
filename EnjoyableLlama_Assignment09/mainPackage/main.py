# main.py
from sqlPackage.sql import * 
import random

if __name__ == "__main__":
    print("Starting the program...")

    # Step 1: Connect to the database
    print("Step 1: Connecting to the database...")
    conn = connect_to_database()
    if conn is None:
        print("Failed to connect to the database.")
    else:
        print("Successfully connected to the database.")

        # Step 2: Fetch product data from tProduct
        print("Step 2: Fetching product data from tProduct table...")
        product_data = fetch_product_data(conn)
        if not product_data:
            print("No product data found.")
            conn.close()
        else:
            print("Product data retrieved successfully.")
            print(f"Number of products retrieved: {len(product_data)}")

            # Step 3: Randomly select one row from product data
            print("Step 3: Randomly selecting one product...")
            selected_product = random.choice(product_data)
            product_id, upc, description, manufacturer_id, brand_id = selected_product
            print(f"Selected Product - ID: {product_id}, Description: {description}, "
                  f"ManufacturerID: {manufacturer_id}, BrandID: {brand_id}")

            # Step 4: Fetch manufacturer name
            print("Step 4: Fetching manufacturer name using join...")
            manufacturer_data = fetch_product_details_with_manufacturer(conn)
            manufacturer_name = next(
                (row[2] for row in manufacturer_data if row[0] == product_id), None
            )
            if not manufacturer_name:
                print("Manufacturer not found.")
                conn.close()
            else:
                print(f"Manufacturer Name: {manufacturer_name}")

                # Step 5: Fetch brand name
                print("Step 5: Fetching brand name using join...")
                brand_data = fetch_product_brand_details(conn)
                brand_name = next(
                    (row[2] for row in brand_data if row[0] == product_id), None
                )
                if not brand_name:
                    print("Brand not found.")
                    conn.close()
                else:
                    print(f"Brand Name: {brand_name}")

                    # Step 6: Fetch number of items sold for the selected product
                    print("Step 6: Fetching number of items sold for the selected product...")
                    items_sold = fetch_product_sales_details(conn, product_id)
                    print(f"Number of items sold: {items_sold}")

                    # Step 7: Construct output sentence
                    print("Step 7: Constructing output sentence...")
                    output_sentence = (
                        f"The product '{description}', manufactured by '{manufacturer_name}' under the brand '{brand_name}', "
                        f"has sold a total of {items_sold} items."
                    )
                    print("Output Sentence:")
                    print(output_sentence)

        # Close the database connection after all steps are done
        print("Closing database connection.")
        conn.close()
    print("Program completed.")