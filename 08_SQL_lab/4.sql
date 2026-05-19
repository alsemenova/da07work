-- 08_SQL_lab/4.sql: Количество заказов по датам.
SELECT OrderDate,
    COUNT(Quantity) AS OrderCount
FROM Orders
GROUP BY OrderDate;