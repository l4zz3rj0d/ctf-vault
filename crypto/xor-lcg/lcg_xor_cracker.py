import binascii

PLAIN1_HEX = "57656c636f6d6520746f206d7920756c7472612073656375726520656e6372797074696f6e2073657276696365210a54686973206d6573736167652069732066756c6c79206b6e6f776e20746f20796f752e0a537572656c7920796f752063616e6e6f7420627265616b206d792074686973206369706865722e2e2e0a"
CIPH1_HEX  = "c6956bf53271f6a2dda7bf830cd45eb6b5d25666fea9a047ab1deffbcbc729f381240e99d35c80877b5e962db075816e4969e486804950e158bf4ade6c779b8c24dcab2f3db73d2d1ee67fda5a9492f5f44efd5538fee69ee018f6311044782bdf7e48c25d5ec1c7a8839f63ec343f9288b37705c49c8b378bb6c190cf"
CIPH3_HEX  = "e58272e5297fe7e4d2b1af9b2a901bb4b5ff0430bea29c5cea4babc197fb39d5823d5384c923c7bd7d40ce7ba8"

plain1 = bytes.fromhex(PLAIN1_HEX)
cipher1 = bytes.fromhex(CIPH1_HEX)
cipher3 = bytes.fromhex(CIPH3_HEX)

# Step 1: Derive keystream (s values)
keystream = [p ^ c for p, c in zip(plain1, cipher1)]

# Step 2: Solve for A and C from first three keystream bytes
def inv_mod(a, m=256):
    a %= m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("No modular inverse")

s1, s2, s3 = keystream[0], keystream[1], keystream[2]
A = ((s3 - s2) * inv_mod(s2 - s1, 256)) % 256
C = (s2 - A * s1) % 256
print(f"A={A}, C={C}")

# Step 3: Try all SEED values (0–255)
def step(x, y, z): return (x * z + y) & 0xFF
def mask_bytes(payload, x, y, seed):
    s = seed & 0xFF
    out = bytearray()
    for b in payload:
        s = step(x, y, s)
        out.append(b ^ s)
    return bytes(out)

for seed_guess in range(256):
    test = mask_bytes(plain1, A, C, seed_guess)
    if test == cipher1:
        SEED = seed_guess
        print(f"Found SEED = {SEED}")
        break

# Step 4: Decrypt CIPH3
flag = mask_bytes(cipher3, A, C, SEED)
print("FLAG:", flag.decode(errors="ignore"))
