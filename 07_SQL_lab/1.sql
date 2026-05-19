-- 07_SQL_lab/1.sql: Список аккаунтов с количеством подписчиков, сортировка по убыванию.
SELECT Account_Name, Followers
FROM user_data
ORDER BY Followers DESC;
