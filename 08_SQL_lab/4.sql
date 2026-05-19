-- 08_SQL_lab/4.sql: Number of orders grouped by order date.
SELECT OrderDate,
    COUNT(Quantity) AS OrderCount
FROM Orders
GROUP BY OrderDate;