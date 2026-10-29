def process_hackathon_teams(teams_data, min_size=2, max_size=4):
    valid_teams = []
    errors = []
    
    for team_name, members, rounds in teams_data:
        if not (min_size <= len(members) <= max_size):
            errors.append(f"Team '{team_name}' rejected: Invalid member count ({len(members)}). Allowed: {min_size}-{max_size}.")
            continue
        
        total_score = sum(rounds)
        final_round_score = rounds[-1] if rounds else 0
        
        valid_teams.append({
            "team_name": team_name,
            "members": members,
            "rounds": rounds,
            "total_score": total_score,
            "final_round_score": final_round_score
        })
        
    valid_teams.sort(key=lambda x: (x["total_score"], x["final_round_score"], x["team_name"]), reverse=True)
    
    ranked_teams = []
    for rank, team in enumerate(valid_teams, start=1):
        ranked_teams.append({
            "rank": rank,
            "team_name": team["team_name"],
            "members": team["members"],
            "total_score": team["total_score"]
        })
        
    return ranked_teams, errors


if __name__ == "__main__":
    teams_data = [
        ("CodeStorm", ["Alice", "Bob", "Charlie"], [85, 90, 95]),
        ("ByteForce", ["David", "Eve"], [90, 85, 95]),
        ("NullPointer", ["Frank", "Grace", "Heidi"], [80, 80, 90]),
        ("SoloCoders", ["Ivan"], [95, 95, 95]),
        ("SyntaxError", ["Jack", "Mallory", "Niaj", "Olivia", "Peggy"], [70, 70, 70]),
        ("BitCrafters", ["Syed", "Zack", "John"], [85, 90, 95])
    ]
    
    rankings, validation_errors = process_hackathon_teams(teams_data, min_size=2, max_size=4)
    
    print("=== VALIDATION & ELIGIBILITY REPORT ===")
    for err in validation_errors:
        print(err)
        
    print("\n=== FINAL HACKATHON LEADERBOARD ===")
    print("Rank | Team Name    | Total Score | Members")
    print("-" * 50)
    for r in rankings:
        members_str = ", ".join(r['members'])
        print(f"{r['rank']:<4} | {r['team_name']:<12} | {r['total_score']:<11} | {members_str}")
