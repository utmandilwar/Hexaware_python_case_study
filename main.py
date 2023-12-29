from serviceprovider import serviceprovider

class Main():

    def main():
        r=serviceprovider()
        while True:
            print("\n----------Main Menu----------")
            print("\nPress-1 create product")
            print("Press-2 create customer")
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
                password=input("Enter password ")
                if r.customer_exists(name,password)>0:
                    print("customer already exists")
                else:
                    email=input("Enter mai id: ")
                    r.create_customer(name, email, password)
            elif i==3:
                print("Thank you")
                break
            else:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    Main.main()