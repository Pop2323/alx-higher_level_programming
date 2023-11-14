-- script that displays the max temperature of each state (ordered by State name).

SELECT State, MAX(Temperature) as Max_Temperature FROM Temperatures GROUP BY State ORDER BY State;
