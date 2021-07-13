-- This script creates a database and a table
SELECT cities.id, cities.name
FROM states, cities
WHERE states.id = cities.state_id AND
	states.name = 'California'

