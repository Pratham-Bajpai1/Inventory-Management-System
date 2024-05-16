-- CREATE DATABASE / SCHEMA
CREATE DATABASE Inventory; 

-- CREATE CATEGORIES TABLE 
CREATE TABLE Categories ( 
  CategoryID INT, 
  CategoryName VARCHAR(255) NOT NULL 

); 
--INSERT DATA IN CATEGORIES TABLE
INSERT INTO Categories (CategoryID, CategoryName) 
VALUES (1, 'Electronics'), 
       (2, 'Clothing'), 
       (3, 'Groceries'); 

-- CREATE SUPPLIERS TABLE 
CREATE TABLE Suppliers ( 
  SupplierID INT PRIMARY KEY, 
  SupplierName VARCHAR(255) NOT NULL, 
  ContactPerson VARCHAR(255) NOT NULL, 
  PhoneNumber VARCHAR(15) NOT NULL 
); 
--INSERT DATA IN SUPPLIER TABLE
INSERT INTO Suppliers (SupplierID, SupplierName, ContactPerson, PhoneNumber) 
VALUES (1, 'Switch On', 'Rajesh Bajpai', '9826547411'),  
       (21, 'Sparsh Khasgiwale', 'Sparsh', ‘8309083648’);  

-- CREATE PRODUCTS TABLE 
CREATE TABLE Products ( 
  ProductID INT PRIMARY KEY, 
  ProductName VARCHAR(255) NOT NULL, 
  Price DECIMAL(10, 2) NOT NULL, 
  Quantity INT NOT NULL, 
  SupplierID INT NOT NULL, 
  FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) 
  ON DELETE CASCADE 
); 
--INSERT DATA IN PRODUCTS TABLE 
INSERT INTO Products (ProductID, ProductName, Price, Quantity, SupplierID) 
VALUES (1, 'Laptop', 999.99, 10, 1),  (2, 'T-Shirt', 19.99, 50, 1), 
       (3, 'Apple', 50.00, 100, 1); 

-- CREATE CUSTOMERS TABLE 
CREATE TABLE Customers ( 
  CustomerID INT PRIMARY KEY, 
  CustomerName VARCHAR(255) NOT NULL, 
  Address TEXT NOT NULL, 
  PhoneNumber VARCHAR(15) NOT NULL, 
); 
--INSERT DATA IN CUSTOMERS TABLE
INSERT INTO Customers (CustomerID, CustomerName, Address, PhoneNumber) 
VALUES (1, 'Pratham Bajpai', 'Bada, Gwalior', '8770483647'); 

-- CREATE ORDERS TABLE 
CREATE TABLE Orders ( 
  OrderID INT PRIMARY KEY, 
  OrderDate DATE NOT NULL, 
  CustomerID INT NOT NULL, 
  ProductID INT NOT NULL, 
  Quantity INT NOT NULL, 
  TotalPrice DECIMAL(10, 2) NOT NULL, 
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID), 
  FOREIGN KEY (ProductID) REFERENCES Products(ProductID) 
  ON DELETE CASCADE 
); 
--INSERT DATA 
INSERT INTO Orders (OrderID, OrderDate, CustomerID, ProductID, Quantity, TotalPrice) 
VALUES (1, '2023-03-10', 1, 1, 2, 1999.98), 
       (2, '2023-03-11', 1, 2, 3, 59.97), 
       (3, '2023-03-11', 1, 3, 10, 9.90);