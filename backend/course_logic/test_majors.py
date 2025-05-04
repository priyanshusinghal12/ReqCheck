from course_logic.checkStatisticsReqs import check_stats_major  # done?
from course_logic.checkActSciReqs import check_actsci_major # done
from course_logic.checkAMathReqs import check_amath_major # done
from course_logic.checkBioStatsReqs import check_biostats_major
from course_logic.checkCompMathReqs import check_comp_math_reqs # done
from course_logic.checkBCSCSReqs import check_bcs_cs_major
from course_logic.checkDataScienceReqs import check_data_science_major # done
from course_logic.checkMathDegreeReqs import check_math_degree_reqs # done
from course_logic.checkMathEconReqs import check_math_econ_reqs
from course_logic.checkMathFinanceReqs import check_math_finance_reqs
from course_logic.checkMathOptBusReqs import check_math_opt_bus_specialization # done
from course_logic.checkMathOptOpsReqs import check_math_opt_ops_specialization # done
from course_logic.checkMathPhysicsReqs import check_math_physics_reqs # done
from course_logic.checkMathStudiesBusReqs import math_studies_business_reqs #done 
from course_logic.checkMathStudiesReqs import math_studies_reqs # done
from course_logic.checkMathTeachReqs import check_math_teaching_major
from course_logic.checkPMathReqs import check_pmath_major # done
from course_logic.checkCOReqs import check_co_major # done
from course_logic.checkAFMReqs import check_afm_ba_reqs
from course_logic.checkAFMReqs import check_afm_entrepreneurial_mindset_reqs
from course_logic.checkAFMReqs import check_afm_enterprise_performance_risk_reqs
from course_logic.checkAFMReqs import check_afm_financial_markets_reqs
from course_logic.checkAFMReqs import check_afm_professional_accountant_reqs
from course_logic.checkAFMReqs import check_afm_sustainability_reqs
from course_logic.checkFARMReqs import check_farm_professional_risk_management_reqs
from course_logic.checkFARMReqs import check_farm_professional_fin_analyst_reqs

####################################################################
# FARM risk mgmt

farm_rm_test1 = ["ACTSC 231", "ACTSC 372", "AFM 101", "AFM 102", "AFM 131", "AMATH 350", "CO 372",
                 "COMM 101", "CS 330", "ECON 101", "ECON 102", "MATBUS 371", "STAT 371",
                 "MATBUS 470", "LS 283", "CO 250", "CS 335", "MATH 237", "STAT 334", "PMATH 330", "PMATH 333",
                 # specialization
                 "CS 338", "ACTSC 445", "PMATH 333", "STAT 341", "BUS 121W", "PSYCH 101", "CLAS 104", "BET 100"]

farm_rm_test1_expected = {
    "Complete all of the following: ACTSC 231, ACTSC 372, AFM 101, AFM 102, AFM 131, AMATH 350, CO 372, COMM 101, CS 330, ECON 101, ECON 102, MATBUS 371, STAT 371":
        [True, ["ACTSC 231", "ACTSC 372", "AFM 101", "AFM 102", "AFM 131", "AMATH 350", "CO 372", "COMM 101", "CS 330", "ECON 101", "ECON 102", "MATBUS 371", "STAT 371"]],
    
    "Complete 1 of the following: ACTSC 446, MATBUS 470":
        [True, ["MATBUS 470"]],
    
    "Complete 1 of the following: AFM 231, LS 283":
        [True, ["LS 283"]],
    
    "Complete 1 of the following: CO 250, CO 255":
        [True, ["CO 250"]],
    
    "Complete 1 of the following: CS 335, CS 476":
        [True, ["CS 335"]],
    
    "Complete 1 of the following: MATH 237, MATH 247":
        [True, ["MATH 237"]],
    
    "Complete one of the following: all of (STAT 330, STAT 333, additional ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT) or (STAT 334, 2 additional courses from ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT)":
        [True, ["STAT 334", "PMATH 330", "PMATH 333"]],  # Now CS 338 is used here, not again below
    
    "Complete all of the following: CS 338":
        [True, ["CS 338"]],  # CS 338 already used
    
    "Complete 1 of the following: ACTSC 445, MATBUS 472":
        [True, ["ACTSC 445"]],
    
    "Complete 1 of the following: AMATH 331, PMATH 331, PMATH 333, PMATH 351":
        [True, ["PMATH 333"]],
    
    "Complete 1 of the following: STAT 340, STAT 341":
        [True, ["STAT 341"]],
    
    "Complete 1 course from BUS, COMM, ECON, HRM, MSE":
        [True, ["BUS 121W"]],
    
    "Complete 3 additional courses":
        [True, ["PSYCH 101", "CLAS 104", "BET 100"]]
}


# Asserts
def test_farm_rm_1():
    assert check_farm_professional_risk_management_reqs(farm_rm_test1) == farm_rm_test1_expected

# FARM CFA specialization
farm_cfa_test1 = ["ACTSC 231", "ACTSC 372", "AFM 101", "AFM 102", "AFM 131", "AMATH 350", "CO 372",
                 "COMM 101", "CS 330", "ECON 101", "ECON 102", "MATBUS 371", "STAT 371",
                 "MATBUS 470", "LS 283", "CO 250", "CS 335", "MATH 237", "STAT 334", "PMATH 330", "PMATH 333",
                 # specialization
                 "COMM 321", "COMM 421", "COMM 433", "ARBUS 302", "ECON 206", "HRM 200", "PSYCH 101", "BET 100"]

farm_cfa_test1_expected = {
        "Complete all of the following: ACTSC 231, ACTSC 372, AFM 101, AFM 102, AFM 131, AMATH 350, CO 372, COMM 101, CS 330, ECON 101, ECON 102, MATBUS 471, STAT 371":
        [True, ["ACTSC 231", "ACTSC 372", "AFM 101", "AFM 102", "AFM 131", "AMATH 350", "CO 372", "COMM 101", "CS 330", "ECON 101", "ECON 102", "MATBUS 371", "STAT 371"]],
    
    "Complete 1 of the following: ACTSC 446, MATBUS 470":
        [True, ["MATBUS 470"]],
    
    "Complete 1 of the following: AFM 231, LS 283":
        [True, ["LS 283"]],
    
    "Complete 1 of the following: CO 250, CO 255":
        [True, ["CO 250"]],
    
    "Complete 1 of the following: CS 335, CS 476":
        [True, ["CS 335"]],
    
    "Complete 1 of the following: MATH 237, MATH 247":
        [True, ["MATH 237"]],
    
    "Complete one of the following: all of (STAT 330, STAT 333, additional ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT) or (STAT 334, 2 additional courses from ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT)":
        [True, ["STAT 334", "PMATH 330", "PMATH 333"]],

    # Specialization Requirements (Chartered Financial Analyst)
    "Complete all of the following: COMM 321, COMM 421, COMM 433": [True, ["COMM 321", "COMM 421", "COMM 433"]],
    "Complete 1 of the following: ARBUS 302, MGMT 244": [True, ["ARBUS 302"]],
    "Complete 1 of the following: ECON 206, ECON 207, ECON 290": [True, ["ECON 206"]],
    "Complete 1 of the following: HRM 200, MSE 211, PSYCH 238": [True, ["HRM 200"]],
    "Complete 2 additional courses": [True, ["PSYCH 101", "BET 100"]]
    }

# Asserts
def test_farm_cfa_1():
    assert check_farm_professional_fin_analyst_reqs(farm_cfa_test1) == farm_cfa_test1_expected

####################################################################
# AFM

# Business analytics specialization
afm_ba_test_1 = ["AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191", "AFM 205", "AFM 206", "AFM 207",
                "AFM 208", "AFM 241", "AFM 244", "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
                "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101", "ECON 102",
                "AFM 121", "AFM 272", "AFM 311", "AFM 345",
                # specialization reqs
                "AFM 346", "AFM 444", "AFM 445", "STAT 374"]

afm_ba_test_1_expected = {
    "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102":
        [True, ["AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191", "AFM 205", "AFM 206", "AFM 207",
                "AFM 208", "AFM 241", "AFM 244", "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
                "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101", "ECON 102"]],
    "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127":
        [True, ["AFM 121"]],
    "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273":
        [True, ["AFM 272"]],
    "Complete 1 of the following: AFM 311, SFM 309":
        [True, ["AFM 311"]],
    "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374":
        [True, ["AFM 345"]],
    "Complete 1 of the following AFM 345, AFM 346":
        [True, ["AFM 345"]],
    "Complete 4 of the following (or 3 if both AFM 345, 346 taken): ACTSC 423, AFM 323, AFM 341, AFM 345, AFM 346, AFM 347, AFM 423, AFM 444, AFM 445, AFM 446, AFM 447, AFM 448, STAT 374":
        [True, ["AFM 346", "AFM 444", "AFM 445", "STAT 374"]],
}

# Asserts
def test_afm_ba_1():
    assert check_afm_ba_reqs(afm_ba_test_1) == afm_ba_test_1_expected

# Entrepreneurial mindset specialization
test_afm_em = ["AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191", "AFM 205", "AFM 206", "AFM 207",
                "AFM 208", "AFM 241", "AFM 244", "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
                "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101", "ECON 102",
                "AFM 121", "AFM 272", "AFM 311", "AFM 345",
                # specialization reqs
                "BET 320", "BET 340", "AFM 326", "BET 350", "AFM 377"]


test_afm_em_expected = {
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102":
        [True, ["AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191", "AFM 205", "AFM 206", "AFM 207",
                "AFM 208", "AFM 241", "AFM 244", "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
                "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101", "ECON 102"]],
    "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127":
        [True, ["AFM 121"]],
    "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273":
        [True, ["AFM 272"]],
    "Complete 1 of the following: AFM 311, SFM 309":
        [True, ["AFM 311"]],
    "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374":
        [True, ["AFM 345"]],
        "Complete all of the following: BET 320, BET 340": [True, ["BET 320", "BET 340"]],
        "Complete 3 courses from the following: AFM 326, AFM 377, AFM 426, AFM 470, BET 350, BET 400, BET 420, BET 430, BET 450, BET 460, BET 470, BET 580, ENBUS 203, MGMT 220": [True, ["AFM 326", "AFM 377", "BET 350"]]
    }

# Asserts
def test_afm_em_1():
    assert check_afm_entrepreneurial_mindset_reqs(test_afm_em) == test_afm_em_expected

# Enterprise performance specialization
test_afm_erp = ["AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191", "AFM 205", "AFM 206", "AFM 207",
                "AFM 208", "AFM 241", "AFM 244", "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
                "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101", "ECON 102",
                "AFM 121", "AFM 272", "AFM 311", "AFM 345",
                # specialization reqs
                "AFM 434", "AFM 452", "AFM 482",
                "AFM 346", "AFM 347" # should work as AFM 345 will double count here
                ]

