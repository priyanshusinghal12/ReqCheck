from course_logic.helper import *
from collections import defaultdict

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
                cs_reqs["Depth Requirement"] = [True, [course for (course, _) in entries[:3]]]
                return

    # If no subject satisfies full depth requirement, include partial progress
    best_partial = []
    for entries in subject_to_courses.values():
        if len(entries) > len(best_partial):
            best_partial = entries[:2]

    cs_reqs["Depth Requirement"] = [False, [course for (course, _) in best_partial]]         
            
def check_breadth_requirement(student_courses, cs_reqs):
    breadth_areas = {
        "Breadth Req - Humanities": (
            ["CHINA", "CLAS", "CMW", "COMMST", "CROAT", "DAC", "DUTCH", "EASIA", "ENGL",
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
    "Depth Requirement (does not check prereq chain of length three)": [False, []],
    "Breadth Req - Humanities": [False, []],
    "Breadth Req - Pure Sciences": [False, []],
    "Breadth Req - Pure and Applied Sciences": [False, []],
    "Breadth Req - Social Sciences": [False, []],
    }
    
    list1 = ["COMMST 100", "COMMST 223", "EMLS 101R", "EMLS 102R", "EMLS 129R", "ENGL 109", "ENGL 129R"]
    
    list1and2 = ["COMMST 100", "COMMST 223", "EMLS 101R", "EMLS 102R", "EMLS 129R", "ENGL 109", "ENGL 129R",
             "COMMST 225", "COMMST 227", "COMMST 228", "EMLS 103R", "EMLS 104R", "EMLS 110R", "ENGL 101B",
             "ENGL 108B", "ENGL 108D", "ENGL 119", "ENGL 208B", "ENGL 209", "ENGL 210E", "ENGL 210F", "ENGL 378"]

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

    # Check ranges
    check_course_range("Complete 3 additional CS courses from CS340-CS398, CS440-CS489",
                       "CS", 340, 489, student_courses, cs_reqs, num_courses_required=3)

    check_course_range("Complete 2 additional CS courses from CS440-CS489",
                       "CS", 440, 489, student_courses, cs_reqs, num_courses_required=2)

    
    #Complete 1 of the following: (1 course from CS440-CS498, a CS course from 600/700 level) 
    # or (Complete CO 487, CS 499T, STAT 440)
    sub_req = {"Complete 1 of: CO 487, CS 499T, STAT 440": [False, []],}
               
    check_n_from_list("Complete 1 of: CO 487, CS 499T, STAT 440",
                      ["CO 487", "CS 499T", "STAT 440"], 1, student_courses, sub_req)
    
    has_cs_440_to_498 = any(
    course.startswith("CS ") and 440 <= int(course.split(" ")[1]) <= 498 for course in student_courses
    )

    if sub_req["Complete 1 of: CO 487, CS 499T, STAT 440"][0]:
        cs_reqs["Complete 1 of the following: (Complete 1 of: CO 487, CS 499T, STAT 440) or (1 course from CS440-CS498) or (a CS course from 600/700 level)"][0] = True
        cs_reqs["Complete 1 of the following: (Complete 1 of: CO 487, CS 499T, STAT 440) or (1 course from CS440-CS498) or (a CS course from 600/700 level)"][1].extend(
            sub_req["Complete 1 of: CO 487, CS 499T, STAT 440"][1]
        )
    elif has_cs_440_to_498:
        check_course_range("Complete 1 of the following: (Complete 1 of: CO 487, CS 499T, STAT 440) or (1 course from CS440-CS498) or (a CS course from 600/700 level)",
                        "CS", 440, 498, student_courses, cs_reqs, num_courses_required=1)
    else:
        check_n_courses("Complete 1 of the following: (Complete 1 of: CO 487, CS 499T, STAT 440) or (1 course from CS440-CS498) or (a CS course from 600/700 level)",
                        eligible_levels=600,
                        subject_codes=["CS"],
                        n=1,
                        student_courses=student_courses,
                        major_reqs=cs_reqs)
        
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
        "Complete 4 of the AI elective list": [False, []],
    }

    # Req 1: CS486 and CS492
    check_complete_all("Complete all of: CS 486, CS 492",
                       ["CS 486", "CS 492"], student_courses, ai_reqs)

    # Req 2: One of CS480 or CS485
    check_n_from_list("Complete one of: CS 480, CS 485",
                      ["CS 480", "CS 485"], n=1,
                      student_courses=student_courses, major_reqs=ai_reqs)

    # Req 3: 4 electives
    ai_electives = [
        "AMATH 449", "BIOL 487", "CO 367", "CO 456", "CO 463", "CO 466", "CS 452", "CS 479",
        "CS 480", "CS 484", "CS 485", "ECE 380", "ECE 423", "ECE 457C", "ECE 481", "ECE 486",
        "ECE 488", "ECE 495", "MTE 544", "SE 380", "STAT 341", "STAT 440", "STAT 441", "STAT 444",
        "SYDE 552", "SYDE 556", "SYDE 572"
    ]

    check_n_from_list("Complete 4 of the AI elective list",
                      ai_electives, n=4, student_courses=student_courses, major_reqs=ai_reqs)

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
        "Complete 2 of: ACTSC447, CS348, CS476, CS490": [False, []],
        "Complete 5 approved courses (min 2 at 200-level or higher)": [False, []]
    }

    core_options = ["ACTSC447", "CS348", "CS476", "CS490"]
    approved_courses = [
        "ACTSC231", "ACTSC372",
        "AFM101", "AFM102",
        "BUS121W", "BUS362W", "BUS381W", "BUS491W",
        "COMM101", "COMM400", "COMM432",
        "ECON101", "ECON102",
        "HRM200", "MGMT220", "MSE311"
    ]
    
    one_of_each_group_allowed = [
        ["AFM131", "ARBUS101", "BUS111W"],
        ["MSE211", "PSYCH238"]
    ]

    all_approved = approved_courses + [item for group in one_of_each_group_allowed for item in group]

    # Step 1: Core Options
    completed_core = [c for c in core_options if c in student_courses]
    if len(completed_core) >= 2:
        reqs["Complete 2 of: ACTSC447, CS348, CS476, CS490"][0] = True
        reqs["Complete 2 of: ACTSC447, CS348, CS476, CS490"][1].extend(completed_core[:2])
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
        "Complete all of: CS349, CS488": [False, []],
        "Complete 1 of: CS383 or FINE383": [False, []],
        "Complete 1 of: FINE100 or FINE130": [False, []],
        "Complete 1 of: FINE228 or FINE247": [False, []],
        "Complete 1 of: VCULT200 or VCULT257": [False, []],
    }

    # Check all of CS349 and CS488
    mandatory = ["CS349", "CS488"]
    if all(course in student_courses for course in mandatory):
        reqs["Complete all of: CS349, CS488"][0] = True
        reqs["Complete all of: CS349, CS488"][1].extend(mandatory)
        for c in mandatory:
            student_courses.remove(c)

    # Pairs to check for one-of requirements
    one_of_pairs = [
        ("Complete 1 of: CS383 or FINE383", ["CS383", "FINE383"]),
        ("Complete 1 of: FINE100 or FINE130", ["FINE100", "FINE130"]),
        ("Complete 1 of: FINE228 or FINE247", ["FINE228", "FINE247"]),
        ("Complete 1 of: VCULT200 or VCULT257", ["VCULT200", "VCULT257"]),
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
        "Complete all of: ECE124, ECE222, ECE327, ECE423": [False, []],
        "Complete 1 of: CS450 or ECE320": [False, []],
        "Complete 2 of: CS452, CS454, CS456, CS457": [False, []],
        "Complete 1 of: ECE224 or MTE325": [False, []],
        "Complete 1 of: GENE123 or MTE120": [False, []],
    }

    # 1. Required core courses
    check_complete_all(
        "Complete all of: ECE124, ECE222, ECE327, ECE423",
        ["ECE124", "ECE222", "ECE327", "ECE423"],
        student_courses,
        specialization_reqs
    )

    # 2. 1 of CS450 or ECE320
    check_n_from_list(
        "Complete 1 of: CS450 or ECE320",
        ["CS450", "ECE320"],
        1,
        student_courses,
        specialization_reqs
    )

    # 3. 2 of CS452, CS454, CS456, CS457
    check_n_from_list(
        "Complete 2 of: CS452, CS454, CS456, CS457",
        ["CS452", "CS454", "CS456", "CS457"],
        2,
        student_courses,
        specialization_reqs
    )

    # 4. 1 of ECE224 or MTE325
    check_n_from_list(
        "Complete 1 of: ECE224 or MTE325",
        ["ECE224", "MTE325"],
        1,
        student_courses,
        specialization_reqs
    )

    # 5. 1 of GENE123 or MTE120
    check_n_from_list(
        "Complete 1 of: GENE123 or MTE120",
        ["GENE123", "MTE120"],
        1,
        student_courses,
        specialization_reqs
    )

    return specialization_reqs

