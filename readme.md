Generators to test:
1. Linear Congruential Generator: X{n+1} = (aX{n} + c)%m - used in rand() in c/c++
2. Mersenne Twister - mt19937 (currently being used in Cake) - benchmark
3. Xorshift (**imp)
4. Xoshiro (**imp)
5. Middle Square Weyl Sequence (not required)
6. Multiple With Carry (**imp)
7. Philox
8. Permuted Congruential Generator
9. Ranlux (available in GNU GSL)
10. AES Counter-based RNG


Statistical Tests to Perform:
1. Chi-Square 
2. Kolmogorov-Smirnov 
3. Anderseon-Darling 
4. Runs (Wald-Wolfowitz)
5. Serial Correlation
6. Frequency Test

time + memory usage tests