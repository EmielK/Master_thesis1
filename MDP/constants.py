from .functions.TPM_gammaprocess import TPM_gammaprocess

STORAGE_COSTS = 0
BACK_ORDER_COSTS = 0.25

C_PM = 10
C_CM = 30

COST_MISSED_ORDER = 4

T_PM = 1
T_CM = 3

MAX_BACK_ORDER = 4
MAX_STORAGE = 4

NUM_STATES = 20
# No production, 1, and 2.
PROD_SETTINGS = 3

PROB_MATRIX_1 = TPM_gammaprocess(5, 0.2, 1, NUM_STATES - 1, 0.1)
PROD_1 = 1
PROD_LEN_1 = 2
PROB_MATRIX_2 = TPM_gammaprocess(7.5, 0.3, 1, NUM_STATES - 1, 0.1)
PROD_2 = 2
PROD_LEN_2 = 1
# need one index extra since DN is also an option, for initialising array
MAX_PROD_TIME = PROD_LEN_1 + 1
MAX_MAIN_TIME = T_CM + 1
# + 1 since 0 is also an option
STOCK_SIZE = MAX_BACK_ORDER + MAX_STORAGE + 1

DN = 0
MAINTENANCE = 1

PROB_NEW_JOBS = 0.3
MAX_NUM_NEW_JOBS = 3
PROB_1 = 0.5
PROB_2 = 0.35
PROB_3 = 0.15

# arbitrary large number
M = 10000
