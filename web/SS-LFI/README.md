🛠️ Warmup CTF – Walkthrough (IDOR → Admin Panel → Crawler → LFI)
1. Initial Access

The challenge provided basic credentials:

guest : guest123


Logging in revealed a simple user dashboard with minimal functionality. Nothing sensitive was exposed initially.

2. IDOR to Gain Admin Access

While exploring the site, an Insecure Direct Object Reference (IDOR) was discovered.
By modifying the request, the admin panel became accessible, which should never have been available to a guest user.

Classic case of “security-by-hoping-no-one-looks.”

3. Admin Panel & the Web Crawler

Inside the admin panel, the only real feature was a website crawler.
It accepted a URL and fetched the response server-side.

But it came with restrictions:

❌ Restrictions:

No numbers

No localhost

No IP addresses

No external URLs that redirect

URL encoded automatically

Most straightforward paths were blocked by the filter.

4. Attempting Direct Flag Access

Trying:

/flag.txt


or

https://pwnsec.ctf.ae/app/challenges/warmup/flag.txt


…always redirected to login.
So direct fetching wouldn’t work.

5. Bypassing the Filter

Creative inputs were attempted — subdirectories, encodings, redirects, relative paths — and eventually the solution was discovered:

✅ The crawler accepted:
file:///flag.txt


This bypassed all URL restrictions because the filter only blocked domains, numbers, and protocols like HTTP — but ignored the file:// scheme.

This allowed the crawler to read local files on the server, giving direct access to the flag.

6. Flag Retrieved

Using the file:// input, the server returned the flag successfully.

Mission accomplished.

📌 Summary

Logged in as guest

Discovered an IDOR → escalated to admin panel

Used admin-only web crawler

Filter blocked external URLs, numbers, IPs

Discovered crawler allowed file:// scheme

Performed local file read

Retrieved the flag

Warmup challenge completed. New technique added to the toolkit. 💼✨
