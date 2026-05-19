-- 08_SQL_lab/2.sql: Наиболее продаваемый продукт по количеству заказанных штук.
SELECT Products.ProductName,
    SUM(Orders.Quantity) AS TotalQuantity
FROM Orders
    JOIN Products ON Orders.ProductID = Products.ProductID
GROUP BY Products.ProductName
ORDER BY TotalQuantity DESC
LIMIT 1;