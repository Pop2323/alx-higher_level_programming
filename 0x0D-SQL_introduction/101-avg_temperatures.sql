-- script that displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending).

SELECT `city` AVG(value) AS `avg_tmp`
from `temperatures`
GROUP BY `city`
GROUP BY `avg_tmp` DESC;
