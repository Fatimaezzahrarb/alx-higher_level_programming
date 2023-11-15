-- list all cities of California that could be found in database hbtn_0d_usa
-- list all the rows of a column in a database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
