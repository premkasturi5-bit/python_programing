def validate_registrations(registrations, prerequisites, conflicts):
    student_courses = {}
    for student_id, course in registrations:
        if student_id not in student_courses:
            student_courses[student_id] = []
        student_courses[student_id].append(course)
        
    violation_report = []
    
    for student_id, courses in student_courses.items():
        student_violations = []
        seen_courses = set()
        
        for course in courses:
            if course in seen_courses:
                student_violations.append(f"Duplicate registration for course: {course}")
            else:
                seen_courses.add(course)
                
        for course in courses:
            if course in prerequisites:
                req = prerequisites[course]
                if req not in courses:
                    student_violations.append(f"Missing prerequisite '{req}' for course '{course}'")
                    
        for c1, c2 in conflicts:
            if c1 in courses and c2 in courses:
                student_violations.append(f"Mutually exclusive courses selected: '{c1}' and '{c2}'")
                
        if student_violations:
            violation_report.append({
                "student_id": student_id,
                "courses": courses,
                "violations": student_violations
            })
            
    return violation_report


if __name__ == "__main__":
    registrations = [
        ("S101", "CS101"),
        ("S101", "CS102"),
        ("S101", "CS101"),
        ("S102", "CS102"),
        ("S103", "CS103"),
        ("S103", "CS101"),
        ("S104", "MATH201"),
        ("S104", "MATH202")
    ]
    
    prerequisites = {
        "CS102": "CS101",
        "CS103": "CS101"
    }
    
    conflicts = [
        ("MATH201", "MATH202")
    ]
    
    violations = validate_registrations(registrations, prerequisites, conflicts)
    
    print("=== REGISTRATION VALIDATION REPORT ===")
    if not violations:
        print("All student registrations are valid.")
    for v in violations:
        print(f"\nStudent ID: {v['student_id']}")
        print(f"Selected Courses: {v['courses']}")
        print("Violations Found:")
        for err in v['violations']:
            print(f"  - {err}")
