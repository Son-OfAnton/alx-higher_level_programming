-- list all records on some that has name in descending order of score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
