import sqlite3
import os 
from dotenv import load_dotenv
load_dotenv() 
from typing import Final  

DbServer:Final=os.getenv("DbServer")
DbName:Final=os.getenv("DbName")

#creating the connection
conn=sqlite3.connect("BotDb.db")
cursor=conn.cursor()

#adding tables
#  conn.executemany("""
#      CREATE TABLE Category (
#          CategoryID INTEGER PRIMARY KEY AUTOINCREMENT, 
#          CatName TEXT NOT NULL, 
#          CreatedAt DATE NOT NULL, 
#          UpdatedAt DATE NOT NULL
#      );

#      CREATE TABLE Products (
#          ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
#          ProName TEXT NOT NULL, 
#          ProStock INTEGER NOT NULL,
#          ProPrice FLOAT NOT NULL,
#          CategoryID INTEGER NOT NULL, 
#          CreatedAt DATE NOT NULL,
#          UpdatedAt DATE NOT NULL, 
#          Describtion TEXT,
#          FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
#      );
    
#      CREATE TABLE Customers (
#          CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
#          CustomerName TEXT NOT NULL, 
#          CustFamilyname TEXT NOT NULL, 
#          Adress TEXT NOT NULL, 
#          PhoneNumber TEXT UNIQUE
#      );
                   
#      CREATE TABLE Orders (
#          OrderID INTEGER PRIMARY KEY AUTOINCREMENT, 
#          CustomerID INTEGER NOT NULL,
#          OrderDate DATE NOT NULL,
#          FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
#      );

#      CREATE TABLE Admin(
#          AdminId INTEGER PRIMARY KEY AUTOINCREMENT, 
#          Username TEXT NOT NULL UNIQUE, 
#          Password TEXT NOT NULL, 
#          OrderID INTEGER NOT NULL, 
#          ProductID INTEGER NOT NULL,
#          Role TEXT DEFAULT 'manager',  
#          CreatedAt DATE NOT NULL, 
#          LastLogin DATETIME,
#          FOREIGN KEY (OrderID) REFERENCES Orders(OrderID), 
#          FOREIGN KEY (ProductID) REFERENCES Orders (ProductID)

#      );
#     CREATE TABLE Order(
#         OrderItemID INTEGER PRIMARY KEY AUTOINCREMENT,
#         OrderID INTEGER NOT NULL,
#         ProductID INTEGER NOT NULL,
#         Quantity INTEGER NOT NULL,
#         UnitPrice FLOAT NOT NULL,
#         FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
#         FOREIGN KEY (ProductID) REFERENCES Products(ProductID)) 
    
#  """)

#now lets create view, a virtual table based on the result of a SELECT query to make our search easier. It doesn't store data itselfbut simplifies complex queries 
# conn.executemany("""
#     CREATE VIEW CustomerReview AS
#     SELECT 
#         Customers.CustomerName || ' ' || Customers.CustFamilyname AS FullName, 
#         Orders.OrderID, 
#         OrderItems.ProductID,
#         Products.ProName, 
#         OrderItems.Quantity, 
#         OrderItems.UnitPrice, 
#         (OrderItems.Quantity * OrderItems.UnitPrice) AS TotalPrice 
#     FROM Orders
#     JOIN Customers ON Orders.CustomerID = Customers.CustomerID
#     JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
#     JOIN Products ON OrderItems.ProductID = Products.ProductID;

#     CREATE VIEW OrderSummary AS
#     SELECT 
#         Category.CategoryID, 
#         Products.ProductID,
#         Products.ProName, 
#         OrderItems.Quantity, 
#         OrderItems.UnitPrice, 
#         Customers.CustomerName || ' ' || Customers.CustFamilyname AS FullName,
#         (OrderItems.Quantity * OrderItems.UnitPrice) AS TotalPrice 
#     FROM Orders
#     JOIN Customers ON Orders.CustomerID = Customers.CustomerID
#     JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
#     JOIN Products ON OrderItems.ProductID = Products.ProductID
#     JOIN Category ON Products.CategoryID = Category.CategoryID;
#     CREATE VIEW TopSellingProducts AS
# SELECT 
#     Products.ProductID,
#     Products.ProName,
#     SUM(OrderItems.Quantity) AS TotalSold,
#     SUM(OrderItems.Quantity * OrderItems.UnitPrice) AS TotalRevenue
# FROM OrderItems
# JOIN Products ON OrderItems.ProductID = Products.ProductID
# GROUP BY Products.ProductID, Products.ProName
# ORDER BY TotalSold DESC;

