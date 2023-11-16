-- List all the records of table second_table by having a name value in my MySQL server.
-- Records are instructed by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
