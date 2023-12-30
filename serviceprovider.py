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
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"INSERT INTO customers (name, email, password) VALUES ('{name}', '{email}', '{password}')"
            c = con.cursor()
            c.execute(query)
            con.commit()
            customer_id = c.lastrowid
            print(f"\nCustomer '{name}' added to the database with ID: {customer_id}\n")
            return customer_id
        except Exception as e:
            print(e)
            return None
        finally:
            pass 

    def customer_exists(self, name, password):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"SELECT COUNT(*) FROM customers WHERE name = '{name}' AND password = '{password}'"
            c = con.cursor()
            c.execute(query)
            con.commit()
            #self.c.execute(query)
            count = c.fetchone()[0]  
            return count
        except Exception as e:
            print(e)
            return False
        finally:
            pass
        
    def delete_product(self,product_id):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"DELETE FROM products WHERE product_id = {product_id}"
            c = con.cursor()
            c.execute(query)
            con.commit()
            if c.rowcount > 0:
                print(f"Product with ID: {product_id} deleted successfully.")
            else:
                print(f"No product found with ID: {product_id}. Nothing was deleted.")
            return False
        except Exception as e:
            print(e)
            return None
        finally:
            pass
        
    def delete_customer(self, customer_id):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"DELETE FROM customers where customer_id = {customer_id}"
            c= con.cursor()
            c.execute(query)
            con.commit()
            if c.rowcount > 0:
                print(f"Customer with ID: {customer_id} deleted successfully.")
            else:
                print(f"No customer found with ID: {customer_id}. Nothing was deleted.")
            return False
        except Exception as e:
            print(e)
            return None
        finally:
            pass
        
    def addTocart(self,customer_id,product_id, quantity):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"INSERT INTO cart (customer_id, product_id, quantity) VALUES ('{customer_id}', '{product_id}','{quantity}')"
            c= con.cursor()
            c.execute(query)
            con.commit()
            print(f"Product ID {product_id} added to the cart for Customer ID {customer_id}. Quantity: {quantity}")
            return False
        except Exception as e:
            print(e)
            return None
        finally:
            pass
        
    def removefromcart(self,customer_id,product_id,):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"DELETE FROM cart WHERE customer_id ={customer_id} AND product_id = {product_id}"
            c= con.cursor()
            c.execute(query)
            con.commit()
            if c.rowcount > 0:
                print(f"Product ID {product_id} removed from the cart for Customer ID {customer_id}.")
            else:
                print(f"No product found in the cart for Customer ID {customer_id} with Product ID {product_id}. Nothing was removed.")
            return False
        except Exception as e:
            print(e)
            return None
        finally:
            pass
        
    def getallfromcart(self,customer_id):
        con = mysql.connector.connect(host="localhost", user="root", password="root", database="ecommerce",port="3306",auth_plugin='mysql_native_password')
        try:
            query= f"SELECT product_id, quantity from cart where customer_id= {customer_id}"
            c= con.cursor()
            c.execute(query)
            con.commit()
            
            return False
        except Exception as e:
            print(e)
            return None
        finally:
            pass
        
    
        
            
            
        
                
                
    
                