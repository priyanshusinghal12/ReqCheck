def check_requirements(completed_courses):
    requirements = {
        "STAT Core": [{"STAT 330", "STAT 331", "STAT 332", "STAT 333"}, 4],
        "Professional Communications": [{"ENGL 378", "MTHEL 300"}, 1],
        "Calculus 3": [{"MATH 237", "MATH 247"}, 1],
        "Advanced Math": [{"AMATH 231", "AMATH 242", "AMATH 250", "AMATH 251", "AMATH 350", "CS 371", "MATH 239", "MATH 249"}, 1],
        "STAT 400-level": [set(), 2],
        "STAT 300/400-level": [set(), 1],
        "CS Option": [{"CS 457", "CS 485", "CS 486"}, 1],
        "300/400-level Electives": [set(), 4],
        "General Electives": [set(), 3],
    }
    
    used_courses = set()
    unmet_requirements = []
    
    for req, (options, count) in requirements.items():
        if options:  # Specific course options
            matched = [c for c in options if c in completed_courses and c not in used_courses]
            if len(matched) >= count:
                used_courses.update(matched[:count])
            else:
                unmet_requirements.append(req)
        
    preferred_order = ["AMATH 231", "MATH 239", "MATH 249", "AMATH 242", "CS 371", "AMATH 350"]
    for course in preferred_order:
        if course in completed_courses and course not in used_courses:
            used_courses.add(course)
            break
    else:
        unmet_requirements.append("Advanced Math")
    
    stat_400 = [c for c in completed_courses if c.startswith("STAT 4") and c not in used_courses]
    if len(stat_400) >= 2:
        used_courses.update(stat_400[:2])
    else:
        unmet_requirements.append("STAT 400-level")
    
    stat_300_400 = [c for c in completed_courses if (c.startswith("STAT 3") or c.startswith("STAT 4")) and c not in used_courses]
    if len(stat_300_400) >= 1:
        used_courses.update(stat_300_400[:1])
    else:
        unmet_requirements.append("STAT 300/400-level")
    
    cs_option_met = False
    for cs_course in ["CS 457", "CS 485", "CS 486"]:
        if cs_course in completed_courses and cs_course not in used_courses:
            used_courses.add(cs_course)
            cs_option_met = True
            break
    
    if not cs_option_met:
        additional_stat_400 = [c for c in completed_courses if c.startswith("STAT 4") and c not in used_courses]
        if len(additional_stat_400) >= 1:
            used_courses.add(additional_stat_400[0])
        else:
            unmet_requirements.append("Additional STAT 400-level")
    
    electives = [c for c in completed_courses if any(c.startswith(prefix) for prefix in ["ACTSC", "AMATH", "CO", "CS", "MATBUS", "MATH", "PMATH", "STAT"]) and c not in used_courses]
    if len(electives) >= 4:
        used_courses.update(electives[:4])
    else:
        unmet_requirements.append("300/400-level Electives")
    
    if len(electives) >= 7:
        used_courses.update(electives[:3])
    else:
        unmet_requirements.append("General Electives")
    
    print("Remaining Requirements:")
    for req in unmet_requirements:
        print(f"- {req}")
    
# Example usage
completed_courses = {
    "PMATH 333", "CS 479", "AFM 101", "CS 135", "MATH 135", "MATH 137", 
    "MTHEL 99", "STAT 444", "CS 136", "CS 136L", "ECON 102", "STAT 443", 
    "MATH 136", "MATH 138", "SPCOM 223", "CS 371", "CS 486", "MATH 235", 
    "CS 231", "CS 234", "MATH 237", "PD 1", "STAT 230", "COOP 1", "PD 11", 
    "AMATH 250", "BET 100", "CLAS 104", "CS 230", "PSYCH 101", "STAT 231", 
    "COOP 2", "PD 13", "BET 210", "CS 330", "ECON 101", "STAT 330", 
    "STAT 331", "STAT 341"
}

check_requirements(completed_courses)
