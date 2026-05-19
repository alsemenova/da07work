-- 07_SQL_lab/3.sql: Аккаунты с более чем 100 постами и менее чем 500 лайками.
SELECT Account_Name,
    Posts,
    Likes
FROM user_data
WHERE Posts > 100
    AND Likes < 500;