from serviceprovider import serviceprovider

class Main():

    def main():
        r=serviceprovider()
        while True:
            print("\n----------Main Menu----------")
            print("\nPress-1 Create product")
            print("\nPress-2 Create customer")
            print("\nPress-3 Delete product")
            print("\nPress-4 Delete customer")
            print("\nPress-5 Add to Cart")
            print("\nPress-6 Remove from Cart")
            print("\nPress-7 Show Cart")
            print("\nPress-8 Place Order")
            print("\nPress-9 Show Order by customer")
            
            print("Press-3 exit")
            i=int(input())
            if i==1:
                product_name = input("Enter product name: ")
                description = input("Enter description: ")
                price = float(input("Enter price: "))
                quantity=int(input("Enter stock quantity: "))
                r.create_product(product_name, price,description,quantity)
            elif i==2:
                name=input("Enter name: ")
                password=input("Enter password: ")
                if r.customer_exists((name,password)>0):
                    print("customer already exists")
                else:
                    email=input("Enter mail id: ")
                    r.create_customer(name, email, password)
            elif i==3:
                product_id=input("Enter product id: ")
                r.delete_product(product_id)
            
            elif i==4:
                customer_id=input("Enter customer id: ")
                r.delete_customer(customer_id)
                
            elif i==5:
                customer_id=input("Enter customer id: ")
                product_id=input("Enter product id: ")
                quantity=input("Enter the product quantity: ")
                r.addTocart(customer_id,product_id,quantity)
                
            elif i==6:
                customer_id=input("Enter customer id: ")
                product_id=input("Enter product id: ")
                r.removefromcart(customer_id,product_id)
                
            elif i==7:
                customer_id=input("Enter customer id: ")
                r.getallfromcart(customer_id)
                if len(r.getallfromcart(customer_id)) == 0:
                    print('\nYour Cart is Empty...')
                    continue
                print('\nFollowing are the Cart Items :\n*ProductName-(Qty)*')
                for product_name, quantity in r.getallfromcart(customer_id).items():
                    print(f'> {self.retrieveProductObject(name).get_name()}-({quantity})')
                
            elif i==8:
                print("Thank you")
                break
            else:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    Main.main()