def check_game_design_specialization(student_courses):
    game_reqs = {
        "Complete all of: DAC204, DAC305": [False, []],
        "Complete 1 of: COMMST149, DAC209, DAC302, DAC309, ENGL392A, ENGL392B, ENGL408C, FINE247, THPERF149": [False, []],
        "Complete 1 of: COMMST210, COMMST339, COMMST430, COMMST435, ENGL293, GSJ205, SOC324": [False, []],
        "Complete 1 of: COMMST235 or ENGL294": [False, []],
        "Complete 2 of: CS449, CS454, CS488": [False, []],
    }

    # Required core
    check_complete_all(
        "Complete all of: DAC204, DAC305",
        ["DAC204", "DAC305"],
        student_courses,
        game_reqs
    )

    # Design & Rhetoric options
    check_n_from_list(
        "Complete 1 of: COMMST149, DAC209, DAC302, DAC309, ENGL392A, ENGL392B, ENGL408C, FINE247, THPERF149",
        ["COMMST149", "DAC209", "DAC302", "DAC309", "ENGL392A", "ENGL392B", "ENGL408C", "FINE247", "THPERF149"],
        1,
        student_courses,
        game_reqs
    )

    # Digital Culture options
    check_n_from_list(
        "Complete 1 of: COMMST210, COMMST339, COMMST430, COMMST435, ENGL293, GSJ205, SOC324",
        ["COMMST210", "COMMST339", "COMMST430", "COMMST435", "ENGL293", "GSJ205", "SOC324"],
        1,
        student_courses,
        game_reqs
    )

    # Game Studies core
    check_n_from_list(
        "Complete 1 of: COMMST235 or ENGL294",
        ["COMMST235", "ENGL294"],
        1,
        student_courses,
        game_reqs
    )

    # Technical electives
    check_n_from_list(
        "Complete 2 of: CS449, CS454, CS488",
        ["CS449", "CS454", "CS488"],
        2,
        student_courses,
        game_reqs
    )

    return game_reqs