test_afm_erp_expected = {
        # Base AFM requirements
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102":
        [True, ["AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191", "AFM 205", "AFM 206", "AFM 207",
                "AFM 208", "AFM 241", "AFM 244", "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
                "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101", "ECON 102"]],
    "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127":
        [True, ["AFM 121"]],
    "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273":
        [True, ["AFM 272"]],
    "Complete 1 of the following: AFM 311, SFM 309":
        [True, ["AFM 311"]],
    "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374":
        [True, ["AFM 345"]],

        # Specialization requirements
        "Complete all of the following: AFM 434, AFM 452, AFM 482": [True, ["AFM 434", "AFM 452", "AFM 482"]],
        "Complete 3 of the following: AFM 276, AFM 322, AFM 345, AFM 346, AFM 347, AFM 445, AFM 451, AFM 470, AFM 477, AFM 485, SFM 301, SFM 310, SFM 311": [True, ["AFM 345", "AFM 346", "AFM 347"]]
    }

# Asserts
def test_afm_erp_1():
    assert check_afm_enterprise_performance_risk_reqs(test_afm_erp) == test_afm_erp_expected


# Financial markets specialization
test_afm_fm = ["AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191", "AFM 205", "AFM 206", "AFM 207",
                "AFM 208", "AFM 241", "AFM 244", "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
                "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101", "ECON 102",
                "AFM 121", "AFM 272", "AFM 311", "AFM 345",
                # specialization reqs
                "AFM 276", "AFM 322", "AFM 324",
                "AFM 423", "AFM 470", "AFM 478" # should work as AFM 345 will double count here
                ]

test_afm_fm_expected = {
        # Base AFM requirements
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102":
        [True, ["AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191", "AFM 205", "AFM 206", "AFM 207",
                "AFM 208", "AFM 241", "AFM 244", "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
                "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101", "ECON 102"]],
    "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127":
        [True, ["AFM 121"]],
    "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273":
        [True, ["AFM 272"]],
    "Complete 1 of the following: AFM 311, SFM 309":
        [True, ["AFM 311"]],
    "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374":
        [True, ["AFM 345"]],

        # Specialization requirements
    "Complete 3.0 units from the following: ACTSC 423, AFM 276, AFM 322, AFM 324, AFM 326, AFM 328, AFM 329, AFM 377, AFM 422, AFM 423, AFM 425, AFM 426, AFM 427, AFM 428, AFM 429, AFM 434, AFM 470, AFM 477, AFM 478, SFM 310, SFM 412": [True, ["AFM 276", "AFM 322", "AFM 324",
                "AFM 423", "AFM 470", "AFM 478"]]
    }

# Asserts
def test_afm_fm_1():
    assert check_afm_financial_markets_reqs(test_afm_fm) == test_afm_fm_expected


# Prof accounting specialization
afm_pro_acct_test = ["AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191", "AFM 205", "AFM 206", "AFM 207",
                "AFM 208", "AFM 241", "AFM 244", "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
                "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101", "ECON 102",
                "AFM 121", "AFM 272", "AFM 311", "AFM 345",
                # specialization reqs
                "AFM 362", "AFM 382", "AFM 451",
                "AFM 462", "AFM 482", "AFM 491" # should work as AFM 345 will double count here
                ]

afm_pro_acct_test_expected = {
        # Base AFM requirements
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102":
        [True, ["AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191", "AFM 205", "AFM 206", "AFM 207",
                "AFM 208", "AFM 241", "AFM 244", "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
                "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101", "ECON 102"]],
    "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127":
        [True, ["AFM 121"]],
    "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273":
        [True, ["AFM 272"]],
    "Complete 1 of the following: AFM 311, SFM 309":
        [True, ["AFM 311"]],
    "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374":
        [True, ["AFM 345"]],

        # Specialization requirements
    "Complete all of the following: AFM 362, AFM 382, AFM 451, AFM 462, AFM 482, AFM 491": [True, ["AFM 362", "AFM 382", "AFM 451",
                "AFM 462", "AFM 482", "AFM 491"]]
    }

# Asserts
def test_afm_prof_acct():
    assert check_afm_professional_accountant_reqs(afm_pro_acct_test) == afm_pro_acct_test_expected

# Sustainability specialization
afm_sust_test = ["AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191", "AFM 205", "AFM 206", "AFM 207",
                "AFM 208", "AFM 241", "AFM 244", "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
                "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101", "ECON 102",
                "AFM 121", "AFM 272", "AFM 311", "AFM 345",
                # specialization reqs
                "ENBUS 102", "ENVS 200", "ENVS 205", "AFM 485", "ENBUS 202", "ENBUS 407" # should work as AFM 345 will double count here
                ]

afm_sust_test_expected = {
        # Base AFM requirements
        "Complete all of: AFM 111, AFM 112, AFM 113, AFM 132, AFM 182, AFM 191, AFM 205, AFM 206, AFM 207, AFM 208, AFM 241, AFM 244, AFM 274, AFM 285, AFM 291, AFM 321, AFM 335, AFM 373, AFM 391, AFM 433, AFM 480, BET 100, COMMST 111, ECON 101, ECON 102":
        [True, ["AFM 111", "AFM 112", "AFM 113", "AFM 132", "AFM 182", "AFM 191", "AFM 205", "AFM 206", "AFM 207",
                "AFM 208", "AFM 241", "AFM 244", "AFM 274", "AFM 285", "AFM 291", "AFM 321", "AFM 335", "AFM 373",
                "AFM 391", "AFM 433", "AFM 480", "BET 100", "COMMST 111", "ECON 101", "ECON 102"]],
    "Complete 1 of the following: ACTSC 127, AFM 121, AFM 127":
        [True, ["AFM 121"]],
    "Complete 1 of the following: ACTSC 291, AFM 272, AFM 273":
        [True, ["AFM 272"]],
    "Complete 1 of the following: AFM 311, SFM 309":
        [True, ["AFM 311"]],
    "Complete 1 of the following: AFM 323, AFM 341, AFM 345, AFM 346, STAT 374":
        [True, ["AFM 345"]],

    # Sustainability specialization requirements
    "Complete 1 of the following: ENBUS 102, ENVS 195, ENVS 220, INDEV 100": [True, ["ENBUS 102"]],
    "Complete 2 of the following: ENVS 200, ENVS 205, ENVS 220, INDEV 200": [True, ["ENVS 200", "ENVS 205"]],
    "Complete all of the following either (AFM 485, ENBUS 202, ENBUS 407) or (ENBUS 310, ENBUS 408, ENBUS 410)": [True, ["AFM 485", "ENBUS 202", "ENBUS 407"]]
    }

# Asserts
def test_afm_sust():
    assert check_afm_sustainability_reqs(afm_sust_test) == afm_sust_test_expected

####################################################################
# COMPUTER SCIENCE

# Test Group A: Checking core reqs

# Case 1: All reqs met, 1 comms course from list 1 and second from list 2
cs_test_1 = ["CS 136L", "CS 341", "CS 350", "CS 135", "CS 136",
             "CS 240", "CS 241", "CS 245", "CS 246", "CS 251", "MATH 127",
             "MATH 128", "MATH 135", "MATH 136", "MATH 239", "STAT 230", "STAT 231",
             "CS 348", "CS 343", "CS 346", "CS 451", "CS 456", "CS 446",
             "COMMST 100",
             "ENGL 108D", # comms req - ENGL 108D being a list 2 course should also count in humanities breadth as per uni rules
             "CLAS 104", # One humanities breadth course left after ENGL 108 D
             "KIN 101", "PHYS 121", # pure & applied science
             "ECON 101", "ECON 102", # social sciences
             "ECON 351", # completes depth req
             ]


cs_test_1_expected = {
    "Complete all of: CS 136L, CS 341, CS 350": [True, ["CS 136L", "CS 341", "CS 350"]],
    "Complete one of: CS 115, CS 135, CS 145": [True, ["CS 135"]],
    "Complete one of: CS 136, CS 146": [True, ["CS 136"]],
    "Complete one of: CS 240, CS 240E": [True, ["CS 240"]],
    "Complete one of: CS 241, CS 241E": [True, ["CS 241"]],
    "Complete one of: CS 245, CS 245E": [True, ["CS 245"]],
    "Complete one of: CS 246, CS 246E": [True, ["CS 246"]],
    "Complete one of: CS 251, CS 251E": [True, ["CS 251"]],
    "Complete one course from List 1 (Communication Requirement 1)": [True, ["COMMST 100"]],
    "Complete one course from List 1 + List 2 (Communication Requirement 2)": [True, ["ENGL 108D"]],
    "Complete one of: MATH 127, MATH 137, MATH 147": [True, ["MATH 127"]],
    "Complete one of: MATH 128, MATH 138, MATH 148": [True, ["MATH 128"]],
    "Complete one of: MATH 135, MATH 145": [True, ["MATH 135"]],
    "Complete one of: MATH 136, MATH 146": [True, ["MATH 136"]],
    "Complete one of: MATH 239, MATH 249": [True, ["MATH 239"]],
    "Complete one of: STAT 230, STAT 240": [True, ["STAT 230"]],
    "Complete one of: STAT 231, STAT 241": [True, ["STAT 231"]],
    "Complete 3 additional CS courses from CS340-CS398, CS440-CS489": [True, ["CS 348", "CS 343", "CS 346"]],
    "Complete 2 additional CS courses from CS440-CS489": [True, ["CS 451", "CS 456"]],
    "Complete 1 of the following: (Complete 1 of: CO 487, CS 499T, STAT 440) or (1 course from CS440-CS498) or (a CS course from 600/700 level)": [True, ["CS 446"]],
    "Depth Requirement (does not check the prerequisite chain option)": [True, ["ECON 101", "ECON 102", "ECON 351"]],
    "Breadth Req - Humanities": [True, ["ENGL 108D", "CLAS 104"]],
    "Breadth Req - Pure Sciences": [True, ["PHYS 121"]],
    "Breadth Req - Pure and Applied Sciences": [True, ["KIN 101"]],
    "Breadth Req - Social Sciences": [True, ["ECON 101", "ECON 102"]],
}

# Case 2: All reqs met, both comms courses from list 1, missing depth req
cs_test_2 = ["CS 136L", "CS 341", "CS 350", "CS 135", "CS 136",
             "CS 240", "CS 241", "CS 245", "CS 246", "CS 251", "MATH 127",
             "MATH 128", "MATH 135", "MATH 136", "MATH 239", "STAT 230", "STAT 231",
             "CS 348", "CS 343", "CS 346", "CS 451", "CS 456", "CS 499T",
             "COMMST 100",
             "COMMST 223", # comms req - from list 1 so shouldn't count for humanities depth
             "CLAS 104", # One humanities breadth course
             "KIN 101", "PHYS 121", # pure & applied science
             "ECON 101", "ECON 102", # social sciences
             # missing depth
             ]

