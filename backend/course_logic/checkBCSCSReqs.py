from course_logic.helper import *
from collections import defaultdict
import re

def check_depth_requirement(student_courses, cs_reqs):
    subject_to_courses = defaultdict(list)

    # Group courses by subject and track their levels
    for course in student_courses:
        try:
            subject, number = course.split()
            level = int(number[:3])
            subject_to_courses[subject].append((course, level))
        except:
            continue

    # Try to satisfy depth requirement with any subject
    for subject, entries in subject_to_courses.items():
        if len(entries) >= 3:
            has_300_plus = any(level >= 300 for (_, level) in entries)
            if has_300_plus:
                cs_reqs["Depth Requirement (does not check the prerequisite chain option)"] = [True, [course for (course, _) in entries[:3]]]
                return

    # If no subject satisfies full depth requirement, include partial progress
    best_partial = []
    for entries in subject_to_courses.values():
        if len(entries) > len(best_partial):
            best_partial = entries[:2]

    cs_reqs["Depth Requirement (does not check the prerequisite chain option)"] = [False, [course for (course, _) in best_partial]]         
            
def check_breadth_requirement(student_courses, cs_reqs):
    breadth_areas = {
        "Breadth Req - Humanities": (
            ["CHINA", "CLAS", "CMW", "SPCOM", "CROAT", "DAC", "DUTCH", "EASIA", "ENGL",
             "FINE", "FR", "GER", "GRK", "HIST", "HUMSC", "ITAL", "ITALST", "JAPAN", "JS",
             "KOREA", "LAT", "MEDVL", "MUSIC", "PHIL", "PORT", "RCS", "REES", "RUSS", "SI",
             "SPAN", "THPERF", "VCULT"], 2),
        
        "Breadth Req - Pure Sciences": (
            ["BIOL", "CHEM", "EARTH", "PHYS", "SCI"], 1),
        
        "Breadth Req - Pure and Applied Sciences": (
            ["BIOL", "CHEM", "EARTH", "ENVS", "ERS", "HEALTH", "KIN", "MNS", "PHYS", "PLAN", "SCI"], 1),
        
        "Breadth Req - Social Sciences": (
            ["AFM", "ANTH", "APPLS", "ARBUS", "BET", "BUS", "COMM", "ECON", "ENBUS", "GEOG", "GSJ",
             "HRM", "INDEV", "INDG", "INTST", "LS", "MSE", "PACS", "PSCI", "PSYCH", "REC", "SDS",
             "SRF", "SOC", "SOCWK", "STV"], 2)
    }

    for req_name, (valid_subjects, num_required) in breadth_areas.items():
        matching_courses = []
        for course in student_courses:
            subject = course.split()[0]
            if subject in valid_subjects:
                matching_courses.append(course)

        cs_reqs[req_name][1].extend(matching_courses[:num_required])
        
        if len(matching_courses) >= num_required:
            cs_reqs[req_name][0] = True
            for c in matching_courses[:num_required]:
                student_courses.remove(c)

def check_capstone_requirement(student_courses, reqs):
    requirement_key = "Complete 1 of the following: (Complete 1 of: CO 487, CS 499T, STAT 440) or (1 course from CS440-CS498) or (a CS course from 600/700 level)"
    
    # Step 1: Check specific courses
    preferred_courses = ["CO 487", "CS 499T", "STAT 440"]
    for course in preferred_courses:
        if course in student_courses:
            reqs[requirement_key] = [True, [course]]
            student_courses.remove(course)
            return

    # Step 2: Check CS 600/700-level course (e.g., "CS 698", "CS 749")
    for course in student_courses:
        match = re.match(r"CS (\d{3})", course)
        if match:
            number = int(match.group(1))
            if 600 <= number < 800:
                reqs[requirement_key] = [True, [course]]
                student_courses.remove(course)
                return

    # Step 3: Check CS 440–498 (inclusive)
    for course in student_courses:
        match = re.match(r"CS (\d{3})", course)
        if match:
            number = int(match.group(1))
            if 440 <= number <= 498:
                reqs[requirement_key] = [True, [course]]
                student_courses.remove(course)
                return

    # If none of the conditions met
    reqs[requirement_key] = [False, []]


