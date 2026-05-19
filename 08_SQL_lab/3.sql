-- 08_SQL_lab/3.sql: Total revenue for each product.
SELECT Products.ProductName,
    SUM(Orders.Total) AS TotalRevenue
FROM Orders
    JOIN Products ON Orders.ProductID = Products.ProductID
GROUP BY Products.ProductName;