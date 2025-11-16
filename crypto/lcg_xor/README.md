# LCG-XOR Cipher Breaker

This directory contains the solver for a custom XOR cipher where the keystream is 
generated using a linear-congruential-style recurrence:

    s(n+1) = (A * s(n) + C) mod 256

Each plaintext byte is masked as:

    cipher[i] = plaintext[i] ⊕ s(i)

Because the first plaintext (PLAIN1) was known and its matching ciphertext was provided, 
the keystream bytes could be recovered directly:

    s(i) = PLAIN1[i] ⊕ CIPH1[i]

Using s1, s2, s3, we solve for unknown parameters A and C using modular algebra:

    A ≡ (s3 - s2) * inv_mod(s2 - s1, 256)
    C ≡ s2 - A * s1  (mod 256)

After obtaining A and C, we brute-force all 256 possible initial seed values and pick 
the one that correctly regenerates CIPH1. Once the seed is identified, decrypting the 
remaining ciphertext (CIPH3) becomes trivial by regenerating the keystream.

This folder contains:

- `lcg_xor_solver.py` — complete solver script
- Example ciphertexts and derivations
- Final decrypted flag

This approach demonstrates a classic *known-plaintext attack* on a weak keystream-based cipher.