cs_test_2_expected = {
    "Complete all of: CS 136L, CS 341, CS 350": [True, ["CS 136L", "CS 341", "CS 350"]],
    "Complete one of: CS 115, CS 135, CS 145": [True, ["CS 135"]],
    "Complete one of: CS 136, CS 146": [True, ["CS 136"]],
    "Complete one of: CS 240, CS 240E": [True, ["CS 240"]],
    "Complete one of: CS 241, CS 241E": [True, ["CS 241"]],
    "Complete one of: CS 245, CS 245E": [True, ["CS 245"]],
    "Complete one of: CS 246, CS 246E": [True, ["CS 246"]],
    "Complete one of: CS 251, CS 251E": [True, ["CS 251"]],
    "Complete one course from List 1 (Communication Requirement 1)": [True, ["COMMST 100"]],
    "Complete one course from List 1 + List 2 (Communication Requirement 2)": [True, ["COMMST 223"]],
    "Complete one of: MATH 127, MATH 137, MATH 147": [True, ["MATH 127"]],
    "Complete one of: MATH 128, MATH 138, MATH 148": [True, ["MATH 128"]],
    "Complete one of: MATH 135, MATH 145": [True, ["MATH 135"]],
    "Complete one of: MATH 136, MATH 146": [True, ["MATH 136"]],
    "Complete one of: MATH 239, MATH 249": [True, ["MATH 239"]],
    "Complete one of: STAT 230, STAT 240": [True, ["STAT 230"]],
    "Complete one of: STAT 231, STAT 241": [True, ["STAT 231"]],
    "Complete 3 additional CS courses from CS340-CS398, CS440-CS489": [True, ["CS 348", "CS 343", "CS 346"]],
    "Complete 2 additional CS courses from CS440-CS489": [True, ["CS 451", "CS 456"]],
    "Complete 1 of the following: (Complete 1 of: CO 487, CS 499T, STAT 440) or (1 course from CS440-CS498) or (a CS course from 600/700 level)": [True, ["CS 499T"]],
    "Depth Requirement (does not check the prerequisite chain option)": [False, ["ECON 101", "ECON 102"]],
    "Breadth Req - Humanities": [False, ["CLAS 104"]],
    "Breadth Req - Pure Sciences": [True, ["PHYS 121"]],
    "Breadth Req - Pure and Applied Sciences": [True, ["KIN 101"]],
    "Breadth Req - Social Sciences": [True, ["ECON 101", "ECON 102"]],
}

# Asserts
def test_bcs_1():
    assert check_bcs_cs_major(cs_test_1) == cs_test_1_expected

def test_bcs_2():
    assert check_bcs_cs_major(cs_test_2) == cs_test_2_expected

# Needs two courses either both from list 1 or one each from lists 1,2
# test to check these 2 pass and that others don't pass

# Check that - Undergraduate Communication Requirement's List 1 courses do not satisfy the Humanities breadth requirement.
#  Courses found only in the Undergraduate Communication Requirement's List 2 can satisfy both the breadth requirement and the Undergraduate Communication Requirement.

####################################################################
# COMBINATORICS AND OPTIMIZATION

# All reqs met, all 3 courses in last option taken from first list 
co_test1 = [
    "CO 250", "CO 330", "CO 351", "MATH 239", "PMATH 336", 
    "CO 330", "CO 342", "CO 351", "CS 462", "CS 466", "CS 487",
    # Additional required courses
    "STAT 341", "STAT 441",
    "CO 481",
    "CS 230", "CS 231", "CS 234"
]

co_test1_expected = {
    "Complete one of: MATH 239, MATH 249": [True, ["MATH 239"]],
    "Complete one of: CO 250, CO 255": [True, ["CO 250"]],
    "Complete one of: CO 330, CO 342": [True, ["CO 330"]],
    "Complete one of: CO 351, CO 353, CO 367, or if CO 255 is taken, one of CO 450-471": [True, ["CO 351"]],
    "Complete one of: PMATH 336, PMATH 347": [True, ["PMATH 336"]],
    "Complete 3 of: CO 330, CO 331, CO 342, CO 351, CO 353, CO 367, CO 430, CO 431, CO 432, CO 434, CO 439, CO 440, CO 442, CO 444, CO 446, CO 450, CO 452, CO 454, CO 456, CO 459, CO 463, CO 466, CO 471, CO 481, CO 485, CO 486, CO 487, CS 467, PHYS 467": [True, ["CO 330", "CO 342", "CO 351"]],
    "Complete 3 of: MATH 237/247, AMATH 331/PMATH 331/PMATH 333, AMATH 332/PMATH 332, CS 462, CS 466, CS 487, PMATH 334/348, PMATH 340": [True, ["CS 462", "CS 466", "CS 487"]],
    "Complete 2 additional courses at the 300- or 400-level from: ACTSC, AMATH, CS, MATBUS, MATH, PMATH, STAT; excluding courses cross-listed with a CO course": [True, ["STAT 341", "STAT 441"]],
    "Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [True, ["CO 481"]],
    "Complete 3 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [True, ["CS 230", "CS 231", "CS 234"]]
}

# Case 2: CO 255 taken and last req is split across first list, MATH 237 and one more list
co_test2 = [
    "CO 255", "CO 330", "CO 446", "MATH 239", "PMATH 336", 
    "CO 330", "CO 342", "CO 466", "CS 487", "MATH 237", "PMATH 332",
    # Additional required courses
    "STAT 341", "STAT 441",
    "CO 481",
    "CS 230", "CS 231", "CS 234"
]

co_test2_expected = {
    "Complete one of: MATH 239, MATH 249": [True, ["MATH 239"]],
    "Complete one of: CO 250, CO 255": [True, ["CO 255"]],
    "Complete one of: CO 330, CO 342": [True, ["CO 330"]],
    "Complete one of: CO 351, CO 353, CO 367, or if CO 255 is taken, one of CO 450-471": [True, ["CO 466"]],
    "Complete one of: PMATH 336, PMATH 347": [True, ["PMATH 336"]],
    "Complete 3 of: CO 330, CO 331, CO 342, CO 351, CO 353, CO 367, CO 430, CO 431, CO 432, CO 434, CO 439, CO 440, CO 442, CO 444, CO 446, CO 450, CO 452, CO 454, CO 456, CO 459, CO 463, CO 466, CO 471, CO 481, CO 485, CO 486, CO 487, CS 467, PHYS 467": [True, ["CO 330", "CO 342", "CO 446"]],
    "Complete 3 of: MATH 237/247, AMATH 331/PMATH 331/PMATH 333, AMATH 332/PMATH 332, CS 462, CS 466, CS 487, PMATH 334/348, PMATH 340": [True, ["MATH 237", "AMATH 332", "CS 487"]],
    "Complete 2 additional courses at the 300- or 400-level from: ACTSC, AMATH, CS, MATBUS, MATH, PMATH, STAT; excluding courses cross-listed with a CO course": [True, ["STAT 341", "STAT 441"]],
    "Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [True, ["CO 481"]],
    "Complete 3 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [True, ["CS 230", "CS 231", "CS 234"]]
}

# Asserts
def test_co_1():
    assert check_co_major(co_test1) == co_test1_expected

def test_co_2():
    assert check_co_major(co_test2) == co_test2_expected

#######################################################################
# Math Degree Requirements

# Case 1: All reqs met, one comms course from list1, other from list 2
math_test1 = ["CS 115", "CS 116", "MATH 106", "MATH 127", "MATH 128", 
              "MATH 135", "MATH 235", "MATH 237", "STAT 230", "STAT 231",
              "SPCOM 100", "ENGL 378"]

math_test1_expected = {
    "Complete one of the following: CS 115, CS 135, CS 145": [True, ["CS 115"]],
    "Complete one of the following: CS 116, CS 136, CS 146": [True, ["CS 116"]],
    "Complete one of the following: MATH 106, MATH 136, MATH 146": [True, ["MATH 106"]],
    "Complete one of the following: MATH 127, MATH 137, MATH 147": [True, ["MATH 127"]],
    "Complete one of the following: MATH 128, MATH 138, MATH 148": [True, ["MATH 128"]],
    "Complete one of the following: MATH 135, MATH 145": [True, ["MATH 135"]],
    "Complete one of the following: MATH 235, MATH 245": [True, ["MATH 235"]],
    "Complete one of the following: MATH 237, MATH 239, MATH 247, MATH 249": [True, ["MATH 237"]],
    "Complete one of the following: STAT 230, STAT 240": [True, ["STAT 230"]],
    "Complete one of the following: STAT 231, STAT 241": [True, ["STAT 231"]],
    "1st Communication Skills Requirement": [True, ["SPCOM 100"]],
    "2nd Communication Skills Requirement": [True, ["ENGL 378"]]
}


# Case 2: All reqs met, both comms courses from list 1
math_test2 = ["CS 115", "CS 116", "MATH 106", "MATH 127", "MATH 128", 
              "MATH 135", "MATH 235", "MATH 237", "STAT 230", "STAT 231",
              "SPCOM 100", "ENGL 109"]

math_test2_expected = {
    "Complete one of the following: CS 115, CS 135, CS 145": [True, ["CS 115"]],
    "Complete one of the following: CS 116, CS 136, CS 146": [True, ["CS 116"]],
    "Complete one of the following: MATH 106, MATH 136, MATH 146": [True, ["MATH 106"]],
    "Complete one of the following: MATH 127, MATH 137, MATH 147": [True, ["MATH 127"]],
    "Complete one of the following: MATH 128, MATH 138, MATH 148": [True, ["MATH 128"]],
    "Complete one of the following: MATH 135, MATH 145": [True, ["MATH 135"]],
    "Complete one of the following: MATH 235, MATH 245": [True, ["MATH 235"]],
    "Complete one of the following: MATH 237, MATH 239, MATH 247, MATH 249": [True, ["MATH 237"]],
    "Complete one of the following: STAT 230, STAT 240": [True, ["STAT 230"]],
    "Complete one of the following: STAT 231, STAT 241": [True, ["STAT 231"]],
    "1st Communication Skills Requirement": [True, ["SPCOM 100"]],
    "2nd Communication Skills Requirement": [True, ["ENGL 109"]]
}

# Asserts
def test_math_1():
    assert check_math_degree_reqs(math_test1) == math_test1_expected

def test_math_2():
    assert check_math_degree_reqs(math_test2) == math_test2_expected

####################################################################
# Math Optimization - Business specialization

