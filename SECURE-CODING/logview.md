## Challenge Overview

The Professor provides an internal tool named Logview, designed to display application logs.
However, improper path handling allows attackers to escape the intended directory and read arbitrary files.

The task is to identify the vulnerability, exploit it, and retrieve the vault key and flag.

## Objective

Identify the file inclusion vulnerability

Exploit path traversal

Leak sensitive environment variables

Retrieve the key and flag

## Vulnerability Discovery

Accessing the application revealed a GET parameter used to fetch files from the server, intended to read files from the normal web/log directory.

By manipulating the parameter with path traversal payloads, it became possible to escape the directory restriction and access system files.

### Example technique:

../../../

## Exploitation (Path Traversal)

Using traversal payloads, the following file was successfully accessed:

/proc/self/environ


This revealed sensitive environment variables, including:

KEY_FILE=/run/secrets/sc-01.key
FLAG=TDHCTF{BELLA_CIAO_NO_MORE_DOT_DOT_SLASH}


### This confirmed:

The flag was already exposed via environment leakage

The key was stored in a protected file path

## Key Retrieval

Using the same path traversal technique, the key file was accessed:

/run/secrets/sc-01.key


### Result:

ac0670b920d86278811d00e928e138627700edc1c875dfd52c8a64997537905e

## Final Flag
TDHCTF{BELLA_CIAO_NO_MORE_DOT_DOT_SLASH}

## Key Takeaways

Unvalidated file paths lead directly to path traversal vulnerabilities

/proc/self/environ is a goldmine when environment variables contain secrets

Secrets should never be stored in readable environment variables

Directory restrictions must be enforced using realpath validation, not trust
