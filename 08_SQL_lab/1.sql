-- 08_SQL_lab/1.sql: Общая сумма продаж по каждому клиенту.
SELECT Customers.CustomerName,
    SUM(Orders.Total) AS TotalSales
FROM Orders
    JOIN Customers ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerName;