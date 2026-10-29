def calculate_rankings(teams, matches):
    stats = {team: {"P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "GD": 0, "Pts": 0} for team in teams}
    
    for home, away, home_score, away_score in matches:
        stats[home]["P"] += 1
        stats[away]["P"] += 1
        stats[home]["GF"] += home_score
        stats[home]["GA"] += away_score
        stats[away]["GF"] += away_score
        stats[away]["GA"] += home_score
        
        if home_score > away_score:
            stats[home]["W"] += 1
            stats[home]["Pts"] += 3
            stats[away]["L"] += 1
        elif home_score < away_score:
            stats[away]["W"] += 1
            stats[away]["Pts"] += 3
            stats[home]["L"] += 1
        else:
            stats[home]["D"] += 1
            stats[home]["Pts"] += 1
            stats[away]["D"] += 1
            stats[away]["Pts"] += 1
            
    for team in stats:
        stats[team]["GD"] = stats[team]["GF"] - stats[team]["GA"]
        
    ranked_teams = sorted(
        stats.items(),
        key=lambda x: (x[1]["Pts"], x[1]["GD"], x[1]["GF"]),
        reverse=True
    )
    
    standings = []
    for rank, (team, data) in enumerate(ranked_teams, start=1):
        standings.append({
            "Rank": rank,
            "Team": team,
            "P": data["P"],
            "W": data["W"],
            "D": data["D"],
            "L": data["L"],
            "GF": data["GF"],
            "GA": data["GA"],
            "GD": data["GD"],
            "Pts": data["Pts"]
        })
        
    return standings


if __name__ == "__main__":
    teams = ["Team Alpha", "Team Beta", "Team Gamma", "Team Delta"]
    matches = [
        ("Team Alpha", "Team Beta", 2, 1),
        ("Team Gamma", "Team Delta", 0, 0),
        ("Team Alpha", "Team Gamma", 1, 1),
        ("Team Beta", "Team Delta", 3, 2),
        ("Team Alpha", "Team Delta", 4, 1),
        ("Team Beta", "Team Gamma", 2, 2)
    ]
    
    standings = calculate_rankings(teams, matches)
    
    print("Rank | Team       | P | W | D | L | GF | GA | GD | Pts")
    print("-" * 55)
    for s in standings:
        print(f"{s['Rank']:<4} | {s['Team']:<10} | {s['P']} | {s['W']} | {s['D']} | {s['L']} | {s['GF']} | {s['GA']} | {s['GD']:+2d} | {s['Pts']}")