def check_software_engineering_specialization(student_courses):
    software_eng_reqs = {
        "Complete 1 of: BET360, BET420, CS492, ENVS205, GEOG207, GEOG306, GSJ205, MSE422, MSE442, PACS315, SOC232, SOC324, STV202, STV205, STV306": [False, []],
        "Complete 2 of: CS343, CS346, CS348, CS349": [False, []],
        "Complete 2 of: CS442, CS444, CS448, CS449, CS450, CS451, CS452, CS453, CS454, CS456, CS457, CS459, CS480, CS484, CS486, CS488": [False, []],
        "Complete 1 of: CS445, ECE451": [False, []],
        "Complete 1 of: CS446, ECE452": [False, []],
        "Complete 1 of: CS447, ECE453": [False, []]
    }

    # Handle CS453/CS459 constraint: use only one of the two if both are present
    if "CS453" in student_courses and "CS459" in student_courses:
        # Remove one arbitrarily (you can tweak the logic if needed)
        student_courses.remove("CS459")

    check_n_from_list("Complete 1 of: BET360, BET420, CS492, ENVS205, GEOG207, GEOG306, GSJ205, MSE422, MSE442, PACS315, SOC232, SOC324, STV202, STV205, STV306",
                      ["BET360", "BET420", "CS492", "ENVS205", "GEOG207", "GEOG306", "GSJ205", "MSE422", "MSE442", "PACS315", "SOC232", "SOC324", "STV202", "STV205", "STV306"],
                      1, student_courses, software_eng_reqs)

    check_n_from_list("Complete 2 of: CS343, CS346, CS348, CS349",
                      ["CS343", "CS346", "CS348", "CS349"],
                      2, student_courses, software_eng_reqs)

    check_n_from_list("Complete 2 of: CS442, CS444, CS448, CS449, CS450, CS451, CS452, CS453, CS454, CS456, CS457, CS459, CS480, CS484, CS486, CS488",
                      ["CS442", "CS444", "CS448", "CS449", "CS450", "CS451", "CS452", "CS453", "CS454", "CS456", "CS457", "CS459", "CS480", "CS484", "CS486", "CS488"],
                      2, student_courses, software_eng_reqs)

    check_n_from_list("Complete 1 of: CS445, ECE451",
                      ["CS445", "ECE451"],
                      1, student_courses, software_eng_reqs)

    check_n_from_list("Complete 1 of: CS446, ECE452",
                      ["CS446", "ECE452"],
                      1, student_courses, software_eng_reqs)

    check_n_from_list("Complete 1 of: CS447, ECE453",
                      ["CS447", "ECE453"],
                      1, student_courses, software_eng_reqs)

    return software_eng_reqs

