-- 08_SQL_lab/5.sql: Top 3 customers by total sales.
SELECT Customers.CustomerName,
    SUM(Orders.Total) AS TotalSales
FROM Orders
    JOIN Customers ON Orders.CustomerID = Customers.CustomerID
GROUP BY Customers.CustomerName
ORDER BY TotalSales DESC
LIMIT 3;