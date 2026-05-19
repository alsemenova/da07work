-- 07_SQL_lab/6.sql: Общее количество постов у всех пользователей.
Select SUM(Posts) as Total_Posts
FROM user_data;