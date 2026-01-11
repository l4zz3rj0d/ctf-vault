## Challenge Overview

A password reset flow protects a Directorate access badge.
The implementation is intentionally insecure, especially in how reset tokens are generated, stored, and validated.

The task is to rebuild the reset flow securely so that the application validates the fixes and unlocks access to the session key and flag.

## Objective

Review the vulnerable reset implementation

Fix insecure token handling

Enforce expiration and one-time use

Pass all security checks

Retrieve the key and the flag

## Security Fixes Implemented

The reset logic was patched to follow proper secure coding practices.

### Implemented protections:

Secure random token generation:
```
crypto.randomBytes(32).toString("hex")
```

Hash-at-rest (do not store raw tokens):
```
store hash(token) instead of token
```

Token expiration:
```
expiresAt = Date.now() + 15 * 60 * 1000
```

One-time use enforcement:
```
rec.used = true
```

Timing-safe comparison:
```
crypto.timingSafeEqual()
```

After applying these changes, the application validated the secure implementation and unlocked the protected endpoints.

## Key
eca462858f508d2003807fde881e1d07b09bf5e6149784da330c34ac46433ead

## Final Flag
TDHCTF{ONE_TIME_TOKEN_ONE_TIME_HEIST}

## Key Takeaways

Reset flows are critical attack surfaces and must be implemented carefully

Tokens must be random, short-lived, hashed, and single-use

Timing-safe comparisons prevent subtle authentication leaks

Fixing security flaws can be just as valuable as exploiting them
