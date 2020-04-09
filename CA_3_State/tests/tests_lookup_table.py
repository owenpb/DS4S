import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import three_state_ca

def test_lookup_19682():
    """
    Test of the lookup function. For the 3-state CA, possible rule numbers are 0,1,2,...,19862. For rule 19682, we should 
    find that every neighborhood maps to state 2. Use an assert statement to test that this is true. 
    
    """
    lt = lookup(19682)
    expected = [2,2,2,2,2,2,2,2] 
    mapping = zip(neighborhoods, expected)
    for neighborhood, expected in mapping:
        assert lt[neighborhood] == expected,\
        "Unexpected ouput for neighborhood {}!".format(neighborhood)
    print("All outputs are correct.") 

def test_lookup_0():
    """
    Test of the lookup function. For the 3-state CA, possible rule numbers are 0,1,2,...,19862. For rule 0, we should 
    find that every neighborhood maps to state 0. Use an assert statement to test that this is true. 
    
    """
    lt = lookup(0)
    expected = [0,0,0,0,0,0,0,0]
    mapping = zip(neighborhoods, expected)
    for neighborhood, expected in mapping:
        assert lt[neighborhood] == expected,\
        "Unexpected ouput for neighborhood {}!".format(neighborhood)
    print("All outputs are correct.") 

def test_lookup_235():
    """
    Test of the lookup function for rule 235. The ternary representation of 235 is 000022201, hence we should get: 
    (0,0)-->1, (0,1)-->0, (0,2)-->2, (1,0)-->2, (1,1)-->2, (1,2)-->0, (2,0)-->0, (2,1)-->0, (2,2)-->0.
    
    """
    lt = lookup(235)
    expected = [1,0,2,2,2,0,0,0]
    mapping = zip(neighborhoods, expected)
    for neighborhood, expected in mapping:
        assert lt[neighborhood] == expected,\
        "Unexpected ouput for neighborhood {}!".format(neighborhood)
    print("All outputs are correct.") 

test_lookup_19682()
test_lookup_0()
test_lookup_235()

