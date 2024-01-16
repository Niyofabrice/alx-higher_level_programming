-- computes the maximum by column of a group of records in a table
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
