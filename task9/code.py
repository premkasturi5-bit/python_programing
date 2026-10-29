def compare_fuel_routes(distance, fuel_price, reserve_percentage, vehicles):
    feasible_options = []
    
    for vehicle_name, mileage, tank_capacity in vehicles:
        if mileage <= 0:
            continue
            
        base_fuel = distance / mileage
        reserve_multiplier = 1.0 + (reserve_percentage / 100.0)
        total_fuel_needed = base_fuel * reserve_multiplier
        
        if total_fuel_needed > tank_capacity:
            continue
            
        journey_cost = total_fuel_needed * fuel_price
        
        feasible_options.append({
            "vehicle": vehicle_name,
            "mileage": mileage,
            "total_fuel": round(total_fuel_needed, 2),
            "journey_cost": round(journey_cost, 2)
        })
        
    if not feasible_options:
        return None, []
        
    feasible_options.sort(key=lambda x: x["journey_cost"])
    optimal_choice = feasible_options[0]
    
    return optimal_choice, feasible_options


if __name__ == "__main__":
    distance_km = 450.0
    fuel_price_per_liter = 1.25
    safety_reserve_pct = 15.0
    
    vehicle_fleet = [
        ("Sedan Efficiency", 15.0, 60.0),
        ("SUV Heavy", 9.5, 80.0),
        ("Compact Hatchback", 18.5, 45.0),
        ("Electric Crossover", 5.0, 30.0)
    ]
    
    optimal, comparison = compare_fuel_routes(distance_km, fuel_price_per_liter, safety_reserve_pct, vehicle_fleet)
    
    print(f"Route Distance: {distance_km} km | Fuel Price: ${fuel_price_per_liter}/L | Reserve: {safety_reserve_pct}%")
    print("\n=== VEHICLE COST COMPARISON REPORT ===")
    print("Vehicle Name      | Mileage (km/L) | Fuel Needed (L) | Journey Cost ($)")
    print("-" * 65)
    for opt in comparison:
        print(f"{opt['vehicle']:<18} | {opt['mileage']:<14} | {opt['total_fuel']:<15} | ${opt['journey_cost']}")
        
    if optimal:
        print(f"\n🏆 Optimal Lowest-Cost Option: {optimal['vehicle']} at ${optimal['journey_cost']}")
    else:
        print("\n❌ No feasible vehicle options available within fuel tank capacity limits.")
