def LinearCongruential_Initialize(a,c, m, X0):
    r"""
    Initialized a linear congruential RNG state.
    
    This state is a list of four integers: [a, c, m, X]
    a,c,m are the parameters of the linear congruential instantiation
    X is the current state of the PRNG.

    INPUT:
    a - coefficient
    c - offset
    m - modulus
    X0 - initial state (seed)

    OUTPUT:
    state - the initial internal state of the RNG.
    """
    return [a, c, m, X0]

def LinearCongruential_Generate(state):
    r"""
    Generates a single linear congruential RNG output and updates the state

    INPUT:
    state - an internal RNG state

    OUTPUT:
    X - a single output of the linear congruential RNG
    """
    a = state[0]
    c = state[1]
    m = state[2]
    X = state[3]
    X_next = (a*X + c)%m
    state[3] = X_next
    return X_next


if __name__ == "__main__":
    a = 121
    c = 1331
    m = 2
    X0 = 1234300
    state = LinearCongruential_Initialize(a, c, m, X0)
    print(LinearCongruential_Generate(state))