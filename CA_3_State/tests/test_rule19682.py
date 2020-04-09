from numpy import array_equal

def test_rule19682():
    
    """
    Test that rule 19682 gives the expected behavior, which is that every row of the spacetime field (after the random initial 
    condition) should have all cells in state 2. Evolve the CA for 'time' timesteps and compare each row of the resulting
    spacetime field with the list [2]*length.
    """
    
    config = ECA(19682, initialize(length))
    config.evolve(time)
    observed = config.spacetime
    expected = [2]*length
    
    for t, observed in enumerate(observed[1:]): # skips the random initial condition (first element of the list)
        assert array_equal(observed, expected),\
        "Wrong configuration at time {}!".format(t)
    print('All configurations are correct.') 

test_rule19682()