# Case 1: All reqs met
mo_bus_test1 = ["AFM 101", "CO 370", "ECON 101", "MSE 211", "STAT 340", "AMATH 242", "CO 250", 
                     "CO 342", "CO 452", "CO 463", "CS 330", "MATH 237", "MATH 239",
                     # specialization courses
                     "ACTSC 231", "AFM 102", "BUS 111W", "BUS 121W", "BUS 252W", "BUS 381W",
                     "CS 338", "ECON 102", "MSE 432", "STAT 371", "STAT 372",
                     "BUS 435W", "STAT 442"  # any 2 from the elective list
                     ]
 
mo_bus_test1_expected = {
    "Complete all of: AFM 101, CO 370, ECON 101, MSE 211, STAT 340": [True, ["AFM 101", "CO 370", "ECON 101", "MSE 211", "STAT 340"]],
    "Complete one of: AMATH 242, CS 370, CS 371": [True, ["AMATH 242"]],
    "Complete one of: CO 250, CO 255": [True, ["CO 250"]],
    "Complete 3 of: CO 342, CO 351, CO 353, CO 367, CO 372, CO 450, CO 452, CO 454, CO 456, CO 463, CO 466, CO 471": [True, ["CO 342", "CO 452", "CO 463"]],
    "Complete one of: CS 330, CS 490": [True, ["CS 330"]],
    "Complete one of: MATH 237, MATH 247": [True, ["MATH 237"]],
    "Complete one of: MATH 239, MATH 249": [True, ["MATH 239"]],
    "Complete all of: ACTSC 231, AFM 102, BUS 111W, BUS 121W, BUS 252W, BUS 381W, CS 338, ECON 102, MSE 432, STAT 371, STAT 372": [True, ["ACTSC 231", "AFM 102", "BUS 111W", "BUS 121W", "BUS 252W", "BUS 381W", "CS 338", "ECON 102", "MSE 432", "STAT 371", "STAT 372"]],
    "Complete 2 of: AMATH 350, BUS 435W, BUS 445W, BUS 455W, BUS 485W, CS 230, CS 234, MSE 311, MSE 436, STAT 440, STAT 442, STAT 444": [True, ["BUS 435W", "STAT 442"]]
}

def test_mo_bus_1():
    assert check_math_opt_bus_specialization(mo_bus_test1) == mo_bus_test1_expected

# Math optimization - Operations Research Specialization

# Case 1: All reqs met
mo_or_test1 = ["AFM 101", "CO 370", "ECON 101", "MSE 211", "STAT 340", "AMATH 242", "CO 250", 
                     "CO 342", "CO 452", "CO 463", "CS 330", "MATH 237", "MATH 239",
                     # specialization courses
                    "CS 234", "STAT 331", "STAT 333",
                    "ECON 102", "MSE 432",  # any 2 from that group
                    "STAT 443",             # any 1 from that group
                    "CO 351",               # or CO 353
                    "PMATH 330", "STAT 341"]

mo_or_test1_expected = {
    "Complete all of: AFM 101, CO 370, ECON 101, MSE 211, STAT 340": [True, ["AFM 101", "CO 370", "ECON 101", "MSE 211", "STAT 340"]],
    "Complete one of: AMATH 242, CS 370, CS 371": [True, ["AMATH 242"]],
    "Complete one of: CO 250, CO 255": [True, ["CO 250"]],
    "Complete 3 of: CO 342, CO 351, CO 353, CO 367, CO 372, CO 450, CO 452, CO 454, CO 456, CO 463, CO 466, CO 471": [True, ["CO 342", "CO 452", "CO 463"]],
    "Complete one of: CS 330, CS 490": [True, ["CS 330"]],
    "Complete one of: MATH 237, MATH 247": [True, ["MATH 237"]],
    "Complete one of: MATH 239, MATH 249": [True, ["MATH 239"]],
    # Specialization reqs
    "Complete all of: CS 234, STAT 331, STAT 333": [True, ["CS 234", "STAT 331", "STAT 333"]],
    "Complete 2 of: AFM 102, ECON 102, MSE 311, MSE 432": [True, ["ECON 102", "MSE 432"]],
    "Complete one of: AMATH 250, AMATH 251, CO 487, CS 338, CS 430, STAT 332, STAT 433, STAT 435, STAT 443": [True, ["STAT 443"]],
    "Complete one of: CO 351, CO 353 or, if CO 255 is taken, one of: CO 450, CO 452, CO 454, CO 456, CO 459, CO 463, CO 466, CO 471": [True, ["CO 351"]],
    "Complete 2 additional math courses from the following subject codes: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [True, ["PMATH 330", "STAT 341"]],
}

# Case 2: CO 255 taken

mo_or_test2 = ["AFM 101", "CO 370", "ECON 101", "MSE 211", "STAT 340", "AMATH 242", "CO 255", 
                     "CO 342", "CO 351", "CO 463", "CS 330", "MATH 237", "MATH 239",
                     # specialization courses
                    "CS 234", "STAT 331", "STAT 333",
                    "ECON 102", "MSE 432",  # any 2 from that group
                    "STAT 443",             # any 1 from that group
                    "CO 459",               # or CO 353
                    "PMATH 330", "STAT 341"]

mo_or_test2_expected = {
    "Complete all of: AFM 101, CO 370, ECON 101, MSE 211, STAT 340": [True, ["AFM 101", "CO 370", "ECON 101", "MSE 211", "STAT 340"]],
    "Complete one of: AMATH 242, CS 370, CS 371": [True, ["AMATH 242"]],
    "Complete one of: CO 250, CO 255": [True, ["CO 255"]],
    "Complete 3 of: CO 342, CO 351, CO 353, CO 367, CO 372, CO 450, CO 452, CO 454, CO 456, CO 463, CO 466, CO 471": [True, ["CO 342", "CO 351", "CO 463"]],
    "Complete one of: CS 330, CS 490": [True, ["CS 330"]],
    "Complete one of: MATH 237, MATH 247": [True, ["MATH 237"]],
    "Complete one of: MATH 239, MATH 249": [True, ["MATH 239"]],
    # Specialization reqs
    "Complete all of: CS 234, STAT 331, STAT 333": [True, ["CS 234", "STAT 331", "STAT 333"]],
    "Complete 2 of: AFM 102, ECON 102, MSE 311, MSE 432": [True, ["ECON 102", "MSE 432"]],
    "Complete one of: AMATH 250, AMATH 251, CO 487, CS 338, CS 430, STAT 332, STAT 433, STAT 435, STAT 443": [True, ["STAT 443"]],
    "Complete one of: CO 351, CO 353 or, if CO 255 is taken, one of: CO 450, CO 452, CO 454, CO 456, CO 459, CO 463, CO 466, CO 471": [True, ["CO 459"]],
    "Complete 2 additional math courses from the following subject codes: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [True, ["PMATH 330", "STAT 341"]],
}

def test_mo_or_1():
    assert check_math_opt_ops_specialization(mo_or_test1) == mo_or_test1_expected

def test_mo_or_2():
    assert check_math_opt_ops_specialization(mo_or_test2) == mo_or_test2_expected

####################################################################
# BMath data science

bmath_ds_test0 = ["CS 136L", "CS 341", "CS 348", "CS 431", "ENGL 378", "STAT 330", "STAT 331", "STAT 332", "STAT 333", "STAT 341",
           "CS 136", "CS 240", "CS 241", "CS 245", "CS 246", "CS 251", "CS 480", "MATH 237", "MATH 239", "STAT 431", "STAT 442", "PMATH 330"]

bmath_ds_test0_expected = {
    "Complete all of the following: CS 136L, CS 341, CS 348, CS 431, STAT 330, STAT 331, STAT 332, STAT 333, STAT 341": [True, ["CS 136L", "CS 341", "CS 348", "CS 431", "STAT 330", "STAT 331", "STAT 332", "STAT 333", "STAT 341"]],
    "Complete 1 of the following: CS 136, CS 146": [True, ["CS 136"]],
    "Complete 1 of the following: CS 240, CS 240E": [True, ["CS 240"]],
    "Complete 1 of the following: CS 241, CS 241E": [True, ["CS 241"]],
    "Complete 1 of the following: CS 245, CS 245E": [True, ["CS 245"]],
    "Complete 1 of the following: CS 246, CS 246E": [True, ["CS 246"]],
    "Complete 1 of the following: CS 251, CS 251E": [True, ["CS 251"]],
    "Complete 1 of the following: CS 480, CS 484, CS 485, CS 486, STAT 441": [True, ["CS 480"]],
    "Complete 2 of the following: STAT 431, STAT 440, STAT 441, STAT 442, STAT 443, STAT 444": [True, ["STAT 431", "STAT 442"]],
    "Complete 1 of the following: ENGL 378, MTHEL 300": [True, ["ENGL 378"]],
    "Complete 1 of the following: MATH 237, MATH 247": [True, ["MATH 237"]],
    "Complete 1 of the following: MATH 239, MATH 249": [True, ["MATH 239"]],
    "Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [True, ["PMATH 330"]]
}


def test_ds_0():
    assert check_data_science_major(bmath_ds_test0) == bmath_ds_test0_expected

####################################################################
# Math phys

mathphys_test0 = ["AMATH 231", "AMATH 271", "AMATH 353", "AMATH 361", "PHYS 121", "PHYS 122", "PHYS 242",
                  "AMATH 242",
                 "AMATH 345", "AMATH 250", "PMATH 331", "AMATH 332", "AMATH 373", "PHYS 454", "PHYS 476", "AMATH 333", "PHYS 359", "PHYS 358", "MATH 237",
                 "AMATH 240", "PHYS 240", "AMATH 340", "PHYS 340", "AMATH 341", "PHYS 200",
                 ]

mathphys_test0_expected = {'Complete all the following: AMATH 231, AMATH 271, AMATH 353, AMATH 361, PHYS 121, PHYS 122, PHYS 242': [True,
  ['AMATH 231',
   'AMATH 271',
   'AMATH 353',
   'AMATH 361',
   'PHYS 121',
   'PHYS 122',
   'PHYS 242']],
 'Complete one of the following: AMATH 242, AMATH 345, AMATH 391, AMATH 445, CS 371': [True,
  ['AMATH 242']],
 'Complete one of the following: AMATH 250, AMATH 251': [True, ['AMATH 250']],
 'Complete one of the following: AMATH 331, PMATH 331, PMATH 333, PMATH 351': [True,
  ['PMATH 331']],
 'Complete one of the following: AMATH 332, PMATH 332, PMATH 352': [True,
  ['AMATH 332']],
 'Complete either AMATH 373, or both of PHYS 234 and PHYS 334': [True,
  ['AMATH 373']],
 'Complete one of the following: AMATH 473, PHYS 454': [True, ['PHYS 454']],
 'Complete one of the following: AMATH 475, PHYS 476': [True, ['PHYS 476']],
 'Complete 2 of the following: AMATH 333, AMATH 474, PHYS 359, PHYS 484': [True,
  ['AMATH 333', 'PHYS 359']],
 'Complete one of the following: ECE 403, PHYS 358': [True, ['PHYS 358']],
 'Complete one of the following: MATH 237, MATH 247': [True, ['MATH 237']],
 'Complete 1.5 additional units from AMATH or PHYS at the 300 or 400 level': [True,
  ['AMATH 345', 'AMATH 340', 'PHYS 340']],
 'Complete 1.5 additional units from AMATH or PHYS at any level': [True,
  ['AMATH 240', 'PHYS 240', 'AMATH 341']]}

