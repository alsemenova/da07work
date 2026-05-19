-- 07_SQL_lab/2.sql: Вывод женских аккаунтов, зарегистрированных до 2020-01-01.
SELECT Account_Name
FROM user_data
WHERE Gender = 'Female'
    AND Date_Joined < '2020-01-01';