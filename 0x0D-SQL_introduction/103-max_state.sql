-- script that displays the max temperature of each state (ordered by State name).

USE hbtn_0c_0;
SELECT State, MAX(Temperature) as Max_Temperature FROM Temperatures GROUP BY State ORDER BY State;