def test_mathphys():
    assert check_math_physics_reqs(mathphys_test0) == mathphys_test0_expected

####################################################################

# STATISTICS 

# Case 1: All reqs met, both CS 371 & AMATH 250 done with CS 371 placed first
stats_test1 = [
    "STAT 330", "STAT 331", "STAT 332", "STAT 333",  # Core STAT courses
    "ENGL 378",  # Communication option 1
    "MATH 237",  # Calculus option 1
    "CS 371",
    "AMATH 250",  #  IMPORTANT: CS 371 placed first to check it's not used, AMATH 250 should be used for advanced math requirement
    "STAT 440", "STAT 441",  # 2 STAT courses at the 400-level
    "STAT 341",# 1 additional STAT course at the 300/400 level
    "CS 486", # USING CS 486 INSTEAD OF 1 additional STAT 400-level course
    "ACTSC 371", "AMATH 350", "CO 487", # after including CS 371 this should form 4 additional 300/400 level courses
    "ACTSC 231", "AMATH 242", "CO 250" # 3 additional courses
]

stats_test1_expected = {
    'Complete all of: STAT 330, STAT 331, STAT 332, STAT 333': [True, ['STAT 330', 'STAT 331', 'STAT 332', 'STAT 333']],
    'Complete one of: ENGL 378, MTHEL 300': [True, ['ENGL 378']],
    'Complete one of: MATH 237, MATH 247': [True, ['MATH 237']], 
    'Complete one of: AMATH 231, AMATH 242, AMATH 250, AMATH 251, AMATH 350, CS 371, MATH 239, MATH 249': [True, ['AMATH 250']], 
    'Complete 2 additional STAT courses at the 400 level': [True, ['STAT 440', 'STAT 441']], 
    'Complete 1 additional STAT courses at the 300/400 level': [True, ['STAT 341']], 
    'Complete either 1 additional STAT 400-level course or one of: CS 457, CS 485, CS 486': [True, ['CS 486']], 
    'Complete 4 additional 300/400 level courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [True, ['CS 371', 'ACTSC 371', 'AMATH 350', 'CO 487']], 
    'Complete 3 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [True, ['ACTSC 231', 'AMATH 242', 'CO 250']]}

# Case 2: using 400 level STAT in both the 3/4XX option and the CS option. Also, using STAT 341 for second last req.
stats_test2 = [
    "STAT 330", "STAT 331", "STAT 333",  # Missing a stats core course
    "MTHEL 300",  # Communication option 1
    "MATH 237",  # Calculus option 1
    "CS 371",
    "AMATH 250",  #  IMPORTANT: CS 371 placed first to check it's not used, AMATH 250 should be used for advanced math requirement
    "STAT 440", "STAT 441",  # 2 STAT courses at the 400-level
    "STAT 468",# 1 additional STAT course at the 300/400 level
    "STAT 444", # Using 1 additional STAT 400-level course instead of CS options
    "ACTSC 371", "AMATH 350", "STAT 341", # after including CS 371 this should form 4 additional 300/400 level courses
    "ACTSC 231", "AMATH 242" # 3 additional courses
]

stats_test2_expected = {
    'Complete all of: STAT 330, STAT 331, STAT 332, STAT 333': [False, ['STAT 330', 'STAT 331', 'STAT 333']],
    'Complete one of: ENGL 378, MTHEL 300': [True, ['MTHEL 300']],
    'Complete one of: MATH 237, MATH 247': [True, ['MATH 237']], 
    'Complete one of: AMATH 231, AMATH 242, AMATH 250, AMATH 251, AMATH 350, CS 371, MATH 239, MATH 249': [True, ['AMATH 250']], 
    'Complete 2 additional STAT courses at the 400 level': [True, ['STAT 440', 'STAT 441']], 
    'Complete 1 additional STAT courses at the 300/400 level': [True, ['STAT 444']], 
    'Complete either 1 additional STAT 400-level course or one of: CS 457, CS 485, CS 486': [True, ['STAT 468']], 
    'Complete 4 additional 300/400 level courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [True, ['CS 371', 'ACTSC 371', 'AMATH 350', 'STAT 341']], 
    'Complete 3 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [False, ['ACTSC 231', 'AMATH 242']]}

# Assert statements for statistics
def test_stats_1():
    assert check_stats_major(stats_test1) == stats_test1_expected

def test_stats_2():
    assert check_stats_major(stats_test2) == stats_test2_expected

####################################################################

# ACTUARIAL SCIENCE

# Case 1: All reqs met
actsci_test1 = [
    "MATH 237", "AMATH 250", "AFM 101", "ACTSC 231", "ACTSC 232",
    "ACTSC 331", "ACTSC 363", "ACTSC 372", "ACTSC 431", "ACTSC 446",
    "ECON 101", "ECON 102", "ENGL 378", "MTHEL 131", "STAT 330",
    "STAT 331", "STAT 333", "STAT 340", "ACTSC 450", "ACTSC 460",
    "ACTSC 340", "AFM 424", "STAT 431"
]

actsci_test1_expected = {'Complete all of: ACTSC 231, ACTSC 232, ACTSC 331, ACTSC 363, ACTSC 372, ACTSC 431, ACTSC 446, AFM 101, ECON 101, ECON 102, MTHEL 131, STAT 330, STAT 331, STAT 333': [True,
  ['ACTSC 231',
   'ACTSC 232',
   'ACTSC 331',
   'ACTSC 363',
   'ACTSC 372',
   'ACTSC 431',
   'ACTSC 446',
   'AFM 101',
   'ECON 101',
   'ECON 102',
   'MTHEL 131',
   'STAT 330',
   'STAT 331',
   'STAT 333']],
 'Complete one of: AMATH 250, AMATH 251, AMATH 350': [True, ['AMATH 250']],
 'Complete one of: ENGL 378, MTHEL 300': [True, ['ENGL 378']],
 'Complete one of: MATH 237, MATH 247': [True, ['MATH 237']],
 'Complete one of: STAT 340, STAT 341': [True, ['STAT 340']],
 'Complete 2 additional ACTSC courses at the 400-level': [True,
  ['ACTSC 450', 'ACTSC 460']],
 'Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [True,
  ['ACTSC 340']],
 'Complete 2 additional courses from these options: any ACTSC 3XX/4XX, AFM 424, STAT 431, STAT 433, STAT 441, STAT 443': [True,
  ['AFM 424', 'STAT 431']]}

# Case 2: All reqs met except - missing some core courses. Also, done 3 ACTSC 400 course to meet reqs 6 and 7.
# For last req, took once course from ACTSC option and one from list.
actsci_test2 = [
    "MATH 237", "AMATH 250", "ACTSC 231", "ACTSC 331", "ACTSC 363",
    "ACTSC 372", "ECON 101", "ENGL 378", "STAT 330", "STAT 333",
    "STAT 340", "ACTSC 450", "ACTSC 340", "AFM 424", "ACTSC 490", "ACTSC 400"
]

actsci_test2_expected = {'Complete all of: ACTSC 231, ACTSC 232, ACTSC 331, ACTSC 363, ACTSC 372, ACTSC 431, ACTSC 446, AFM 101, ECON 101, ECON 102, MTHEL 131, STAT 330, STAT 331, STAT 333': [False,
  ['ACTSC 231',
   'ACTSC 331',
   'ACTSC 363',
   'ACTSC 372',
   'ECON 101',
   'STAT 330',
   'STAT 333']],
 'Complete one of: AMATH 250, AMATH 251, AMATH 350': [True, ['AMATH 250']],
 'Complete one of: ENGL 378, MTHEL 300': [True, ['ENGL 378']],
 'Complete one of: MATH 237, MATH 247': [True, ['MATH 237']],
 'Complete one of: STAT 340, STAT 341': [True, ['STAT 340']],
 'Complete 2 additional ACTSC courses at the 400-level': [True,
  ['ACTSC 450', 'ACTSC 490']],
 'Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [True,
  ['ACTSC 400']],
 'Complete 2 additional courses from these options: any ACTSC 3XX/4XX, AFM 424, STAT 431, STAT 433, STAT 441, STAT 443': [True,
  ['AFM 424', 'ACTSC 340']]
                         }

# Case 3: Last req - took both options from the list
actsci_test3 = [
    "STAT 433", "CS 330", "MATH 237", "AMATH 250", "AFM 101", "ACTSC 231", "ACTSC 232",
    "ACTSC 331", "ACTSC 363", "ACTSC 372", "ACTSC 431", "ACTSC 446",
    "ECON 101", "ECON 102", "ENGL 378", "MTHEL 131", "STAT 330",
    "STAT 331", "STAT 333", "STAT 340", "ACTSC 450", "AFM 424"
]

actsci_test3_expected = {'Complete all of: ACTSC 231, ACTSC 232, ACTSC 331, ACTSC 363, ACTSC 372, ACTSC 431, ACTSC 446, AFM 101, ECON 101, ECON 102, MTHEL 131, STAT 330, STAT 331, STAT 333': [True,
  ['ACTSC 231',
   'ACTSC 232',
   'ACTSC 331',
   'ACTSC 363',
   'ACTSC 372',
   'ACTSC 431',
   'ACTSC 446',
   'AFM 101',
   'ECON 101',
   'ECON 102',
   'MTHEL 131',
   'STAT 330',
   'STAT 331',
   'STAT 333']],
 'Complete one of: AMATH 250, AMATH 251, AMATH 350': [True, ['AMATH 250']],
 'Complete one of: ENGL 378, MTHEL 300': [True, ['ENGL 378']],
 'Complete one of: MATH 237, MATH 247': [True, ['MATH 237']],
 'Complete one of: STAT 340, STAT 341': [True, ['STAT 340']],
 'Complete 2 additional ACTSC courses at the 400-level': [False,
  ['ACTSC 450']],
 'Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [True,
  ['CS 330']],
 'Complete 2 additional courses from these options: any ACTSC 3XX/4XX, AFM 424, STAT 431, STAT 433, STAT 441, STAT 443': [True,
  ['AFM 424', 'STAT 433']]}

