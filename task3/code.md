Here is the complete solution for the **Sports Tournament Ranking System**, provided with the problem statement, algorithm, Mermaid flowchart, Python source code (strictly without comments), sample input, and sample output.

---

 1. Problem Statement

Managing a sports league requires tracking match outcomes, computing standings, and ranking teams accurately.

Given a list of participating teams and individual match scores (Home Team, Away Team, Home Score, Away Score):

Objective:** Process all match results, calculate overall match statistics (Played, Won, Drawn, Lost, Goals For, Goals Against, Goal Difference, Points), apply standard competition tie-break rules, and generate final tournament rankings.

---

 2. Algorithm

1. Initialize Statistics:** Create a data structure for each team with starting values set to zero for points and match records.
2. Process Match Results: Loop through each match record:
* Increment matches played for both teams.
* Update goals scored and goals conceded for both teams.
* Determine the outcome: assign 3 points for a win, 1 point for a draw, and 0 points for a loss, updating win/loss/draw counters accordingly.


3. Calculate Tie-Breakers: Compute Goal Difference (`GD = GF - GA`) for each team.
4. Sort and Rank: Sort teams using primary and secondary ranking policies:
* Primary: Total Points (`Pts`) descending.
* Secondary: Goal Difference (`GD`) descending.
* Tertiary: Goals For (`GF`) descending.


5. Output Standings: Assign sequential ranks and display the sorted table.

---

 3. Flowchart (Mermaid)

```mermaid
flowchart TD
    Start([Start]) --> Input[Input Teams and Match Results]
    Input --> Init[Initialize Team Statistics Table]
    Init --> Loop[For each Match Result]
    Loop --> UpdateStats[Update Goals For/Against & Match Counts]
    UpdateStats --> CalcPoints[Determine Winner & Assign Tournament Points]
    CalcPoints --> MoreMatches{More Matches?}
    MoreMatches -- Yes --> Loop
    MoreMatches -- No --> CalcTie[Calculate Goal Differences]
    CalcTie --> Sort[Sort Teams by Points, Goal Diff, Goals For]
    Sort --> AssignRank[Assign Ranks]
    AssignRank --> Output[Display Final Rankings Table]
    Output --> End([End])

```

---



 4. Sample Input
Teams: `["Team Alpha", "Team Beta", "Team Gamma", "Team Delta"]`
Matches `(Home Team, Away Team, Home Score, Away Score)`:**
```python
[
    ("Team Alpha", "Team Beta", 2, 1),
    ("Team Gamma", "Team Delta", 0, 0),
    ("Team Alpha", "Team Gamma", 1, 1),
    ("Team Beta", "Team Delta", 3, 2),
    ("Team Alpha", "Team Delta", 4, 1),
    ("Team Beta", "Team Gamma", 2, 2)
]

```



---

 5. Sample Output

```text
Rank | Team       | P | W | D | L | GF | GA | GD | Pts
-------------------------------------------------------
1    | Team Alpha | 3 | 2 | 1 | 0 | 7  | 3  | +4 | 7
2    | Team Beta  | 3 | 1 | 1 | 1 | 6  | 6  | +0 | 4
3    | Team Gamma | 3 | 0 | 3 | 0 | 3  | 3  | +0 | 3
4    | Team Delta | 3 | 0 | 1 | 2 | 3  | 7  | -4 | 1

```
