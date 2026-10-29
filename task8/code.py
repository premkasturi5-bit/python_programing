from datetime import datetime, timedelta

def calculate_parking_fee(entry_str, exit_str, category):
    try:
        entry_time = datetime.strptime(entry_str, "%Y-%m-%d %H:%M")
        exit_time = datetime.strptime(exit_str, "%Y-%m-%d %H:%M")
    except ValueError:
        return {"error": "Invalid date/time format. Use YYYY-MM-DD HH:MM"}
        
    if exit_time <= entry_time:
        return {"error": "Exit time must be later than entry time."}
        
    duration = exit_time - entry_time
    total_hours = duration.total_seconds() / 3600
    
    rates = {
        "Car": {"hourly": 10.0, "daily_max": 120.0, "overnight": 20.0},
        "Bike": {"hourly": 5.0, "daily_max": 50.0, "overnight": 10.0},
        "Truck": {"hourly": 20.0, "daily_max": 250.0, "overnight": 40.0}
    }
    
    if category not in rates:
        return {"error": "Invalid vehicle category."}
        
    rate_info = rates[category]
    
    days = duration.days
    remaining_hours = total_hours - (days * 24)
    
    base_fee = 0.0
    if days > 0:
        base_fee += days * rate_info["daily_max"]
    
    calculated_hourly_fee = remaining_hours * rate_info["hourly"]
    if calculated_hourly_fee > rate_info["daily_max"]:
        base_fee += rate_info["daily_max"]
    else:
        base_fee += calculated_hourly_fee
        
    overnight_fee = 0.0
    current = entry_time
    while current < exit_time:
        next_midnight = datetime(current.year, current.month, current.day) + timedelta(days=1)
        check_end = min(exit_time, next_midnight)
        
        night_start = datetime(current.year, current.month, current.day, 0, 0)
        night_end = datetime(current.year, current.month, current.day, 6, 0)
        
        if current < night_end and check_end > night_start:
            overnight_fee += rate_info["overnight"]
            
        current = next_midnight
        
    penalty = 0.0
    if total_hours > 72:
        penalty = 50.0
        
    total_fee = base_fee + overnight_fee + penalty
    
    return {
        "entry": entry_str,
        "exit": exit_str,
        "category": category,
        "total_hours": round(total_hours, 2),
        "base_fee": round(base_fee, 2),
        "overnight_fee": round(overnight_fee, 2),
        "penalty": round(penalty, 2),
        "total_fee": round(total_fee, 2)
    }

if __name__ == "__main__":
    test_cases = [
        ("2026-06-01 10:00", "2026-06-01 14:30", "Car"),
        ("2026-06-01 22:00", "2026-06-02 08:00", "Car"),
        ("2026-06-01 08:00", "2026-06-05 12:00", "Truck"),
        ("2026-06-01 12:00", "2026-06-01 10:00", "Bike")
    ]
    
    for entry, exit_t, cat in test_cases:
        res = calculate_parking_fee(entry, exit_t, cat)
        print(res)
