import mysql.connector

# connect to the database
db = mysql.connector.connect(
  host="localhost", # Enter host, check in server feature of mysql workbench.
  user="root", # Enter user which was set in mysql workbench.
  password="122pp", # Enter password which was set in mysql workbench.
  database="inventory" # Enter database/schema name which was made in mysql workbench.
)

# create a cursor object to execute SQL queries
cursor = db.cursor()

# add a category to the inventory
def add_category(CategoryID, CategoryName):
    sql = "INSERT INTO categories (CategoryID, CategoryName) VALUES (%s, %s)"
    val = (CategoryID, CategoryName)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "category added to inventory")

# delete a category from the inventory
def delete_category(CategoryID):
    sql = "DELETE FROM categories WHERE CategoryID = %s"
    val = (CategoryID,)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "category deleted")


# view all category
def view_category():
    cursor.execute("SELECT * FROM categories")
    results = cursor.fetchall()
    print("\nCategoryID", "CategoryName")
    for category in results:
        print(category)

# add a suppliers to the inventory
def add_suppliers(SupplierID, SupplierName, ContactPerson, PhoneNumber):
    sql = "INSERT INTO suppliers (SupplierID, SupplierName, ContactPerson, PhoneNumber) VALUES (%s, %s, %s, %s)"
    val = (SupplierID, SupplierName, ContactPerson, PhoneNumber)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "supplier added to inventory")

# view all suppliers
def view_suppliers():
    cursor.execute("SELECT * FROM suppliers")
    results = cursor.fetchall()
    print("\nSupplierID", "SupplierName", "ContactPerson", "PhoneNumber")
    for suppliers in results:
        print(suppliers)

# add a product to the inventory
def add_product(ProductID, ProductName, Price, Quantity, SupplierID):
    sql = "INSERT INTO products (ProductID, ProductName, Price, Quantity, SupplierID) VALUES (%s, %s, %s, %s, %s)"
    val = (ProductID, ProductName, Price, Quantity, SupplierID)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "product added to inventory")

# update a product in the inventory
def update_product(ProductName, Price, Quantity, SupplierID, ProductID):
    sql = "UPDATE products SET ProductName=%s, Price=%s, Quantity=%s, SupplierID=%s WHERE ProductID=%s"
    val = (ProductName, Price, Quantity, SupplierID, ProductID)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "product updated")

# delete a product from the inventory
def delete_product(ProductID):
    sql = "DELETE FROM products WHERE ProductID = %s"
    val = (ProductID,)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "product deleted")

# display all products in the inventory
def view_product():
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    print("\nProductID", "ProductName", "Price", "Quantity", "SupplierID")
    for product in results:
        print(product)

# add a customer to the inventory
def add_customers(CustomerID, CustomerName, Address, PhoneNumber):
    sql = "INSERT INTO customers (CustomerID, CustomerName, Address, PhoneNumber) VALUES (%s, %s, %s, %s)"
    val = (CustomerID, CustomerName, Address, PhoneNumber)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "customer added to inventory")

 # view all customers
def view_customers():
    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    print("\nCustomerID", "CustomerName","Address", "PhoneNumber")
    for customers in results:
        print(customers)

# add a order to the inventory
def add_order(OrderID, OrderDate, CustomerID, ProductID, Quantity, TotalPrice):
    sql = "INSERT INTO orders (OrderID, OrderDate, CustomerID, ProductID, Quantity, TotalPrice) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (OrderID, OrderDate, CustomerID, ProductID, Quantity, TotalPrice)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "order added to inventory")

# view all orders
def view_orders():
    cursor.execute("SELECT * FROM orders")
    results = cursor.fetchall()
    print("\nOrderID", "OrderDate", "CustomerID", "ProductID", "Quantity", "TotalPrice")
    for orders in results:
        print(orders)

# interact with the user
print("--------------Welcome in Inventory Management System---------------")
username = "pratham014"
password = "54321pb"
name = input("Enter username: ")
passw = input("Enter password: ")

