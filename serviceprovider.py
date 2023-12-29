import mysql.connector 
from DBConnection import DBConnection
    
class serviceprovider(DBConnection):
    
    def create_product(self, name, price,description,stockQuantity):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            #self.open() 
            query = f"INSERT INTO products (name, price,description,stockQuantity) VALUES ('{name}', '{price}','{description}', '{stockQuantity}')"
            c = con.cursor()
            c.execute(query)
            #self.c.execute(query)
            #self.mydb.commit()
            con.commit()
            product_id = c.lastrowid
            print(f"\nProduct '{name}' added to the database with ID: {product_id}\n")
            return product_id
        except Exception as e:
            print(e)
            return None
        finally:
            pass#self.close()

    def create_customer(self, name, email, password):
        try:
            self.open() 
            query = f"INSERT INTO customers (name, email, password) VALUES ('{name}', '{email}', '{password}')"
            self.c.execute(query)
            self.mydb.commit()
            customer_id = self.c.lastrowid
            print(f"\nCustomer '{name}' added to the database with ID: {customer_id}\n")
            return customer_id
        except Exception as e:
            print(e)
            return None
        finally:
            self.close() 

    def customer_exists(self, name, password):
        try:
            self.open()  
            query = f"SELECT COUNT(*) FROM customers WHERE name = '{name}' AND password = '{password}'"
            self.c.execute(query)
            count = self.c.fetchone()[0]  
            return count
        
        except Exception as e:
            print(e)
            return False
        
        finally:
            self.close()