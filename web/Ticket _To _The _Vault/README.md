## Challenge Overview

The Directorate runs a public "tip portal" intended for anonymous submissions.
However, weak access controls and exposed metadata allow attackers to discover administrative functionality and sensitive internal content.

By uncovering hidden paths and reused credentials, it becomes possible to access protected admin resources and retrieve the key and flag.

## Objective

Enumerate hidden endpoints

Discover exposed credentials

Gain administrative access

Retrieve the key and the flag

## Discovery (robots.txt)

Checking the robots.txt file revealed highly sensitive information:

Disallow: /admin
Disallow: /admin/tickets
Disallow: /admin/flag

# CTF Discovery: Default user credentials
# Tokyo: tokyo / rio123
# The Professor: admin / admin123


### This exposed:

Hidden administrative paths

Valid user credentials

Valid admin credentials

This immediately indicated broken security hygiene.

## Exploitation

Using the disclosed admin credentials:

Username: admin
Password: admin123


Access was obtained to the admin area.

### Visiting the protected endpoint:

/admin/flag


Returned both the flag and the key directly.

## Key
fd19b36f825efe06c7a8786f42be22c3add7ff8c543734d35d1af40480457662

## Final Flag
TDHCTF{THE_BOT_DID_THE_DIRTY_WORK}

## Key Takeaways

robots.txt must never contain sensitive paths or credentials

Default credentials should never exist in production systems

Security through obscurity fails instantly when metadata is exposed

Enumeration is often enough to fully compromise poorly designed systems
