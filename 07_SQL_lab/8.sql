-- 07_SQL_lab/8.sql: Топ-3 аккаунта по количеству лайков.
SELECT Account_Name,
    Likes
FROM user_data
ORDER BY Likes DESC
LIMIT 3;