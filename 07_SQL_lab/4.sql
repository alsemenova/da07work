-- 07_SQL_lab/4.sql: Подсчёт пользователей, присоединившихся после 2020-01-01.
SELECT COUNT(User_ID) AS User_Count
FROM user_data
WHERE Date_Joined > '2020-01-01';