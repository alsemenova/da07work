-- 08_SQL_lab/1.sql: Total sales amount for each customer.
SELECT Customers.CustomerName,
    SUM(Orders.Total) AS TotalSales
FROM Orders
    JOIN Customers ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerName;