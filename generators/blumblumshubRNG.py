#Note: not cryptographically secure RNG.

def random_prime(n : int)->None:
    pass

def BlumBlumShub_Intialize(bitlen, seed):
    r"""
    Intitializes a Blum-Blum-Shub RNG State

    A BBS-RNG State is a list with two elements: [N, X]

    N is a 2*bitlen modulus (product of two primes).
    X is the current state of the PRNG.

    INPUT: 
    bitlen - the bit length of each of the prime factors of n.
    seed - a large random integer to start out the prng.

    OUTPUT:
    state - a BBS-RNG internal state
    """
    # way to generate primes, because we do not know how the internal sage random_prime function works.
    p = 3
    while (p < 2^(bitlen-1) or (3 != (p%4))):
        p = random_prime(2^bitlen)

    q = 3
    while (q < 2^(bitlen-1) or (3 != (q%4))):
        q = random_prime(2^bitlen)
    
    N = p*q
    X = (seed^2 % N)
    state = [N, X]
    return state




def BlumBlumShub_Generate(num_bits, state):
    r"""
    Blum-Blum-Shub random number generator function

    INPUT:
    num_bits- the number of bits (iterations) to generate with this RNG
    state - an internal state of the BBS-RNG (a list [N, x]) - check BlumBlumShub_Intialize().

    OUTPUT:
    random_bits - a num_bits length list of random bits.
    """
    random_bits = []
    N = state[0]
    X = state[1]

    for j in range(num_bits):
        X = X^2 % N
        random_bits.append(X % 2)
    
    #update internal state
    state[1] = X

    return random_bits