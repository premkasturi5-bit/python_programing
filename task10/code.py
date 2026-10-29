def calculate_water_bills(households, slabs, fixed_fee, excessive_threshold, penalty_amount):
    billing_reports = []
    
    for name, consumption in households:
        remaining = consumption
        tier_cost = 0.0
        
        for limit, rate in slabs:
            if remaining <= 0:
                break
            slab_usage = min(remaining, limit)
            tier_cost += slab_usage * rate
            remaining -= slab_usage
            
        if remaining > 0:
            highest_rate = slabs[-1][1]
            tier_cost += remaining * highest_rate
            
        total_bill = tier_cost + fixed_fee
        is_excessive = consumption > excessive_threshold
        
        penalty = 0.0
        if is_excessive:
            penalty = penalty_amount
            total_bill += penalty
            
        billing_reports.append({
            "household": name,
            "consumption": consumption,
            "base_cost": round(tier_cost, 2),
            "fixed_fee": fixed_fee,
            "penalty": penalty,
            "total_bill": round(total_bill, 2),
            "status": "Excessive" if is_excessive else "Normal"
        })
        
    return billing_reports


if __name__ == "__main__":
    tariff_slabs = [
        (15.0, 1.20),   # Tier 1: Up to 15 KL @ $1.20 per KL
        (15.0, 2.50),   # Tier 2: Next 15 KL (15 to 30 KL) @ $2.50 per KL
        (float('inf'), 4.50)  # Tier 3: Above 30 KL @ $4.50 per KL
    ]
    
    fixed_service_fee = 15.0
    excessive_usage_threshold = 40.0
    penalty_surcharge = 30.0
    
    households_data = [
        ("Greenwood Villa", 12.0),
        ("Maple Heights", 28.0),
        ("Oakridge Estate", 45.0),
        ("Pinecrest Apt", 10.0),
        ("Sunrise Manor", 55.0)
    ]
    
    reports = calculate_water_bills(
        households_data, 
        tariff_slabs, 
        fixed_service_fee, 
        excessive_usage_threshold, 
        penalty_surcharge
    )
    
    print("=== PROGRESSIVE WATER TARIFF ANALYSIS REPORT ===")
    print("Household      | Usage (KL) | Base Cost | Fixed | Penalty | Total Bill | Status")
    print("-" * 78)
    for r in reports:
        print(f"{r['household']:<14} | {r['consumption']:<10} | ${r['base_cost']:<8} | ${r['fixed_fee']:<5} | ${r['penalty']:<7} | ${r['total_bill']:<10} | {r['status']}")
