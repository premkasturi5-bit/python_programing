def allocate_seat(classrooms, classroom_name, row, col, student_name):
    if classroom_name not in classrooms:
        return f"Error: Classroom '{classroom_name}' does not exist."
    
    grid = classrooms[classroom_name]
    
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return f"Error: Seat position ({row}, {col}) is out of bounds for {classroom_name}."
    
    current_status = grid[row][col]
    
    if current_status == "Reserved":
        return f"Conflict: Seat ({row}, {col}) in {classroom_name} is RESERVED and cannot be allocated."
    elif current_status != "Empty":
        return f"Conflict: Seat ({row}, {col}) in {classroom_name} is already assigned to {current_status} (Duplicate Assignment)."
    
    grid[row][col] = student_name
    return f"Success: Allocated seat ({row}, {col}) in {classroom_name} to {student_name}."


def calculate_vacant_capacity(classrooms):
    vacancy_report = {}
    total_vacant = 0
    
    for name, grid in classrooms.items():
        vacant_count = sum(row.count("Empty") for row in grid)
        vacancy_report[name] = vacant_count
        total_vacant += vacant_count
        
    return vacancy_report, total_vacant


if __name__ == "__main__":
    classrooms = {
        "Room 101": [
            ["Empty", "Reserved", "Empty"],
            ["Empty", "Empty", "Reserved"],
            ["Empty", "Empty", "Empty"]
        ],
        "Room 102": [
            ["Reserved", "Empty", "Empty"],
            ["Empty", "Reserved", "Empty"]
        ]
    }
    
    requests = [
        ("Room 101", 0, 0, "Alice"),
        ("Room 101", 0, 1, "Bob"),
        ("Room 101", 2, 2, "Alice"),
        ("Room 101", 2, 2, "Charlie"),
        ("Room 102", 0, 1, "David")
    ]
    
    print("=== ALLOCATION PROCESSING ===")
    for req in requests:
        result = allocate_seat(classrooms, req[0], req[1], req[2], req[3])
        print(result)
        
    vacancy, total = calculate_vacant_capacity(classrooms)
    
    print("\n=== VACANT CAPACITY REPORT ===")
    for room, count in vacancy.items():
        print(f"{room}: {count} vacant seats")
    print(f"Total Institutional Vacancy: {total} seats")
    
    print("\n=== FINAL CLASSROOM MATRICES ===")
    for room, grid in classrooms.items():
        print(f"\n{room}:")
        for r in grid:
            print(r)