while True:
    if name == username:
        if passw == password:
            print("Successfully Login\n")
            print("What would you like to do?")
            print("1. For Category")
            print("2. For Suppliers")
            print("3. For Product")
            print("4. For Customers")
            print("5. For Orders")
            print("6. Quit")

            choice = int(input("Enter Number: "))

            if choice == 1:
                print("1. ADD Category")
                print("2. DELETE Category")
                print("3. VIEW Category")
                ctg = int(input("Enter: "))

                if ctg == 1:
                    id = int(input("Enter Category ID: "))
                    name = input("Enter Category Name: ")
                    add_category(id, name)
                    print("\n")
                
                elif ctg == 2:
                    id = int(input("Enter Category ID:"))
                    delete_category(id)
                    print("\n")

                elif ctg == 3:
                    view_category()
                    print("\n")

                else:
                    print("Enter Valid Number!")
                    print("\n")

            elif choice == 2:
                print("1. ADD Suppliers")
                print("2. VIEW Suppliers")
                supp = int(input("Enter: "))

                if supp == 1:
                    id = int(input("Enter Supplier ID: "))
                    name = input("Entter Supplier Name: ")
                    cp = input("Enter Contact Person: ")
                    phone = input("Enter Phone Number: ")
                    add_suppliers(id, name, cp, phone)
                    print("\n")
                    
                elif supp == 2:
                    view_suppliers()
                    print("\n")

                else:
                    print("Enter Valid Number!")
                    print("\n")

            elif choice == 3:
                print("1. ADD Product")
                print("2. UPDATE Product")
                print("3. DELETE Product")
                print("4. VIEW Product")
                prd = int(input("Enter: "))

                if prd == 1:
                    id = int(input("Enter Product ID: "))
                    name = input("Enter Product Name: ")
                    price = int(input("Enter Price: "))
                    quantity = int(input("Enter Quantity: "))
                    sid = int("Enter Supplier ID: ")
                    add_product(id, name, price, quantity, sid)
                    print("\n")

                elif prd == 2:
                    name = input("Enter Product Name: ")
                    price = int(input("Enter Price: "))
                    quantity = int(input("Enter Quantity: "))
                    sid = int("Enter Supplier ID: ")
                    id = int(input("Enter Product ID: "))
                    update_product(name, price, quantity, sid, id)
                    print("\n")

                elif prd == 3:
                    id = int(input("Enter Product ID: "))
                    delete_product(id)
                    print("\n")

                elif prd == 4:
                    view_product()
                    print("\n")

                else:
                    print("Enter Valid Number!")
                    print("\n")

            elif choice == 4:
                print("1. ADD Customer: ")
                print("2. VIEW Customer: ")
                cus = int(input("Enter: "))

                if cus == 1:
                    id = int(input("Enter Customer ID: "))
                    name = input("Enter Customer Name: ")
                    add = input("Enter Customer Address: ")
                    phone = input("Enter Customer PhoneNumber: ")
                    add_customers(id, name, add, phone)
                    print("\n")

                elif cus == 2:
                    view_customers()
                    print("\n")

                else:
                    print("Enter Valid Number!")
                    print("\n")

            elif choice == 5:
                print("1. ADD Order")
                print("2. View Order")
                od = int(input("Enter: "))

                if od == 1:
                    id = int(input("Enter Order ID: "))
                    date = input("Enter Order Date: ")
                    cusid = int(input("Enter Customer ID: "))
                    prodid = int(input("Enter Product ID: "))
                    quantity = int(input("Enter Quantity: "))
                    tp = int(input("Enter Total Price: "))
                    add_order(id, name, cusid, prodid, quantity, tp)
                    print("\n")
                    
                elif od == 2:
                    view_orders()
                    print("\n")

            elif choice == 6:
                print("THANK YOU !")
                break

            else:
                print("Invalid choice! Please try again.")
                print("\n")

        else:
            print("Wrong Password!")
            break

    else:
        print("Password doest not match with username!")
        break