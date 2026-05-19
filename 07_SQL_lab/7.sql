-- 07_SQL_lab/7.sql: Среднее количество лайков для пользователей с более чем 200 подписчиками.
SELECT AVG(Likes) AS Avg_Likes
FROM user_data
WHERE Followers > 200
GROUP BY Followers;