def check_hci_specialization(student_courses):
    hci_reqs = {
        "Complete all of: CS349, CS449": [False, []],
        "Complete 1 of: BET360, CS492, GSJ205, MSE442, PACS315, SOC232, STV202, STV205, STV208, STV210, STV302, STV304, STV305, STV306": [False, []],
        "Complete 2 of: ENGL108D, ENGL293, ENGL295, FINE100, FINE150, INTEG121, INTEG251, KIN320, PSYCH207, PSYCH261, STAT332, STAT430, VCULT257": [False, []],
        "Complete 2 of: CS454, CS480, CS484, CS486, CS488, (1 of CS445/ECE451/SE463), (1 of CS446/ECE452/SE464), (1 of CS447/ECE453/SE465), (1 of CS453/CS459)": [False, []],
    }

    # 1️⃣ Required core courses
    check_complete_all("Complete all of: CS349, CS449", ["CS349", "CS449"], student_courses, hci_reqs)

    # 2️⃣ Ethics & Society elective
    check_n_from_list("Complete 1 of: BET360, CS492, GSJ205, MSE442, PACS315, SOC232, STV202, STV205, STV208, STV210, STV302, STV304, STV305, STV306",
                      ["BET360", "CS492", "GSJ205", "MSE442", "PACS315", "SOC232", "STV202", "STV205", "STV208", "STV210", "STV302", "STV304", "STV305", "STV306"],
                      1, student_courses, hci_reqs)

    # 3️⃣ Cognitive/Psych/Design electives
    check_n_from_list("Complete 2 of: ENGL108D, ENGL293, ENGL295, FINE100, FINE150, INTEG121, INTEG251, KIN320, PSYCH207, PSYCH261, STAT332, STAT430, VCULT257",
                      ["ENGL108D", "ENGL293", "ENGL295", "FINE100", "FINE150", "INTEG121", "INTEG251", "KIN320", "PSYCH207", "PSYCH261", "STAT332", "STAT430", "VCULT257"],
                      2, student_courses, hci_reqs)

    # 4️⃣ Advanced technical electives (with group-of-1 logic for CS445/CS446/CS447/CS453)
    full_list = ["CS454", "CS480", "CS484", "CS486", "CS488"]

    # Handle “only one of” groups:
    groups = [
        ["CS445", "ECE451", "SE463"],
        ["CS446", "ECE452", "SE464"],
        ["CS447", "ECE453", "SE465"],
        ["CS453", "CS459"]
    ]

    used_courses = []

    for group in groups:
        for course in group:
            if course in student_courses:
                used_courses.append(course)
                student_courses.remove(course)
                break  # only count one from the group

    all_valid_courses = full_list + used_courses
    check_n_from_list("Complete 2 of: CS454, CS480, CS484, CS486, CS488, (1 of CS445/ECE451/SE463), (1 of CS446/ECE452/SE464), (1 of CS447/ECE453/SE465), (1 of CS453/CS459)",
                      all_valid_courses, 2, student_courses, hci_reqs)

    return hci_reqs
