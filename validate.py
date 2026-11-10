import re
email = input("what's ur email?").strip()

if re.search(r"^.+@.+\.edu$",email):
    print("valid")

else:
    print("invalid")