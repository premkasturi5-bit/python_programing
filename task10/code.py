def analyze_water_distribution(areas_data):
    results = []
    for area in areas_data:
        name = area["name"]
        demands = area["demands"]
        supplies = area["supplies"]
        
        total_demand = sum(demands)
        total_supply = sum(supplies)
        total_shortage = sum(max(0, d - s) for d, s in zip(demands, supplies))
        shortage_percentage = (total_shortage / total_demand * 100) if total_demand > 0 else 0
        
        results.append({
            "area": name,
            "total_demand": total_demand,
            "total_supply": total_supply,
            "total_shortage": total_shortage,
            "shortage_percentage": shortage_percentage
        })
        
    results.sort(key=lambda x: x["shortage_percentage"], reverse=True)
    return results

if __name__ == "__main__":
    sample_areas = [
        {
            "name": "Area A",
            "demands": [1000, 1200, 1100, 1150],
            "supplies": [800, 900, 1000, 850]
        },
        {
            "name": "Area B",
            "demands": [1500, 1400, 1600, 1550],
            "supplies": [1500, 1400, 1500, 1500]
        },
        {
            "name": "Area C",
            "demands": [800, 850, 900, 820],
            "supplies": [500, 550, 600, 500]
        }
    ]
    
    analysis = analyze_water_distribution(sample_areas)
    import json
    print(json.dumps(analysis, indent=2))
