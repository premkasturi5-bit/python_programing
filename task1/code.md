## Problem Statement

Design a program that analyzes nested lists of environmental monitoring data (such as PM2.5 air-quality readings across multiple monitoring stations or time intervals). The program must calculate global and station-specific averages, identify extreme values (minimum and maximum readings), and classify each individual observation into predefined categories (e.g., Good, Moderate, Unhealthy) based on supplied threshold values.

---

## Algorithm

1. **Initialize** variables to store the global sum, global count, global maximum (`-inf`), and global minimum (`inf`).
2. **Accept** a nested list of numerical readings and a dictionary of threshold values.
3. **Iterate** through each sublist (station) in the nested list:
* Initialize a local sum for the current station.
* Iterate through each reading within the station:
* Add the reading to the global sum and increment the global count.
* Update the global maximum and minimum if applicable.
* Add the reading to the station sum.
* Compare the reading against the thresholds (`good`, `moderate`) to assign a classification label.


* Compute the station average and store it.


4. **Compute** the global average by dividing the total global sum by the global count.
5. **Return** or display the summary statistics (global average, extremes, station averages) alongside the classified observations.

---

## Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Input Nested Readings & Thresholds]
    B --> C[Initialize Global Stats: Sum, Count, Min, Max]
    C --> D[Loop through each station sublist]
    D --> E[Initialize Station Sum & Classification List]
    E --> F[Loop through each reading in station]
    F --> G[Update Global Sum, Count, Min, Max]
    G --> H[Classify reading based on thresholds]
    H --> I{More readings in station?}
    I -- Yes --> F
    I -- No --> J[Calculate Station Average]
    J --> K{More stations?}
    K -- Yes --> D
    K -- No --> L[Calculate Global Average]
    L --> M[Output Results]
    M --> N[Stop]

```

---

## Python Source Code

```python
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

```

---

## Sample Input

```json
{
  "data": [
    [35.5, 42.0, 58.2],
    [15.1, 22.4, 19.8],
    [85.0, 92.5, 110.0]
  ],
  "thresholds": {
    "good": 50.0,
    "moderate": 100.0
  }
}

```

---

## Sample Output

```json
{
  "global_average": 53.388888888888886,
  "global_maximum": 110.0,
  "global_minimum": 15.1,
  "station_averages": [
    [0, 45.233333333333334],
    [1, 19.1],
    [2, 95.83333333333333]
  ],
  "classified_observations": [
    [[35.5, "Good"], [42.0, "Good"], [58.2, "Moderate"]],
    [[15.1, "Good"], [22.4, "Good"], [19.8, "Good"]],
    [[85.0, "Moderate"], [92.5, "Moderate"], [110.0, "Unhealthy"]]
  ]
}

```
