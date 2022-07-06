# re for regular expressions
# https://regex101.com/ for testing playground
import re

# 8 characters long
# contain letters, numbers $%#@
pattern = re.compile(r"[a-zA-Z0-9]{8,}")
password = '345j'
check = pattern.fullmatch(password)
print(check)
