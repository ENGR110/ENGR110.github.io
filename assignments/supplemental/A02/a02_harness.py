# author: Juliette Zerick (jzerick@iu.edu)
#   AI for ENGR110, Spring 2019
# Purpose: This is a draft harness for autograder for assignment A01.

import sys
import re

sys.path.append('/usr/local/lib/python3.6/dist-packages')
try:
    import myhdl
except:
    print('failed to import myhdl, bailing')
    sys.exit(1)

def instance_count(pattern,S):
    return len(re.findall(pattern,S))

test_name = sys.argv[1]

if test_name == 'And16':
    from test_And16 import *
elif test_name == 'Or16':
    from test_Or16 import *
elif test_name == 'Not16':
    from test_Not16 import *            
elif test_name == 'Or8Way':
    from test_Or8Way import *
elif test_name == 'Mux':
    from test_Mux import *            
elif test_name == 'DMux':
    from test_DMux import *
elif test_name == 'Mux16':
    from test_Mux16 import *            
elif test_name == 'Mux4Way16':
    from test_Mux4Way16 import *
elif test_name == 'Mux8Way16':
    from test_Mux8Way16 import *            
elif test_name == 'DMux4Way':
    from test_DMux4Way import *
elif test_name == 'DMux8Way':
    from test_DMux8Way import * 
