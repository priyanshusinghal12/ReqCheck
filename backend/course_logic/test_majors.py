from course_logic.checkStatisticsReqs import check_stats_major  # done?
from course_logic.checkActSciReqs import check_actsci_major # done
from course_logic.checkAMathReqs import check_amath_major # done
from course_logic.checkBioStatsReqs import check_biostats_major
from course_logic.checkCompMathReqs import check_comp_math_reqs
from course_logic.checkCSReqs import check_computer_science_major
from course_logic.checkDataScienceReqs import check_data_science_major
from course_logic.checkMathDegreeReqs import check_math_degree_reqs
from course_logic.checkMathEconReqs import check_math_econ_reqs
from course_logic.checkMathFinanceReqs import check_math_finance_reqs
from course_logic.checkMathOptBusReqs import check_math_opt_bus_specialization
from course_logic.checkMathOptOpsReqs import check_math_opt_ops_specialization
from course_logic.checkMathPhysicsReqs import check_math_physics_reqs
from course_logic.checkMathStudiesBusReqs import math_studies_business_reqs
from course_logic.checkMathStudiesReqs import math_studies_reqs
from course_logic.checkMathTeachReqs import check_math_teaching_major
from course_logic.checkPMathReqs import check_pmath_major # done
from course_logic.checkCOReqs import check_co_major

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


# # Case 1: only partially completed concentration.
# cm_test1 = ['CS 230', 'CS 234', # reqd
#             'CS 371', 'MATH 237', 'MATH 249',
#             'ECON 212',
#             ]

# # Case 2: Both ECON and BIO courses present, but BIO closer to completed concentration.
# cm_test1 = ['CS 230', 'CS 234', # reqd
#             'CS 371', 'MATH 237', 'MATH 249',
#             'ECON 212',
#             ]

# Case 3: Testing that "In List 1, the two courses must be in different subject codes.
# In List 3, only one of CS431 or CS451 may be taken.


# Checking that the courses are in at least 2 diff subject codes in "Complete 4 additional courses, taken from List 2 or List 3; choices must be in at least two different subject codes (AMATH, CO, CS, PMATH, STAT), and 2 courses must be at the 400-level

# Testing that 2 courses are at 400 in level in the req above

# For list 2: one test case where both courses are from the "any option", then test cases to make
# sure that STAT 340/341 and CO 353/367 are not counted as separate.
# Students who take CO255 may take CO450 or CO466 instead of CO353 or CO367.
# In List 3, BIOL382 counts as an AMATH course for the purpose of the "at least two different subject codes" requirement.


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