# passes all but has some courses with W at the end for elective, eg. MATBUS 300W

actsci_test4 = [
    "MATH 237", "AMATH 250", "AFM 101", "ACTSC 231", "ACTSC 232",
    "ACTSC 331", "ACTSC 363", "ACTSC 372", "ACTSC 431", "ACTSC 446",
    "ECON 101", "ECON 102", "ENGL 378", "MTHEL 131", "STAT 330",
    "STAT 331", "STAT 333", "STAT 340", "ACTSC 450", "ACTSC 460",
    "MATBUS 300W", "AFM 424", "STAT 431"
]

actsci_test4_expected = {'Complete all of: ACTSC 231, ACTSC 232, ACTSC 331, ACTSC 363, ACTSC 372, ACTSC 431, ACTSC 446, AFM 101, ECON 101, ECON 102, MTHEL 131, STAT 330, STAT 331, STAT 333': [True,
  ['ACTSC 231',
   'ACTSC 232',
   'ACTSC 331',
   'ACTSC 363',
   'ACTSC 372',
   'ACTSC 431',
   'ACTSC 446',
   'AFM 101',
   'ECON 101',
   'ECON 102',
   'MTHEL 131',
   'STAT 330',
   'STAT 331',
   'STAT 333']],
 'Complete one of: AMATH 250, AMATH 251, AMATH 350': [True, ['AMATH 250']],
 'Complete one of: ENGL 378, MTHEL 300': [True, ['ENGL 378']],
 'Complete one of: MATH 237, MATH 247': [True, ['MATH 237']],
 'Complete one of: STAT 340, STAT 341': [True, ['STAT 340']],
 'Complete 2 additional ACTSC courses at the 400-level': [True,
  ['ACTSC 450', 'ACTSC 460']],
 'Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [True,
  ['MATBUS 300W']],
 'Complete 2 additional courses from these options: any ACTSC 3XX/4XX, AFM 424, STAT 431, STAT 433, STAT 441, STAT 443': [True,
  ['AFM 424', 'STAT 431']]}


# Case 5: checking that ACTSC 4XX is not unnecessarily used when ACTSC 3XX can be used

actsci_test5 = [
    'ACTSC 300', #ACTSC 3XX
    'AMATH 350', # diff eqns
    'ACTSC 231', 'ACTSC 232', 'ACTSC 331',
   'ACTSC 363', # core
   'ACTSC 450', 'ACTSC 460', # ACTSC 400
   'ACTSC 372',
   'ACTSC 431',
   'ACTSC 446',
   'AFM 101',
   'ACTSC 351', # ACTSC 3XX
   'ECON 101',
   'ECON 102',
    'MTHEL 131',
   'STAT 330',
   'STAT 331',
   'STAT 333', # core
   'MTHEL 300', # comms
   'MATH 247', 'STAT 340'
]

actsci_test5_expected = {'Complete all of: ACTSC 231, ACTSC 232, ACTSC 331, ACTSC 363, ACTSC 372, ACTSC 431, ACTSC 446, AFM 101, ECON 101, ECON 102, MTHEL 131, STAT 330, STAT 331, STAT 333': [True,
  ['ACTSC 231',
   'ACTSC 232',
   'ACTSC 331',
   'ACTSC 363',
   'ACTSC 372',
   'ACTSC 431',
   'ACTSC 446',
   'AFM 101',
   'ECON 101',
   'ECON 102',
   'MTHEL 131',
   'STAT 330',
   'STAT 331',
   'STAT 333']],
 'Complete one of: AMATH 250, AMATH 251, AMATH 350': [True, ['AMATH 350']],
 'Complete one of: ENGL 378, MTHEL 300': [True, ['MTHEL 300']],
 'Complete one of: MATH 237, MATH 247': [True, ['MATH 247']],
 'Complete one of: STAT 340, STAT 341': [True, ['STAT 340']],
 'Complete 2 additional ACTSC courses at the 400-level': [True,
  ['ACTSC 450', 'ACTSC 460']],
 'Complete 1 additional course at the 300- or 400-level from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [False, [],],
 'Complete 2 additional courses from these options: any ACTSC 3XX/4XX, AFM 424, STAT 431, STAT 433, STAT 441, STAT 443': [True,
  ['ACTSC 300', 'ACTSC 351']]}


# Asserts for ActSci
def test_actsci_1():
    assert check_actsci_major(actsci_test1) == actsci_test1_expected

def test_actsci_2():
    assert check_actsci_major(actsci_test2) == actsci_test2_expected

def test_actsci_3():
    assert check_actsci_major(actsci_test3) == actsci_test3_expected

def test_actsci_4():
    assert check_actsci_major(actsci_test4) == actsci_test4_expected

def test_actsci_5():
    assert check_actsci_major(actsci_test5) == actsci_test5_expected

####################################################################

# AMATH

# Case 0: All reqs met, also checks AMATH 4XX is not being used where AMATH 3XX can be
amath_test0 = ['CS 371', 'AMATH 251', 'PMATH 332',
'ME 400',
'CS 330',
'MATH 247',
'AMATH 300',
'MTE 200',
'AMATH 400',
'AMATH 450', 'AMATH 468',
'AMATH 340', 'AMATH 470',
'ME 238',
'MTE 300',
# core courses
'AMATH 231', 'AMATH 342', 'AMATH 351', 'AMATH 353', 'PHYS 121'
]

amath_test0_expected = {'Complete all of: AMATH 231, AMATH 342, AMATH 351, AMATH 353, PHYS 121': [True, ['AMATH 231', 'AMATH 342', 'AMATH 351', 'AMATH 353', 'PHYS 121']],
                   'Complete one of: AMATH 242, CS 371': [True, ['CS 371']],
                   'Complete one of: AMATH 250, AMATH 251': [True, ['AMATH 251']],
                   'Complete one of: AMATH 332, PMATH 332, PMATH 352': [True, ['PMATH 332']],
                   'Complete one of: MATH 237, MATH 247': [True, ['MATH 247']],
                   'Complete 3 AMATH courses at the 400 level': [True,
                                                                ['AMATH 400', 'AMATH 450', 'AMATH 468']],
                   'Complete 1 additional AMATH course at the 300/400 level': [True,
                                                                               ['AMATH 300']],
                   'Complete 5 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [False,
                                                                                                         ['CS 330', 'AMATH 340', 'AMATH 470']],
                   'Complete 4 additional courses, all from the same subject code from: AE, BIOL, BME/SYDE, CHE, CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME/MTE, MNS, MSE, NE, PHYS': [True,
                                                                                                                                                                                              ['ME 400', 'MTE 200', 'ME 238', 'MTE 300']]
                   }



# Case 1: Some core missing, econ specialization and AMATH 301 to fulfil the 300/400 option
amath_test1 = ["AMATH 431", "BET 100", "AMATH 420",
               "AMATH 351", "PMATH 332",
               "MATH 237",
                "CS 371", "AMATH 478",
               "ECON 201", "ECON 207", "ECON 250", "ECON 350", "AMATH 301"]

amath_test1_expected = {
    'Complete all of: AMATH 231, AMATH 342, AMATH 351, AMATH 353, PHYS 121': [False, ["AMATH 351"]],
    'Complete one of: AMATH 242, CS 371': [True, ["CS 371"]],
    'Complete one of: AMATH 250, AMATH 251': [False, []],
    'Complete one of: AMATH 332, PMATH 332, PMATH 352': [True, ["PMATH 332"]],
    'Complete one of: MATH 237, MATH 247': [True, ["MATH 237"]],
    'Complete 3 AMATH courses at the 400 level': [True, ["AMATH 431", "AMATH 420", "AMATH 478"]],
    'Complete 1 additional AMATH course at the 300/400 level': [True, ["AMATH 301"]],
    'Complete 5 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [False, []],
    'Complete 4 additional courses, all from the same subject code from: AE, BIOL, BME/SYDE, CHE, CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME/MTE, MNS, MSE, NE, PHYS': [True, ["ECON 201", "ECON 207", "ECON 250", "ECON 350"]]
}



# Test 2: Concentration split between 2 ME and 2 MTE
amath_test2 = ["AMATH 431", "ENGL 100", "ME 400", "AMATH 420", "ECON 450",
          "AMATH 480", "AMATH 351", "MTE 200", "PHYS 121", "ME 238", "PMATH 332",
          "MATH 237", "CS 371", "AMATH 478", "MTE 300"]

amath_test2_expected = {'Complete all of: AMATH 231, AMATH 342, AMATH 351, AMATH 353, PHYS 121': [False, ['AMATH 351', 'PHYS 121']],
                   'Complete one of: AMATH 242, CS 371': [True, ['CS 371']],
                   'Complete one of: AMATH 250, AMATH 251': [False, []],
                   'Complete one of: AMATH 332, PMATH 332, PMATH 352': [True, ['PMATH 332']],
                   'Complete one of: MATH 237, MATH 247': [True, ['MATH 237']],
                   'Complete 3 AMATH courses at the 400 level': [True,
                                                                ['AMATH 431', 'AMATH 420', 'AMATH 480']],
                   'Complete 1 additional AMATH course at the 300/400 level': [True,
                                                                               ['AMATH 478']],
                   'Complete 5 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [False,
                                                                                                         []],
                   'Complete 4 additional courses, all from the same subject code from: AE, BIOL, BME/SYDE, CHE, CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME/MTE, MNS, MSE, NE, PHYS': [True,
                                                                                                                                                                                              ['ME 400', 'MTE 200', 'ME 238', 'MTE 300']]
                   }

# Test 3: Concentration split between 3 SYDE and 1BME
amath_test3 = ["AMATH 431", "ENGL 100", "SYDE 400", "AMATH 420", "ECON 450",
          "AMATH 480", "AMATH 351", "SYDE 200", "PHYS 121", "BME 238", "PMATH 332",
          "MATH 237", "CS 371", "AMATH 478", "SYDE 300"]

amath_test3_expected = {
    'Complete all of: AMATH 231, AMATH 342, AMATH 351, AMATH 353, PHYS 121': [False, ['AMATH 351', 'PHYS 121']],
    'Complete one of: AMATH 242, CS 371': [True, ['CS 371']],
    'Complete one of: AMATH 250, AMATH 251': [False, []],
    'Complete one of: AMATH 332, PMATH 332, PMATH 352': [True, ['PMATH 332']],
    'Complete one of: MATH 237, MATH 247': [True, ['MATH 237']],
    'Complete 3 AMATH courses at the 400 level': [True, ['AMATH 431', 'AMATH 420', 'AMATH 480']],
    'Complete 1 additional AMATH course at the 300/400 level': [True, ['AMATH 478']],
    'Complete 5 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [False, []],
    'Complete 4 additional courses, all from the same subject code from: AE, BIOL, BME/SYDE, CHE, CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME/MTE, MNS, MSE, NE, PHYS': [True, ['SYDE 400', 'SYDE 200', 'BME 238', 'SYDE 300']]
}


