## Challenge Overview

The Directorate distributes a journaling tool called Confession App, supposedly for agent well-being.
Suspicious as expected, the binary hides sensitive logic that can be uncovered with basic analysis.

Goal: extract the passphrase and retrieve the hidden key and flag.

## Objective

Analyze the binary

Discover how validation works

Recover the passphrase

Use it to obtain the flag

## Artifact

Binary: confession_app

## Initial Analysis (strings)

Instead of heavy reversing, running strings on the binary already revealed valuable clues:

CHALLENGE_KEY
127.0.0.1
{"passphrase":"%s"}
"key":"
"flag":"
POST /validate.php HTTP/1.1


This suggested:

The binary communicates with a web endpoint

The endpoint is /validate.php

JSON is used to send a passphrase

This gave a clear direction on where to look next.

## validate.php Analysis

Inspecting validate.php revealed the full logic and the expected passphrase directly in the source code.

Hardcoded expected passphrase:

The network gateway location is now revealed to us


The script validates the input and, on success, returns both the key and the flag.

## Exploitation

Running the binary and entering the recovered passphrase:

./confession_app
=== Confession App v1.0 ===
What is the passphrase of the vault?
> The network gateway location is now revealed to us


Output:

Network Gateway Identified
Key: 9f2e066481ee032f3e17b39d03185c7da50af36ffb10bdeda021683dd2e749af
Flag: TDHCTF{confession_gateway_phrase}

## Final Flag
TDHCTF{confession_gateway_phrase}

## Key Takeaways

strings can expose critical application behavior

Hardcoded secrets in backend code are trivial to extract

Always inspect related server files when binaries hint at web interaction

Obfuscation ≠ security (developers, please take notes)
