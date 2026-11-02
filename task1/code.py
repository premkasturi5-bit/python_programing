def analyze_environment_data(data, thresholds):
    total_sum = 0
    total_count = 0
    global_max = float('-inf')
    global_min = float('inf')
    
    classified_results = []
    station_averages = []
    
    for station_index, station in enumerate(data):
        station_sum = 0
        station_count = len(station)
        station_classifications = []
        
        for val in station:
            total_sum += val
            total_count += 1
            
            if val > global_max:
                global_max = val
            if val < global_min:
                global_min = val
                
            station_sum += val
            
            if val <= thresholds['good']:
                status = "Good"
            elif val <= thresholds['moderate']:
                status = "Moderate"
            else:
                status = "Unhealthy"
                
            station_classifications.append((val, status))
        
        avg_station = (station_sum / station_count) if station_count > 0 else 0
        station_averages.append((station_index, avg_station))
        classified_results.append(station_classifications)
        
    global_avg = (total_sum / total_count) if total_count > 0 else 0
    
    return {
        "global_average": global_avg,
        "global_maximum": global_max,
        "global_minimum": global_min,
        "station_averages": station_averages,
        "classified_observations": classified_results
    }

if __name__ == "__main__":
    sample_data = [
        [35.5, 42.0, 58.2],
        [15.1, 22.4, 19.8],
        [85.0, 92.5, 110.0]
    ]
    sample_thresholds = {
        "good": 50.0,
        "moderate": 100.0
    }
    results = analyze_environment_data(sample_data, sample_thresholds)
    print(results)
