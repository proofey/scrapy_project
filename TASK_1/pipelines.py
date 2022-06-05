import sqlite3


class DeviceSQLitePipeline:
    def __init__(self):
        self.con = sqlite3.connect('devices.db')
        self.cur = self.con.cursor()
        self.create_table()


    #This method creates a new database table if it doesn't exists and skip it if it exists
    def create_table(self):  
        self.cur.execute("""CREATE TABLE IF NOT EXISTS products(    
                            product_number CHAR(100) PRIMARY KEY,
                            category CHAR(50),
                            subcategory CHAR(50),
                            name CHAR(50),
                            subtitle CHAR(50),
                            price REAL  
        )""")

#Here we process the item and store it in the table we created above.
#Every item has unique primary key wich is the 'product number'
#If we change some of the values in the table row the new value is stored
    def process_item(self, item, spider):      
        self.cur.execute(f"""INSERT INTO products (product_number, category, subcategory, name, subtitle, price)
            VALUES (?, ?, ?, ?, ?, ?) 
                    ON CONFLICT (product_number) DO UPDATE SET
                    category = EXCLUDED.category,
                    subcategory = EXCLUDED.subcategory,
                    name = EXCLUDED.name,
                    subtitle = EXCLUDED.subtitle,
                    price = EXCLUDED.price
                    """, 
                    (item['product_number'],
                    item['category'],
                    item['subcategory'], 
                    item['name'], 
                    item['subtitle'], 
                    item['price']))
        self.con.commit()
        return item