def check_bcs_cs_major(student_courses):
    cs_reqs = {
    "Complete all of: CS 136L, CS 341, CS 350": [False, []],
    "Complete one of: CS 115, CS 135, CS 145": [False, []],
    "Complete one of: CS 136, CS 146": [False, []],
    "Complete one of: CS 240, CS 240E": [False, []],
    "Complete one of: CS 241, CS 241E": [False, []],
    "Complete one of: CS 245, CS 245E": [False, []],
    "Complete one of: CS 246, CS 246E": [False, []],
    "Complete one of: CS 251, CS 251E": [False, []],
    "Complete one course from List 1 (Communication Requirement 1)": [False, []],
    "Complete one course from List 1 + List 2 (Communication Requirement 2)": [False, []],
    "Complete one of: MATH 127, MATH 137, MATH 147": [False, []],
    "Complete one of: MATH 128, MATH 138, MATH 148": [False, []],
    "Complete one of: MATH 135, MATH 145": [False, []],
    "Complete one of: MATH 136, MATH 146": [False, []],
    "Complete one of: MATH 239, MATH 249": [False, []],
    "Complete one of: STAT 230, STAT 240": [False, []],
    "Complete one of: STAT 231, STAT 241": [False, []],
    "Complete 3 additional CS courses from CS340-CS398, CS440-CS489": [False, []],
    "Complete 2 additional CS courses from CS440-CS489": [False, []],
    "Complete 1 of the following: (Complete 1 of: CO 487, CS 499T, STAT 440) or (1 course from CS440-CS498) or (a CS course from 600/700 level)": [False, []],
    "Depth Requirement (does not check the prerequisite chain option)": [False, []],
    "Breadth Req - Humanities": [False, []],
    "Breadth Req - Pure Sciences": [False, []],
    "Breadth Req - Pure and Applied Sciences": [False, []],
    "Breadth Req - Social Sciences": [False, []],
    }
    
    list1 = [
        "SPCOM 100", "SPCOM 223", "EMLS 101R", "EMLS 102R", "EMLS 129R", "ENGL 109", "ENGL 129R",
        "COMMST 100", "COMMST 223"
    ]
    
    list1and2 = [
        "SPCOM 100", "SPCOM 223", "EMLS 101R", "EMLS 102R", "EMLS 129R", "ENGL 109", "ENGL 129R",
        "SPCOM 225", "SPCOM 227", "SPCOM 228", "EMLS 103R", "EMLS 104R", "EMLS 110R", "ENGL 101B",
        "ENGL 108B", "ENGL 108D", "ENGL 119", "ENGL 208B", "ENGL 209", "ENGL 210E", "ENGL 210F", "ENGL 378",
        "COMMST 100", "COMMST 223", "COMMST 225", "COMMST 227", "COMMST 228"
    ]


    # Core group
    check_complete_all("Complete all of: CS 136L, CS 341, CS 350",
                       ["CS 136L", "CS 341", "CS 350"], student_courses, cs_reqs)

    # Check one-of groups
    check_n_from_list("Complete one of: CS 115, CS 135, CS 145",
                      ["CS 115", "CS 135", "CS 145"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: CS 136, CS 146",
                      ["CS 136", "CS 146"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: CS 240, CS 240E",
                      ["CS 240", "CS 240E"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: CS 241, CS 241E",
                      ["CS 241", "CS 241E"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: CS 245, CS 245E",
                      ["CS 245", "CS 245E"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: CS 246, CS 246E",
                      ["CS 246", "CS 246E"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: CS 251, CS 251E",
                      ["CS 251", "CS 251E"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: MATH 127, MATH 137, MATH 147",
                      ["MATH 127", "MATH 137", "MATH 147"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: MATH 128, MATH 138, MATH 148",
                      ["MATH 128", "MATH 138", "MATH 148"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: MATH 135, MATH 145",
                      ["MATH 135", "MATH 145"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: MATH 136, MATH 146",
                      ["MATH 136", "MATH 146"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: MATH 239, MATH 249",
                      ["MATH 239", "MATH 249"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: STAT 230, STAT 240",
                      ["STAT 230", "STAT 240"], 1, student_courses, cs_reqs)

    check_n_from_list("Complete one of: STAT 231, STAT 241",
                      ["STAT 231", "STAT 241"], 1, student_courses, cs_reqs)
    
    check_n_from_list("Complete one course from List 1 (Communication Requirement 1)",
                      list1, 1, student_courses, cs_reqs)
    
    check_n_from_list_without_removing("Complete one course from List 1 + List 2 (Communication Requirement 2)",
                      list1and2, 1, student_courses, cs_reqs)
    
    check_capstone_requirement(student_courses, cs_reqs)

    # Check ranges
    check_course_range("Complete 2 additional CS courses from CS440-CS489",
                       "CS", 440, 489, student_courses, cs_reqs, num_courses_required=2)
    
    check_course_range("Complete 3 additional CS courses from CS340-CS398, CS440-CS489",
                       "CS", 340, 489, student_courses, cs_reqs, num_courses_required=3)

        
    student_courses = [course for course in student_courses if course not in list1]

    #Depth Reqs
    check_depth_requirement(student_courses, cs_reqs)
    
    #Breadth Reqs
    check_breadth_requirement(student_courses, cs_reqs)

    
    return cs_reqs

def check_ai_specialization(student_courses):
    ai_reqs = {
        "Complete all of: CS 486, CS 492": [False, []],
        "Complete one of: CS 480, CS 485": [False, []],
        "Complete 4 from given list - one Faculty of Math course": [False, []],
        "Complete 4 from given list - one Faculty of Engineering course": [False, []],
        "Complete 4 from given list - remaining two courses": [False, []]
    }

    # Req 1: CS486 and CS492
    check_complete_all("Complete all of: CS 486, CS 492",
                       ["CS 486", "CS 492"], student_courses, ai_reqs)

    # Req 2: One of CS480 or CS485
    check_n_from_list("Complete one of: CS 480, CS 485",
                      ["CS 480", "CS 485"], n=1,
                      student_courses=student_courses, major_reqs=ai_reqs)

    # Req 3: 4 electives
    
    math_faculty_ai_electives = [
        "AMATH 449", "BIOL 487", "CO 367", "CO 456", "CO 463", "CO 466", "CS 452", "CS 479",
        "CS 480", "CS 484", "CS 485", "STAT 341", "STAT 440", "STAT 441", "STAT 444",
    ]

    check_n_from_list("Complete 4 from given list - one Faculty of Math course",
                      math_faculty_ai_electives, n=1,
                      student_courses=student_courses, major_reqs=ai_reqs)

    engg_faculty_ai_electives = ["ECE 380", "ECE 423", "ECE 457C", "ECE 481", "ECE 486",
        "ECE 488", "ECE 495", "MTE 544", "SE 380",
        "SYDE 552", "SYDE 556", "SYDE 572"]
    
    check_n_from_list("Complete 4 from given list - one Faculty of Engineering course",
                      engg_faculty_ai_electives, n=1,
                      student_courses=student_courses, major_reqs=ai_reqs)
    
    check_n_from_list("Complete 4 from given list - remaining two courses",
                      math_faculty_ai_electives + engg_faculty_ai_electives,
                      n=2,
                      student_courses=student_courses, major_reqs=ai_reqs)

    return ai_reqs

def check_bioinformatics_requirements(student_courses):
    bioinfo_reqs = {
        "Complete all of the following bioinformatics core courses": [False, []]
    }

    required_courses = [
        "BIOL 130", "BIOL 130L", "BIOL 239", "BIOL 240", "BIOL 240L",
        "BIOL 308", "BIOL 365", "BIOL 465",
        "CHEM 120", "CHEM 120L", "CHEM 123", "CHEM 123L",
        "CS 482"
    ]

    check_complete_all("Complete all of the following bioinformatics core courses",
                       required_courses, student_courses, bioinfo_reqs)

    return bioinfo_reqs

def check_business_specialization(student_courses):
    reqs = {
        "Complete 2 of: ACTSC 447, CS 348, CS 476, CS 490": [False, []],
        "Complete 5 approved courses (min 2 at 200-level or higher)": [False, []]
    }

    core_options = ["ACTSC 447", "CS 348", "CS 476", "CS 490"]
    approved_courses = [
        "ACTSC 231", "ACTSC 372",
        "AFM 101", "AFM 102",
        "BUS 121W", "BUS 362W", "BUS 381W", "BUS 491W",
        "COMM 101", "COMM 400", "COMM 432",
        "ECON 101", "ECON 102",
        "HRM 200", "MGMT 220", "MSE 311"
    ]
    
    one_of_each_group_allowed = [
        ["AFM 131", "ARBUS 101", "BUS 111W"],
        ["MSE 211", "PSYCH 238"]
    ]

    all_approved = approved_courses + [item for group in one_of_each_group_allowed for item in group]

    # Step 1: Core Options
    completed_core = [c for c in core_options if c in student_courses]
    if len(completed_core) >= 2:
        reqs["Complete 2 of: ACTSC 447, CS 348, CS 476, CS 490"][0] = True
        reqs["Complete 2 of: ACTSC 447, CS 348, CS 476, CS 490"][1].extend(completed_core[:2])
        for c in completed_core[:2]:
            student_courses.remove(c)

    # Step 2: Approved Courses
    selected_courses = []
    used_from_group = [False] * len(one_of_each_group_allowed)
    upper_level_count = 0

    for course in student_courses[:]:
        subject = course.split()[0]
        try:
            level = int(course.split()[1][:3])
        except:
            continue

        if course in approved_courses:
            selected_courses.append(course)
            student_courses.remove(course)
            if level >= 200:
                upper_level_count += 1

        else:
            for i, group in enumerate(one_of_each_group_allowed):
                if course in group and not used_from_group[i]:
                    selected_courses.append(course)
                    student_courses.remove(course)
                    used_from_group[i] = True
                    if level >= 200:
                        upper_level_count += 1
                    break

        if len(selected_courses) == 5:
            break

    if len(selected_courses) == 5 and upper_level_count >= 2:
        reqs["Complete 5 approved courses (min 2 at 200-level or higher)"][0] = True
    reqs["Complete 5 approved courses (min 2 at 200-level or higher)"][1].extend(selected_courses)

    return reqs

def check_computational_fine_art(student_courses):
    reqs = {
        "Complete all of: CS 349, CS 488": [False, []],
        "Complete 1 of: CS 383 or FINE 383": [False, []],
        "Complete 1 of: FINE 100 or FINE 130": [False, []],
        "Complete 1 of: FINE 228 or FINE 247": [False, []],
        "Complete 1 of: VCULT 200 or VCULT 257": [False, []],
    }

    # Check all of CS 349 and CS 488
    mandatory = ["CS 349", "CS 488"]
    if all(course in student_courses for course in mandatory):
        reqs["Complete all of: CS 349, CS 488"][0] = True
        reqs["Complete all of: CS 349, CS 488"][1].extend(mandatory)
        for c in mandatory:
            student_courses.remove(c)

    # Pairs to check for one-of requirements
    one_of_pairs = [
        ("Complete 1 of: CS 383 or FINE 383", ["CS 383", "FINE 383"]),
        ("Complete 1 of: FINE 100 or FINE 130", ["FINE 100", "FINE 130"]),
        ("Complete 1 of: FINE 228 or FINE 247", ["FINE 228", "FINE 247"]),
        ("Complete 1 of: VCULT 200 or VCULT 257", ["VCULT 200", "VCULT 257"]),
    ]

    for req_name, options in one_of_pairs:
        for course in options:
            if course in student_courses:
                reqs[req_name][0] = True
                reqs[req_name][1].append(course)
                student_courses.remove(course)
                break

    return reqs

def check_digital_hardware_specialization(student_courses):
    specialization_reqs = {
        "Complete all of: ECE 124, ECE 222, ECE 327, ECE 423": [False, []],
        "Complete 1 of: CS 450 or ECE 320": [False, []],
        "Complete 2 of: CS 452, CS 454, CS 456, CS 457": [False, []],
        "Complete 1 of: ECE 224 or MTE 325": [False, []],
        "Complete 1 of: GENE 123 or MTE 120": [False, []],
    }

    check_complete_all(
        "Complete all of: ECE 124, ECE 222, ECE 327, ECE 423",
        ["ECE 124", "ECE 222", "ECE 327", "ECE 423"],
        student_courses,
        specialization_reqs
    )

    check_n_from_list(
        "Complete 1 of: CS 450 or ECE 320",
        ["CS 450", "ECE 320"],
        1,
        student_courses,
        specialization_reqs
    )

    check_n_from_list(
        "Complete 2 of: CS 452, CS 454, CS 456, CS 457",
        ["CS 452", "CS 454", "CS 456", "CS 457"],
        2,
        student_courses,
        specialization_reqs
    )

    check_n_from_list(
        "Complete 1 of: ECE 224 or MTE 325",
        ["ECE 224", "MTE 325"],
        1,
        student_courses,
        specialization_reqs
    )

    check_n_from_list(
        "Complete 1 of: GENE 123 or MTE 120",
        ["GENE 123", "MTE 120"],
        1,
        student_courses,
        specialization_reqs
    )

    return specialization_reqs

def check_game_design_specialization(student_courses):
    game_reqs = {
        "Complete all of: DAC 204, DAC 305": [False, []],
        "Complete 1 of: COMMST 149, DAC 209, DAC 302, DAC 309, ENGL 392A, ENGL 392B, ENGL 408C, FINE 247, THPERF 149": [False, []],
        "Complete 1 of: COMMST 210, COMMST 339, COMMST 430, COMMST 435, ENGL 293, GSJ 205, SOC 324": [False, []],
        "Complete 1 of: COMMST 235 or ENGL 294": [False, []],
        "Complete 2 of: CS 449, CS 454, CS 488": [False, []],
    }

    check_complete_all(
        "Complete all of: DAC 204, DAC 305",
        ["DAC 204", "DAC 305"],
        student_courses,
        game_reqs
    )

    check_n_from_list(
        "Complete 1 of: COMMST 149, DAC 209, DAC 302, DAC 309, ENGL 392A, ENGL 392B, ENGL 408C, FINE 247, THPERF 149",
        ["COMMST 149", "DAC 209", "DAC 302", "DAC 309", "ENGL 392A", "ENGL 392B", "ENGL 408C", "FINE 247", "THPERF 149"],
        1,
        student_courses,
        game_reqs
    )

    check_n_from_list(
        "Complete 1 of: COMMST 210, COMMST 339, COMMST 430, COMMST 435, ENGL 293, GSJ 205, SOC 324",
        ["COMMST 210", "COMMST 339", "COMMST 430", "COMMST 435", "ENGL 293", "GSJ 205", "SOC 324"],
        1,
        student_courses,
        game_reqs
    )

    check_n_from_list(
        "Complete 1 of: COMMST 235 or ENGL 294",
        ["COMMST 235", "ENGL 294"],
        1,
        student_courses,
        game_reqs
    )

    check_n_from_list(
        "Complete 2 of: CS 449, CS 454, CS 488",
        ["CS 449", "CS 454", "CS 488"],
        2,
        student_courses,
        game_reqs
    )

    return game_reqs

def check_software_engineering_specialization(student_courses):
    software_eng_reqs = {
        "Complete 1 of: BET 360, BET 420, CS 492, ENVS 205, GEOG 207, GEOG 306, GSJ 205, MSE 422, MSE 442, PACS 315, SOC 232, SOC 324, STV 202, STV 205, STV 306": [False, []],
        "Complete 2 of: CS 343, CS 346, CS 348, CS 349": [False, []],
        "Complete 2 of: CS 442, CS 444, CS 448, CS 449, CS 450, CS 451, CS 452, CS 453, CS 454, CS 456, CS 457, CS 459, CS 480, CS 484, CS 486, CS 488": [False, []],
        "Complete 1 of: CS 445, ECE 451": [False, []],
        "Complete 1 of: CS 446, ECE 452": [False, []],
        "Complete 1 of: CS 447, ECE 453": [False, []]
    }

    if "CS 453" in student_courses and "CS 459" in student_courses:
        student_courses.remove("CS 459")

    check_n_from_list("Complete 1 of: BET 360, BET 420, CS 492, ENVS 205, GEOG 207, GEOG 306, GSJ 205, MSE 422, MSE 442, PACS 315, SOC 232, SOC 324, STV 202, STV 205, STV 306",
                      ["BET 360", "BET 420", "CS 492", "ENVS 205", "GEOG 207", "GEOG 306", "GSJ 205", "MSE 422", "MSE 442", "PACS 315", "SOC 232", "SOC 324", "STV 202", "STV 205", "STV 306"],
                      1, student_courses, software_eng_reqs)

    check_n_from_list("Complete 2 of: CS 343, CS 346, CS 348, CS 349",
                      ["CS 343", "CS 346", "CS 348", "CS 349"],
                      2, student_courses, software_eng_reqs)

    check_n_from_list("Complete 2 of: CS 442, CS 444, CS 448, CS 449, CS 450, CS 451, CS 452, CS 453, CS 454, CS 456, CS 457, CS 459, CS 480, CS 484, CS 486, CS 488",
                      ["CS 442", "CS 444", "CS 448", "CS 449", "CS 450", "CS 451", "CS 452", "CS 453", "CS 454", "CS 456", "CS 457", "CS 459", "CS 480", "CS 484", "CS 486", "CS 488"],
                      2, student_courses, software_eng_reqs)

    check_n_from_list("Complete 1 of: CS 445, ECE 451",
                      ["CS 445", "ECE 451"],
                      1, student_courses, software_eng_reqs)

    check_n_from_list("Complete 1 of: CS 446, ECE 452",
                      ["CS 446", "ECE 452"],
                      1, student_courses, software_eng_reqs)

    check_n_from_list("Complete 1 of: CS 447, ECE 453",
                      ["CS 447", "ECE 453"],
                      1, student_courses, software_eng_reqs)

    return software_eng_reqs

def check_hci_specialization(student_courses):
    hci_reqs = {
        "Complete all of: CS 349, CS 449": [False, []],
        "Complete 1 of: BET 360, CS 492, GSJ 205, MSE 442, PACS 315, SOC 232, STV 202, STV 205, STV 208, STV 210, STV 302, STV 304, STV 305, STV 306": [False, []],
        "Complete 2 of: ENGL 108D, ENGL 293, ENGL 295, FINE 100, FINE 150, INTEG 121, INTEG 251, KIN 320, PSYCH 207, PSYCH 261, STAT 332, STAT 430, VCULT 257": [False, []],
        "Complete 2 of: CS 454, CS 480, CS 484, CS 486, CS 488, (1 of CS 445/ECE 451/SE 463), (1 of CS 446/ECE 452/SE 464), (1 of CS 447/ECE 453/SE 465), (1 of CS 453/CS 459)": [False, []],
    }

    check_complete_all("Complete all of: CS 349, CS 449", ["CS 349", "CS 449"], student_courses, hci_reqs)

    check_n_from_list("Complete 1 of: BET 360, CS 492, GSJ 205, MSE 442, PACS 315, SOC 232, STV 202, STV 205, STV 208, STV 210, STV 302, STV 304, STV 305, STV 306",
                      ["BET 360", "CS 492", "GSJ 205", "MSE 442", "PACS 315", "SOC 232", "STV 202", "STV 205", "STV 208", "STV 210", "STV 302", "STV 304", "STV 305", "STV 306"],
                      1, student_courses, hci_reqs)

    check_n_from_list("Complete 2 of: ENGL 108D, ENGL 293, ENGL 295, FINE 100, FINE 150, INTEG 121, INTEG 251, KIN 320, PSYCH 207, PSYCH 261, STAT 332, STAT 430, VCULT 257",
                      ["ENGL 108D", "ENGL 293", "ENGL 295", "FINE 100", "FINE 150", "INTEG 121", "INTEG 251", "KIN 320", "PSYCH 207", "PSYCH 261", "STAT 332", "STAT 430", "VCULT 257"],
                      2, student_courses, hci_reqs)

    full_list = ["CS 454", "CS 480", "CS 484", "CS 486", "CS 488"]

    groups = [
        ["CS 445", "ECE 451", "SE 463"],
        ["CS 446", "ECE 452", "SE 464"],
        ["CS 447", "ECE 453", "SE 465"],
        ["CS 453", "CS 459"]
    ]

    used_courses = []

    for group in groups:
        for course in group:
            if course in student_courses:
                used_courses.append(course)
                student_courses.remove(course)
                break

    all_valid_courses = full_list + used_courses
    check_n_from_list("Complete 2 of: CS 454, CS 480, CS 484, CS 486, CS 488, (1 of CS 445/ECE 451/SE 463), (1 of CS 446/ECE 452/SE 464), (1 of CS 447/ECE 453/SE 465), (1 of CS 453/CS 459)",
                      all_valid_courses, 2, student_courses, hci_reqs)

    return hci_reqs
