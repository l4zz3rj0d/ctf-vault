# 📝 Connection Tester – Complete Writeup (Web Exploitation)

🚩 Category: Web
🔧 Techniques: SQL Injection → Command Injection
💻 Stack: Node.js / Express

#1. Introduction 🔍

This challenge revolves around a small web application created by “junior developers” — which, in CTF language, is basically code for:

“Please hack this. It won’t fight back.” 😎

The app includes:

A login portal

An admin dashboard

A “Connectivity Tool” meant to test network connections

The exploitation chain turned out to be:

👉 SQL Injection → Admin Access → Command Injection → Flag Extraction

Simple, elegant, and absolutely catastrophic for the application.

# 2. SQL Injection on the Login Page 💉

The login page responded differently to invalid usernames vs invalid passwords — a hint of username enumeration.

Testing classic SQLi payloads immediately worked. Using:  admin' OR 1=1--

we bypassed authentication and landed straight in the Administrator Dashboard.
No filters. No prepared statements.
A developer’s worst nightmare and a hacker’s warm hug. 🤝

# 3. Discovering the Connectivity Tool 🌐

Inside the admin panel, a button directed us to: /connect

The page source contained a minimal POST form:
<form method="post" action="/connect">
  <label>Target Address</label>
  <input type="text" name="address" placeholder="127.0.0.1" />
  <button type="submit">Submit</button>
</form>
No JavaScript. No client-side validation.
Whatever danger was ahead, it was on the backend. ⚙️

# 4. Testing the Connectivity Feature 🧪

Submitting: 127.0.0.1
returned:connecting to 127.0.0.1

A simple echo.
Then we attempted command injection using:
127.0.0.1; ls
The output was:
connecting to 127.0.0.1
ls: cannot access '...': No such file or directory

This revealed a critical detail:

The backend echoes our input

The backend executes a shell command using our input

The developer appends ... after our input

The appended ... breaks our injected command

This confirmed:
⚠️ We had command execution — but needed to escape the trailing dots.

# 5. Achieving Command Injection 💥

To bypass the broken suffix, we used a clean escape payload:; ls -la / #

Explanation:

; → ends the original command

ls -la / → our custom command

 → comments out the ... added by the backend

Success.
We now had a shell on their server. 🔓🐚

The output revealed several directories, including: /app

A classic location for CTF flags.

# 6. Locating and Extracting the Flag 🏴‍☠️

After navigating into /app, we executed:; cat /app/flag.txt #

And like magic, the flag appeared. ✨

# 7. Final Flag 🎉
PCTF{C0nn3cti0n_S3cured}

# 8. Conclusion 🧠

This challenge neatly demonstrated two fundamental vulnerabilities:

🔸 SQL Injection

Allowed full login bypass.

🔸 Command Injection

Allowed arbitrary OS command execution due to unsafe handling of user input in shell commands.

Together, these flaws resulted in complete compromise of the application.
A great example of why developers should never trust user input — especially junior ones. 😅
