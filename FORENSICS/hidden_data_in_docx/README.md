# 📝 Forensic Challenge Writeup – Hidden Data in a DOCX File (Steganography)
🎯 Overview

We were given a suspicious Word document named word_sea_adventures.docx with the hint that something was hidden inside.
DOCX files are actually ZIP containers, so the challenge revolved around extracting embedded files and analyzing them for steganographic payloads.

# 🧩 1. Inspecting the DOCX File
✔ Confirmed DOCX = ZIP container
xxd word_sea_adventures.docx | head


Header showed:

50 4B 03 04


Meaning it’s really a ZIP archive.

# ✔ Extracted contents
mkdir docx_unzipped
unzip word_sea_adventures.docx -d docx_unzipped


Inside we found:

crab.jpg

sponge.jpg

squid.jpg

Three large images = perfect candidates for steganography.

# 🦀 2. Steg Analysis — crab.jpg
stegseek crab.jpg


Stegseek immediately extracted a hidden file:

crab.jpg.out

Contents of crab.jpg.out
Mr Crabs heard that his cashier may be hiding some money and maybe a flag somewhere.


Interpretation:
Mr. Krabs → Cashier → SpongeBob → Check sponge.jpg.

# 🧽 3. Steg Analysis — sponge.jpg
stegseek sponge.jpg


This produced:

sponge.jpg.out

Contents of sponge.jpg.out
Spongebob is so chill! Why would he be hiding any flags?


This is a fake-out message — meaning the real flag is NOT here.

Who’s left?

Squidward.

# 🐙 4. Steg Analysis — squid.jpg
stegseek squid.jpg


This revealed:

squid.jpg.out

Contents of squid.jpg.out
I guess you found handsome squidward... even his looks can't hide the flag.
tctf{w0rD_f1le5_ar3_als0_z1p}


And there it is — the real hidden flag.

# 🏁 Final Flag
tctf{w0rD_f1le5_ar3_als0_z1p}

# 🧠 Conclusion

This challenge demonstrated:

DOCX = ZIP container

Need to extract internal media

Multiple layers of steganography

Clue-based chain (Mr. Krabs → SpongeBob → Squidward)

Only Squidward had the real flag

You solved it cleanly and logically — and extracted every hidden message along the way.