# Test 4: Concentration in ECON with some ME and MTE courses done
amath_test4 = ["AMATH 431", "ENGL 100", "ME 400", "AMATH 420", "ECON 450",
          "ACTSC 231", "AMATH 351", "MTE 200", "PHYS 121", "ECON 100",
          "ECON 201", "ECON 352", "PMATH 332",
          "MATH 237", "AMATH 478", "MATBUS 100", "AMATH 100",
          "AMATH 330", "PMATH 333", "ACTSC 234"]

amath_test4_expected = {
    'Complete all of: AMATH 231, AMATH 342, AMATH 351, AMATH 353, PHYS 121': [False, ['AMATH 351', 'PHYS 121']],
    'Complete one of: AMATH 242, CS 371': [False, []],
    'Complete one of: AMATH 250, AMATH 251': [False, []],
    'Complete one of: AMATH 332, PMATH 332, PMATH 352': [True, ['PMATH 332']],
    'Complete one of: MATH 237, MATH 247': [True, ['MATH 237']],
    'Complete 3 AMATH courses at the 400 level': [True, ['AMATH 431', 'AMATH 420', 'AMATH 478']],
    'Complete 1 additional AMATH course at the 300/400 level': [True, ['AMATH 330']],
    'Complete 5 additional courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT': [True, ['ACTSC 231', 'MATBUS 100', 'AMATH 100', 'PMATH 333', 'ACTSC 234']],
    'Complete 4 additional courses, all from the same subject code from: AE, BIOL, BME/SYDE, CHE, CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME/MTE, MNS, MSE, NE, PHYS': [True, ['ECON 450', 'ECON 100', 'ECON 201', 'ECON 352']],
}



# Asserts for AMATH

def test_amath_0():
    assert check_amath_major(amath_test0) == amath_test0_expected

def test_amath_1():
    assert check_amath_major(amath_test1) == amath_test1_expected

def test_amath_2():
    assert check_amath_major(amath_test2) == amath_test2_expected

def test_amath_3():
    assert check_amath_major(amath_test3) == amath_test3_expected

def test_amath_4():
    assert check_amath_major(amath_test4) == amath_test4_expected

####################################################################

# PURE MATH 



####################################################################

# COMPUTATIONAL MATH 

# Case 0: All reqs met and taken both 
# Computational math

# Case 1: All reqs met
cm_test_1 = ["CS 230", "CS 234", "CS 371", "MATH 247", "MATH 239",
             "ECON 101", "ECON 102", "ECON 212", "AMATH 250", "CO 250",
             "AMATH 342", "STAT 341", "CS 431", "CS 479", "AMATH 382", "AMATH 383"
             ]

cm_test1_expected = {
    "Complete all of: CS 230, CS 234": [True, ["CS 230", "CS 234"]],
    
    "Complete one of: AMATH 242, CS 371": [True, ["CS 371"]],
    
    "Complete one of: MATH 237, MATH 247": [True, ["MATH 247"]],
    
    "Complete one of: MATH 239, MATH 249": [True, ["MATH 239"]],
    
    "Complete 3 non-math courses from the same subject code (AE, BIOL, BME, CHE, CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME, MNS, MSE, MTE, NE, PHYS, SYDE)": 
        [True, ["ECON 212", "ECON 101", "ECON 102"]],
    
    "List 1 Requirement - Complete 2 courses from these options: AMATH 250/251/350, CO 250/255, CS 245/CS 245E/PMATH 330/PMATH 432, CS 246/246E": 
        [True, ["AMATH 250", "CO 250"]],
    
    "List 2 requirement - Complete 2 courses from these options: AMATH 342, CS 475, PMATH 370, CO 367/CO 353, STAT 340/341": 
        [True, ["AMATH 342", "STAT 341"]],
    
    "Complete 4 additional courses in at least 2 different subject codes, at least 2 of which are 400 level": 
        [True, ["CS 431", "CS 479", "AMATH 382", "AMATH 383"]],
}


# Case 2: Test that in list 1, the two courses are in different subject codes - should fail list 1 req
cm_test2 = ["CS 230", "CS 234", "CS 371", "MATH 247", "MATH 239",
            "ECON 101", "ECON 102", "ECON 212",
            "CS 245E", "CS 246", # only one course should be applied since list 1 requires the two courses to be in different subject codes
            "AMATH 342", "STAT 341", "CS 431", "CS 479", "STAT 441", "STAT 444"]

cm_test2_expected = {
    "Complete all of: CS 230, CS 234": [True, ["CS 230", "CS 234"]],
    
    "Complete one of: AMATH 242, CS 371": [True, ["CS 371"]],
    
    "Complete one of: MATH 237, MATH 247": [True, ["MATH 247"]],
    
    "Complete one of: MATH 239, MATH 249": [True, ["MATH 239"]],
    
    "Complete 3 non-math courses from the same subject code (AE, BIOL, BME, CHE, CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME, MNS, MSE, MTE, NE, PHYS, SYDE)": 
        [True, ["ECON 212", "ECON 101", "ECON 102"]],  # 3 ECONs
    
    "List 1 Requirement - Complete 2 courses from these options: AMATH 250/251/350, CO 250/255, CS 245/CS 245E/PMATH 330/PMATH 432, CS 246/246E": 
        [False, ["CS 245E"]],
    
    "List 2 requirement - Complete 2 courses from these options: AMATH 342, CS 475, PMATH 370, CO 367/CO 353, STAT 340/341": 
        [True, ["AMATH 342", "STAT 341"]],
    
    "Complete 4 additional courses in at least 2 different subject codes, at least 2 of which are 400 level": 
        [True, ["CS 431", "CS 479", "STAT 441", "STAT 444"]],
}

# Case 3: In List 3, only one of CS431 or CS451 may be taken.
cm_test3 = ["CS 230", "CS 234", "CS 371", "MATH 247", "MATH 239",
            "ECON 101", "ECON 102", "ECON 212",
            "CS 245E", "CS 246",
            "AMATH 342", "STAT 341", "CS 431", "CS 451", # should be incomplete as only CS 431 will be used
            "STAT 441", "STAT 444"]

cm_test3_expected = {
    "Complete all of: CS 230, CS 234": [True, ["CS 230", "CS 234"]],
    
    "Complete one of: AMATH 242, CS 371": [True, ["CS 371"]],
    
    "Complete one of: MATH 237, MATH 247": [True, ["MATH 247"]],
    
    "Complete one of: MATH 239, MATH 249": [True, ["MATH 239"]],
    
    "Complete 3 non-math courses from the same subject code (AE, BIOL, BME, CHE, CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME, MNS, MSE, MTE, NE, PHYS, SYDE)": 
        [True, ["ECON 212", "ECON 101", "ECON 102"]],  # 3 ECONs
    
    "List 1 Requirement - Complete 2 courses from these options: AMATH 250/251/350, CO 250/255, CS 245/CS 245E/PMATH 330/PMATH 432, CS 246/246E": 
        [False, ["CS 245E"]],
    
    "List 2 requirement - Complete 2 courses from these options: AMATH 342, CS 475, PMATH 370, CO 367/CO 353, STAT 340/341": 
        [True, ["AMATH 342", "STAT 341"]],
    
    "Complete 4 additional courses in at least 2 different subject codes, at least 2 of which are 400 level": 
        [False, ["CS 431", "STAT 441", "STAT 444"]],
}

# Checking that the courses are in at least 2 diff subject codes in "Complete 4 additional courses, taken from List 2 or List 3; choices must be in at least two different subject codes (AMATH, CO, CS, PMATH, STAT), and 2 courses must be at the 400-level
cm_test4 = ["CS 230", "CS 234", "CS 371", "MATH 247", "MATH 239",
            "ECON 101", "ECON 102", "ECON 212",
            "CS 245E", "CS 246",
            "AMATH 342", "STAT 341",
            "CO 450", "CO 452", "CO 454", "C0 456"] # should not be accepted as same subject code

cm_test4_expected = {
    "Complete all of: CS 230, CS 234": [True, ["CS 230", "CS 234"]],
    
    "Complete one of: AMATH 242, CS 371": [True, ["CS 371"]],
    
    "Complete one of: MATH 237, MATH 247": [True, ["MATH 247"]],
    
    "Complete one of: MATH 239, MATH 249": [True, ["MATH 239"]],
    
    "Complete 3 non-math courses from the same subject code (AE, BIOL, BME, CHE, CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME, MNS, MSE, MTE, NE, PHYS, SYDE)": 
        [True, ["ECON 212", "ECON 101", "ECON 102"]],  # 3 ECONs
    
    "List 1 Requirement - Complete 2 courses from these options: AMATH 250/251/350, CO 250/255, CS 245/CS 245E/PMATH 330/PMATH 432, CS 246/246E": 
        [False, ["CS 245E"]],
    
    "List 2 requirement - Complete 2 courses from these options: AMATH 342, CS 475, PMATH 370, CO 367/CO 353, STAT 340/341": 
        [True, ["AMATH 342", "STAT 341"]],
    
    "Complete 4 additional courses in at least 2 different subject codes, at least 2 of which are 400 level": 
        [False, ["CO 450", "CO 452", "CO 454"]],
}

# Checking that for last req at least 2 courses need to be at the 400 level
cm_test5 = ["CS 230", "CS 234", "CS 371", "MATH 247", "MATH 239",
            "ECON 101", "ECON 102", "ECON 212",
            "CS 245E", "CS 246",
            "AMATH 342", "STAT 341", "STAT 431", "CS 351",
            "CS 231", "CS 200",
            "CO 450", "CO 351", "AMATH 343", "CS 341"] # should not be accepted as only 1 is 400 level

cm_test5_expected = {
    "Complete all of: CS 230, CS 234": [True, ["CS 230", "CS 234"]],
    
    "Complete one of: AMATH 242, CS 371": [True, ["CS 371"]],
    
    "Complete one of: MATH 237, MATH 247": [True, ["MATH 247"]],
    
    "Complete one of: MATH 239, MATH 249": [True, ["MATH 239"]],
    
    "Complete 3 non-math courses from the same subject code (AE, BIOL, BME, CHE, CHEM, CIVE, EARTH, ECE, ECON, ENVE, GEOE, ME, MNS, MSE, MTE, NE, PHYS, SYDE)": 
        [True, ["ECON 212", "ECON 101", "ECON 102"]],  # 3 ECONs
    
    "List 1 Requirement - Complete 2 courses from these options: AMATH 250/251/350, CO 250/255, CS 245/CS 245E/PMATH 330/PMATH 432, CS 246/246E": 
        [False, ["CS 245E"]],
    
    "List 2 requirement - Complete 2 courses from these options: AMATH 342, CS 475, PMATH 370, CO 367/CO 353, STAT 340/341": 
        [True, ["AMATH 342", "STAT 341"]],
    
    "Complete 4 additional courses in at least 2 different subject codes, at least 2 of which are 400 level": 
        [False, ["CO 450", "CO 351", "AMATH 343", 'CS 341']],
}

