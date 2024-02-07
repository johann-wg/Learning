-- 코드를 입력하세요
SELECT COUNT(user_id) AS USERS
FROM user_info
WHERE TO_CHAR(joined, 'YYYY') = '2021'
AND age >= 20
AND age <= 29;