# """)


#Building Triggers, a statement that executes when there's a modifaction to database
# conn.executescript(""" 
# CREATE TRIGGER ReduceStockAfterOrder
#     AFTER INSERT ON OrderItems
#     FOR EACH ROW
#     BEGIN
#         UPDATE Products
#         SET ProStock = ProStock - NEW.Quantity
#         WHERE ProductID = NEW.ProductID;
#     END;
#     CREATE TRIGGER PreventOverOrder
#     BEFORE INSERT ON OrderItems
#     FOR EACH ROW
#     WHEN (SELECT ProStock FROM Products WHERE ProductID = NEW.ProductID) < NEW.Quantity
#     BEGIN
#         SELECT RAISE(ABORT, 'Not enough stock available.');
#     END;
#     CREATE TRIGGER RestoreStockAfterDelete
#     AFTER DELETE ON OrderItems
#     FOR EACH ROW
#     BEGIN
#         UPDATE Products
#         SET ProStock = ProStock + OLD.Quantity
#         WHERE ProductID = OLD.ProductID;
#     END;
#     CREATE TRIGGER UPDATESTOCK
#     AFTER UPDATE ON OrderItems
#     FOR EACH ROW
#     BEGIN
#         UPDATE Products
#         SET ProStock = ProStock + OLD.Quantity - NEW.Quantity
#         WHERE ProductID = NEW.ProductID;
#     END;
#     CREATE TRIGGER UpdateProductTimestamp
#     AFTER UPDATE ON Products
#     FOR EACH ROW
#     BEGIN
#         UPDATE Products
#         SET UpdatedAt = CURRENT_DATE
#         WHERE ProductID = NEW.ProductID;
#     END;   
#      CREATE TABLE ProductLog (
#     LogID INTEGER PRIMARY KEY AUTOINCREMENT,
#     ProductID INTEGER,
#     Action TEXT,
#     LogDate DATETIME DEFAULT CURRENT_TIMESTAMP
# );

#     CREATE TRIGGER LogProductInsert
#     AFTER INSERT ON Products
#     FOR EACH ROW
#     BEGIN
#         INSERT INTO ProductLog (ProductID, Action)
#         VALUES (NEW.ProductID, 'INSERT');
#     END;                              
#     CREATE TRIGGER UpdateCustomer
#     AFTER UPDATE ON Customers
#     FOR EACH ROW
#     BEGIN
#         UPDATE Customers SET UpdatedAt = DATE('now') WHERE CustomerID = NEW.CustomerID;
#     END;
#     CREATE TRIGGER UpdateOrderTimestamp
#     AFTER UPDATE ON Orders
#     FOR EACH ROW
#     BEGIN
#         UPDATE Orders SET UpdatedAt = DATE('now') WHERE OrderID = NEW.OrderID;
#     END;
#     CREATE TABLE ChangeLog (
#         LogID INTEGER PRIMARY KEY AUTOINCREMENT,
#         TableName TEXT,
#         Action TEXT,
#         RecordID INTEGER,
#         LogDate DATETIME DEFAULT CURRENT_TIMESTAMP
#     );
#     CREATE TRIGGER LogCustomerInsert
#     AFTER INSERT ON Customers
#     FOR EACH ROW
#     BEGIN
#         INSERT INTO ChangeLog (TableName, Action, RecordID)
#         VALUES ('Customers', 'INSERT', NEW.CustomerID);
#     END;
#     CREATE TRIGGER LogOrderInsert
#     AFTER INSERT ON Orders
#     FOR EACH ROW
#     BEGIN
#         INSERT INTO ChangeLog (TableName, Action, RecordID)
#         VALUES ('Orders', 'INSERT', NEW.OrderID);
#     END;

# # """)
conn.commit()
conn.close()