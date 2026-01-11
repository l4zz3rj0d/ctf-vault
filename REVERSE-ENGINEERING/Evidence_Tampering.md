## Challenge Overview

Berlin recovers a heavily obfuscated binary named “Evidence Tampering Console”, allegedly used by the Directorate’s internal cleanup unit.
The narrative suggests encrypted strings and timestamp manipulation logic, hinting that the system is designed to rewrite digital history.

The objective was to uncover how the system validates input and extract the hidden intelligence.

## Objective

Analyze the binary (evidence_tool)

Discover hidden endpoints

Inspect backend logic

Retrieve the key and flag

## Artifacts

Binary: evidence_tool

Web files:

/var/www/html/validate.php

/var/www/html/key.txt

## Initial Analysis (strings)

Running strings on the binary revealed a critical clue:

/validate.php


This indicated that the binary communicates with a web endpoint, similar to the previous challenge.

That gave a clear direction: inspect the backend script.

## Backend Inspection

Reading the PHP file:

cat /var/www/html/validate.php


Revealed:

Validation is handled by the binary (not PHP)

The flag is hardcoded inside the script

The key is stored in an external file

Relevant discovery:

$CHALLENGE_FLAG = "TDHCTF{tampered_time_offset}";
$key_file = '/var/www/html/key.txt';

## Key & Flag Retrieval

Using the disclosed path, the key file was read:

cat /var/www/html/key.txt


Output:

232a3a6c2c510de8d3f293aad5b7268fc9d9c90aba566016ded0936b976e73fd


## Final Flag
TDHCTF{tampered_time_offset}

## Key Takeaways

Even heavily obfuscated binaries can leak critical hints through strings

Always follow discovered endpoints — they often expose backend logic

Hardcoding secrets in server files defeats the entire purpose of protection

A single leaked path can collapse the whole security model