# For list 2: one test case where both courses are from the "any option", then test cases to make
# sure that STAT 340/341 and CO 353/367 are not counted as separate.
# Students who take CO255 may take CO450 or CO466 instead of CO353 or CO367.

def test_cm_1():
    assert check_comp_math_reqs(cm_test_1) == cm_test1_expected

def test_cm_2():
    assert check_comp_math_reqs(cm_test2) == cm_test2_expected

def test_cm_3():
    assert check_comp_math_reqs(cm_test3) == cm_test3_expected

def test_cm_4():
    assert check_comp_math_reqs(cm_test4) == cm_test4_expected

def test_cm_5():
    assert check_comp_math_reqs(cm_test5) == cm_test5_expected

####################################################################

# PMATH

# Case 0: All reqs met
pmath_test0 = ['PMATH 401', 'PMATH 402', 'PMATH 403', 'PMATH 405', 'PMATH 415',
               'MATH 247', 'MATH 249', 'PMATH 367',
               'PMATH 347', 'PMATH 348', 'PMATH 351', 'PMATH 352', 'PMATH 450'] # core courses

pmath_test0_expected = {
    "Complete all of: PMATH 347, PMATH 348, PMATH 351, PMATH 352, PMATH 450": [True, ['PMATH 347', 'PMATH 348', 'PMATH 351', 'PMATH 352', 'PMATH 450']],
    "Complete one of: MATH 237, MATH 247": [True, ['MATH 247']],
    "Complete one of: MATH 239, MATH 249": [True, ['MATH 249']],
    "Complete one of: PMATH 365, PMATH 367": [True, ['PMATH 367']],
    "Complete 3 additional PMATH courses at the 400 level": [True, ['PMATH 401', 'PMATH 402', 'PMATH 403']],
    "Complete 2 additional 400 level courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [True, ['PMATH 405', 'PMATH 415']]
  }

# Case 1: Missing a core course and last 2 reqs unmet
pmath_test1 = ['PMATH 401', 'PMATH 402', 'PMATH 333', 'PMATH 415',
               'MATH 237', 'MATH 239', 'PMATH 367',
               'PMATH 347', 'PMATH 351', 'PMATH 352', 'PMATH 450'] # core courses

pmath_test1_expected = {
    "Complete all of: PMATH 347, PMATH 348, PMATH 351, PMATH 352, PMATH 450": [False, ['PMATH 347', 'PMATH 351', 'PMATH 352', 'PMATH 450']],
    "Complete one of: MATH 237, MATH 247": [True, ['MATH 237']],
    "Complete one of: MATH 239, MATH 249": [True, ['MATH 239']],
    "Complete one of: PMATH 365, PMATH 367": [True, ['PMATH 367']],
    "Complete 3 additional PMATH courses at the 400 level": [True, ['PMATH 401', 'PMATH 402', 'PMATH 415']],
    "Complete 2 additional 400 level courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [False, []]
  }


def test_pmath_0():
    assert check_pmath_major(pmath_test0) == pmath_test0_expected
    
def test_pmath_1():
    assert check_pmath_major(pmath_test1) == pmath_test1_expected


####################################################################
# Math studies

# Case 1: All reqs met
mst_test1 = ["MATH 136", "MATH 137", "MATH 138", "MATH 135", "MATH 225", "MATH 237",
            "STAT 220", "STAT 221", "CS 115", "CS 116",
            "SPCOM 100", "ENGL 108D",
            "PMATH 330", "PMATH 340", "CS 330", "CS 338", "CS 436", "CS 371",
            "MATBUS 371", "STAT 341", "CS 479", "CS 431",
            "CS 230", "CS 231", "CS 234", "CS 200",
            "ECON 101", "ECON 102", "ECON 201", "CLAS 104", "PSYCH 101", "BET 100", "BET 210", "ECON 212",
            "AMATH 250", "ACTSC 231",
            "HIST 101", "ENGL 109", "BET 456", "FR 101"]

mst_test1_expected = {
    "Complete one of the following: MATH 106, MATH 136, MATH 146": [True, ["MATH 136"]],
    "Complete one of the following: MATH 127, MATH 137, MATH 147": [True, ["MATH 137"]],
    "Complete one of the following: MATH 128, MATH 138, MATH 148": [True, ["MATH 138"]],
    "Complete one of the following: MATH 135, MATH 145": [True, ["MATH 135"]],
    "Complete one of the following: MATH 225, MATH 235, MATH 245": [True, ["MATH 225"]],
    "Complete one of the following: MATH 207, MATH 237, MATH 247, MATH 229, MATH 239, MATH 249": [True, ["MATH 237"]],
    "Complete one of the following: STAT 220, STAT 230, STAT 240": [True, ["STAT 220"]],
    "Complete one of the following: STAT 221, STAT 231, STAT 241": [True, ["STAT 221"]],
    "Complete one of the following: CS 115, CS 135, CS 145": [True, ["CS 115"]],
    "Complete one of the following: CS 116, CS 136, CS 146": [True, ["CS 116"]],
    "1st Communication Skills Requirement": [True, ["SPCOM 100"]],
    "2nd Communication Skills Requirement": [True, ["ENGL 109"]],
    "Ten mathematics 3XX and/or 4XX courses": [
        True,
        ["PMATH 330", "PMATH 340", "CS 330", "CS 338", "CS 436", "CS 371",
            "MATBUS 371", "STAT 341", "CS 479", "CS 431"]
    ],
    "Four additional mathematics courses": [
        True,
        ["CS 230", "CS 231", "CS 234", "CS 200"]
    ],
    "Eight additional non-math courses": [
        True,
        ["ENGL 108D", "ECON 101", "ECON 102", "ECON 201", "CLAS 104", "PSYCH 101", "BET 100", "BET 210"]
    ],
    "Two additional math courses or two courses that contribute to a minor outside of Mathematics": [
        True,
        ["AMATH 250", "ACTSC 231"]
    ],
    "Four free-choice electives": [
        True,
        ["ECON 212", "HIST 101", "BET 456", "FR 101"]
    ]
}

# Asserts
def test_ms_1():
    assert math_studies_reqs(mst_test1) == mst_test1_expected

# Math studies: business specialization

# Case: All reqs met


ms_bus_test1 = ['MATH 136', 'MATH 137', 'MATH 138', 'MATH 135', 'MATH 235', 'MATH 237',
                'STAT 230', 'STAT 231', 'CS 135', 'CS 116',
                'SPCOM 100', 'SPCOM 223',
                "AFM 101", "AFM 102", "BUS 121W", "CS 330", "ECON 101", "ECON 102", "ACTSC 231", "AFM 131", 
                "MGMT 244", "CO 255", "CO 370", "CS 338", "STAT 340", "STAT 332",
                "STAT 341", "STAT 444", "STAT 441", "AMATH 250", "AMATH 353",
                "CS 100", "PMATH 330",
                "LS 271", "LS 319", "HRM 101"]

ms_bus_test1_expected = {
    "Complete one of the following: MATH 106, MATH 136, MATH 146": [True, ["MATH 136"]],
    "Complete one of the following: MATH 127, MATH 137, MATH 147": [True, ["MATH 137"]],
    "Complete one of the following: MATH 128, MATH 138, MATH 148": [True, ["MATH 138"]],
    "Complete one of the following: MATH 135, MATH 145": [True, ["MATH 135"]],
    "Complete one of the following: MATH 225, MATH 235, MATH 245": [True, ["MATH 235"]],
    "Complete one of the following: MATH 207, MATH 237, MATH 247, MATH 229, MATH 239, MATH 249": [True, ["MATH 237"]],
    "Complete one of the following: STAT 220, STAT 230, STAT 240": [True, ["STAT 230"]],
    "Complete one of the following: STAT 221, STAT 231, STAT 241": [True, ["STAT 231"]],
    "Complete one of the following: CS 115, CS 135, CS 145": [True, ["CS 135"]],
    "Complete one of the following: CS 116, CS 136, CS 146": [True, ["CS 116"]],
    "1st Communication Skills Requirement": [True, ["SPCOM 100"]],
    "2nd Communication Skills Requirement": [True, ["SPCOM 223"]],
    "Complete one of the following: STAT 321, STAT 322, STAT 331, STAT 332": [True, ["STAT 332"]],
    "Complete one of the following: CO 227, CO 250, CO 255": [True, ["CO 255"]],
    "Complete one of the following: CO 327, CO 370": [True, ["CO 370"]],
    "Complete one of the following: AFM 272, ACTSC 291, ACTSC 221, ACTSC 231": [True, ["ACTSC 231"]],
    "Complete two of the following: CS 200, CS 338, CS 430, STAT 340": [True, ["CS 338", "STAT 340"]],
    "Complete all of: CS 330, AFM 101, AFM 102, BUS 121W, ECON 101, ECON 102": [True, ["CS 330", "AFM 101", "AFM 102", "BUS 121W", "ECON 101", "ECON 102"]],
    "Complete one of: AFM 131, ARBUS 101, BUS 111W": [True, ["AFM 131"]],
    "Complete one of: ARBUS 302, BUS 252W, MGMT 244": [True, ["MGMT 244"]],
    "Complete 7 additional math courses from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [True, ["STAT 341", "STAT 444", "STAT 441", "AMATH 250", "AMATH 353", "CS 100", "PMATH 330"]],
    "Complete 10 math courses at the 300 or 400-level (including any taken above) from: ACTSC, AMATH, CO, CS, MATBUS, MATH, PMATH, STAT": [True, ['CS 330', 'CO 370', 'CS 338', 'STAT 340', 'STAT 332', "STAT 341", "STAT 444", "STAT 441", "AMATH 353", "PMATH 330"]],
    "Complete one of: LS 271, PACS 202": [True, ["LS 271"]],
    "Complete one of: LS 319, PACS 323": [True, ["LS 319"]],
    "Complete one course from AFM, BUS, COMM, ECON, HRM, MSE, STV": [True, ["HRM 101"]]
}

# Asserts    
def test_mb_1():
    assert math_studies_business_reqs(ms_bus_test1) == ms_bus_test1_expected


