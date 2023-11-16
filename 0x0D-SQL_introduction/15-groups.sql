-- List number of the records with same score in table second_table in my MySQL server.
-- Records are instructed by descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
