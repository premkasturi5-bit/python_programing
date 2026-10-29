def evaluate_admissions(applicants, criteria, available_seats):
    eligible_pool = []
    rejection_log = []
    
    min_aggregate = criteria["min_aggregate"]
    min_core_subject = criteria["min_core_subject"]
    
    for applicant in applicants:
        name, core_mark, aggregate, entrance_score = applicant
        
        if core_mark < min_core_subject:
            rejection_log.append((name, f"Failed core subject threshold ({core_mark} < {min_core_subject})"))
            continue
            
        if aggregate < min_aggregate:
            rejection_log.append((name, f"Failed aggregate threshold ({aggregate} < {min_aggregate})"))
            continue
            
        eligible_pool.append({
            "name": name,
            "core_mark": core_mark,
            "aggregate": aggregate,
            "entrance_score": entrance_score
        })
        
    eligible_pool.sort(
        key=lambda x: (x["entrance_score"], x["aggregate"], x["core_mark"]),
        reverse=True
    )
    
    admitted = []
    waitlisted = []
    
    for index, candidate in enumerate(eligible_pool):
        if index < available_seats:
            candidate["status"] = "Admitted"
            admitted.append(candidate)
        else:
            candidate["status"] = "Waitlisted"
            waitlisted.append(candidate)
            
    return admitted, waitlisted, rejection_log


if __name__ == "__main__":
    criteria = {
        "min_aggregate": 75.0,
        "min_core_subject": 70
    }
    available_seats = 3
    
    applicants = [
        ("Alice Smith", 85, 88.5, 92),
        ("Bob Jones", 65, 82.0, 88),
        ("Charlie Brown", 90, 91.0, 95),
        ("Diana Prince", 78, 80.0, 85),
        ("Ethan Hunt", 72, 74.5, 70),
        ("Fiona Gallagher", 88, 88.5, 92)
    ]
    
    admitted, waitlisted, rejections = evaluate_admissions(applicants, criteria, available_seats)
    
    print("=== REJECTION LOG ===")
    for name, reason in rejections:
        print(f"{name}: {reason}")
        
    print("\n=== ADMISSION & WAITLIST RANKINGS ===")
    print("Rank | Status     | Name            | Entrance | Aggregate | Core")
    print("-" * 60)
    
    combined = admitted + waitlisted
    for rank, c in enumerate(combined, start=1):
        print(f"{rank:<4} | {c['status']:<10} | {c['name']:<15} | {c['entrance_score']:<8} | {c['aggregate']:<9} | {c['core_mark']}")
