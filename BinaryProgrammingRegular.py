from src.BBTree import BBTree, PSEUDOCOST_BRANCHING, MOST_FRACTIONAL, FIXED_BRANCHING, DEPTH_FIRST, BEST_FIRST, BEST_ESTIMATE
from src.BranchAndBound import GenerateRandomMIP, BranchAndBound

branch_strategy_list = [PSEUDOCOST_BRANCHING, MOST_FRACTIONAL, FIXED_BRANCHING]
search_strategy_list = [DEPTH_FIRST, BEST_FIRST, BEST_ESTIMATE]

# 2.1.1
CONSTRAINTS, VARIABLES, OBJ, MAT, RHS = GenerateRandomMIP(numVars = 10, numCons = 10, density = 0.2,
                                                          maxObjCoeff = 50, maxConsCoeff = 50,
                                                          rand_seed = 5)

# 2.1.2
#CONSTRAINTS, VARIABLES, OBJ, MAT, RHS = GenerateRandomMIP(numVars = 10, numCons = 10, density = 0.2,
#                                                          maxObjCoeff = 50, maxConsCoeff = 50,
#                                                          rand_seed = 6)

# 2.1.3
#CONSTRAINTS, VARIABLES, OBJ, MAT, RHS = GenerateRandomMIP(numVars = 10, numCons = 10, density = 0.2,
#                                                          maxObjCoeff = 50, maxConsCoeff = 50,
#                                                          rand_seed = 8)

# 2.1.4
#CONSTRAINTS, VARIABLES, OBJ, MAT, RHS = GenerateRandomMIP(numVars = 10, numCons = 10, density = 0.2,
#                                                          maxObjCoeff = 50, maxConsCoeff = 50,
#                                                          rand_seed = 9)

for i in range(len(search_strategy_list)):
    for j in range(len(branch_strategy_list)):
        T = BBTree()
        T.set_display_mode('matplotlib')
        opt, LB = BranchAndBound(T, CONSTRAINTS, VARIABLES, OBJ, MAT, RHS,
        branch_strategy = branch_strategy_list[j],
        search_strategy = search_strategy_list[i],
        display_interval = 10000)
        T.set_layout('dot')
        f = open('search_strategy_' + search_strategy_list[i] + '_branch_strategy_' + branch_strategy_list[j] + '.png', 'wb')
        T.write(f, format='png')
        print('########################################################\n'
              '########################################################\n'
              '########################################################\n')