-- A script that updates the score of Bob to 10 in the table second_table
-- Bobs id value is not allowed to be used, only the name field
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
