-- 07_SQL_lab/5.sql: Суммарное количество лайков по гендеру.
SELECT Gender,
    SUM(Likes) AS Total_Likes
FROM user_data
GROUP by Gender;